
#include <istream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <cstdio>
#include <iostream>

using namespace std;

#define LOG(text) //(cout << text << endl)


// - Helpers ------------------------------------------------------------------

template<class T> inline T toNum(const string& str) 
{
	stringstream ss(str);
	T value;
	ss >> value;
	return value;
}

template<class T> inline string toStr(const T& value) 
{
	stringstream ss;
	ss << value;
	return ss.str();
}


// - InputData ----------------------------------------------------------------

class InputData
{
public:
	static const size_t boardSize = 4;
	vector<char> board;
	
public:
	char charAt(size_t x, size_t y) const {
		return board.at((y * boardSize) + x); 
	}
	friend istream& operator >> (istream& stream, InputData& input);
};

inline istream& operator >> (istream& stream, InputData& input) 
{
	string line;
	char value = 0;
	for(size_t y=0; y!=input.boardSize; ++y) {
		getline(stream, line);
		istringstream is(line);
		for(size_t x=0; x!=input.boardSize; ++x) {
			is >> value;
			input.board.push_back(value);
		}
	}
	getline(stream, line);
	return stream;
}


// - OutputData ---------------------------------------------------------------

class OutputData
{
public:
	string result;

public:
	friend ostream& operator << (ostream& stream, OutputData& outputData);
};

inline ostream& operator << (ostream& stream, OutputData& outputData) 
{
	stream << outputData.result;
	return stream;
}


// - Input --------------------------------------------------------------------

class Input
{
public:
	vector<InputData> data;

public:
	friend istream& operator >> (istream& stream, Input& input);
};

inline istream& operator >> (istream& stream, Input& input) 
{
	string line;
	getline(stream, line);
	size_t count = toNum<size_t>(line);

	for(size_t i=0; i<count; ++i) {
		LOG("parsing " << i << "/" << count);
		InputData inputData;
		stream >> inputData;
		input.data.push_back(inputData);
	}

	return stream;
}


// - Output -------------------------------------------------------------------

struct Output 
{
public:
	vector<OutputData> data;

public:
	friend ostream& operator << (ostream& stream, Output& output);
};

inline ostream& operator << (ostream& stream, Output& output)
{
	for(size_t i=0; i!=output.data.size(); ++i) {
		LOG("outputting " << i << "/" << output.data.size());
		stream << "Case #" << (i+1) << ": " << output.data.at(i) << std::endl;
	}
	return stream;
}


// - Solution -----------------------------------------------------------------

struct Solution
{
public:
	void solve(const Input& input, Output& output);
	OutputData solve(const InputData& input);
};

void Solution::solve(const Input& input, Output& output)
{
	for(size_t i=0; i!=input.data.size(); ++i) {
		LOG("solving " << i << "/" << input.data.size());
		OutputData outputData = solve(input.data.at(i));
		output.data.push_back(outputData);
	}
}

void scoreChar(char value, size_t &scoreX, size_t &scoreO, bool& bEndGame) {
	switch(value) {
	case '.': 
		bEndGame = false;
		break;
	case 'X': 
		++scoreX;
		break;
	case 'O': 
		++scoreO;
		break;
	case 'T': 
		++scoreX;
		++scoreO;
		break;
	}
}

OutputData Solution::solve(const InputData& input)
{
	OutputData output;
	bool bEndGame = true;
	bool bWonX = false;
	bool bWonO = false;


	for(size_t y=0; y!=input.boardSize; ++y) {
		size_t scoreX = 0;
		size_t scoreO = 0;
		for(size_t x=0; x!=input.boardSize; ++x) {
			scoreChar(input.charAt(x,y), scoreX, scoreO, bEndGame);
			if(scoreX == input.boardSize) {
				bWonX = true;
			}
			if(scoreO == input.boardSize) {
				bWonO = true;
			}
		}
	}
	
	for(size_t y=0; y!=input.boardSize; ++y) {
		size_t scoreX = 0;
		size_t scoreO = 0;
		for(size_t x=0; x!=input.boardSize; ++x) {
			scoreChar(input.charAt(y,x), scoreX, scoreO, bEndGame);
			if(scoreX == input.boardSize) {
				bWonX = true;
			}
			if(scoreO == input.boardSize) {
				bWonO = true;
			}
		}
	}

	{
		size_t scoreX = 0;
		size_t scoreO = 0;
		for(size_t x=0; x!=input.boardSize; ++x) {
			scoreChar(input.charAt(x,x), scoreX, scoreO, bEndGame);
		}
		if(scoreX == input.boardSize) {
			bWonX = true;
		}
		if(scoreO == input.boardSize) {
			bWonO = true;
		}
	}
	
	{
		size_t scoreX = 0;
		size_t scoreO = 0;
		for(size_t x=0; x!=input.boardSize; ++x) {
			scoreChar(input.charAt(x,input.boardSize-1-x), scoreX, scoreO, bEndGame);
		}
		if(scoreX == input.boardSize) {
			bWonX = true;
		}
		if(scoreO == input.boardSize) {
			bWonO = true;
		}
	}

	if(bWonX) {
		output.result = "X won";
	} else if(bWonO) {
		output.result = "O won";
	} else if(bEndGame) {
		output.result = "Draw";
	} else {
		output.result = "Game has not completed";
	}

	return output;
}


// - main ---------------------------------------------------------------------

int main(int argc, char* argv[])
{
	string inputFileName = "input.in";
	string outputFileName = "output.out";
	if(argc == 2) {
		inputFileName = argv[1];
	}

	// Input
	LOG("parsing: " << inputFileName);
	ifstream inputFile(inputFileName);
	if(!inputFile) {
		LOG("Could not open " << inputFileName);
		return 1;
	}

	Input input;
	inputFile >> input;
	
	// Solve
	Output output;
	Solution solution;
	solution.solve(input,output);
	
	// Output
	LOG("outputting: " << outputFileName);
	ofstream outputFile(outputFileName);
	if(!outputFile) {
		LOG("Could not open " << outputFileName);
		return 1;
	}
	
	outputFile << output;
	cout << output;

	//LOG(output);
	
	LOG("Completed");
	return 0;
}

