#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <ctime>
#include <algorithm>

// typedef
typedef unsigned int uint;

// define
#ifdef _DEBUG
#	define CHECK_DATA 1
#else
#	define CHECK_DATA 0
#endif

#ifdef    WIN32
#	define DIRECTORY_SEPARATOR '\\'
#else
#	define DIRECTORY_SEPARATOR '/'
#endif

#define DEFAULT_INPUT "test.txt"
#define DEFAULT_OUTPUT "result.txt"

//=========================================================================//
//     Input Class
//=========================================================================//
class Input{
public:
	std::vector<int> data;
public:
	// for Stream
	friend std::istream& operator>>(std::istream& in, Input &input){
		std::string line;
		std::getline(in, line);
		std::istringstream str(line);
		int i=0;
		while(!str.eof()){
			input.data.push_back(0);
			str >> input.data[i++];
		}

		return in;
	}
	// for Stream
	friend std::ostream& operator<<(std::ostream& out, const Input& input){
		using std::endl;

		for(uint i=0; i<input.data.size(); ++i){
			out << input.data[i] << " ";
		}
		out << endl;
		return out;
	}
};

//=========================================================================//
//     Result Class
//=========================================================================//
class Result{
private:
	__int64 value_;
	static std::vector<std::vector<uint> > cache_;
public:
	// Solve
	void Solve(const Input &input){
		for(uint i=2; ; ++i){
			bool ok = true;
			for(uint j=0; j<input.data.size(); ++j){
				if(!IsHappy(i, input.data[j])){
					ok = false;
					break;
				}
			}
			if(ok){
				value_ = i;
				break;
			}
		}
	}
	bool IsHappy(const uint i, const uint j){
		std::vector<uint> numbers;
		uint happy = 0, prev, t = i;

		std::vector<uint> values;
		while(happy != 1){
			if(cache_.size() > t && cache_[t].size() > j && cache_[t][j] != 0){
				if(cache_[t][j] == 1){
					happy = 1;
				}
				else{
					happy = 0;
				}
				break;
			}

			if(std::find(values.begin(), values.end(), t) == values.end()){
				values.push_back(t);
			}
			else{
				happy = 0;
				break;
			}

			prev = t;
			numbers.clear();
			for(; t!=0; t/=j){
				numbers.push_back(t % j);
			}
			happy = 0;
			for(uint k=0; k<numbers.size(); ++k){
				happy += numbers[k] * numbers[k];
			}
			
			t = happy;
		}
		for(uint k=0; k<values.size(); ++k){
			if(cache_.size() <= values[k]){
				cache_.resize(values[k]+1);
			}
			if(cache_[values[k]].size() <= j){
				cache_[values[k]].resize(j+1);
			}
			cache_[values[k]][j] = happy;
		}
		return (happy == 1);
	}
	// for Stream
	friend std::ostream& operator<<(std::ostream& out, const Result& result){
		using std::endl;

		out << " " << result.value_ << endl;

		return out;
	}
};

std::vector<std::vector<uint> > Result::cache_;

//=========================================================================//
//     Get Input
//=========================================================================//
int GetInput(const std::string &file_name, std::vector<Input> *inputs){
	// Open File
	std::ifstream file(file_name.c_str());
	if(!file.is_open()){
		std::cout << "Input File Open Error: [" << file_name << "]" << std::endl;
		return -1;
	}

	// get number
	uint T;
	file >> T;
	std::getline(file, std::string());
	// get data
	inputs->resize(T);
	for(uint i=0; i<T; ++i){
		file >> (*inputs)[i];
	}

	// close
	file.close();
	return 0;
}


//=========================================================================//
//     Output Data (for debug)
//=========================================================================//
void OutputData(std::ostream &out, const std::vector<Input> &inputs){
	using std::endl;

	out << "=====[Input]================" << endl;
	out << inputs.size() << endl;
	for(uint i=0; i<inputs.size(); ++i){
		out << inputs[i];
	}
	out << endl;
}

//=========================================================================//
//     Output Result
//=========================================================================//
void OutputResult(std::ostream &out, const std::vector<Result> &results){
	for(uint i=0; i<results.size(); ++i){
		out << "Case #" << (i+1) << ":" << results[i];
	}
}

int OutputResult(const std::string &file_name, const std::vector<Result> &results, double time){
	using std::cout;
	using std::endl;

	std::ofstream file(file_name.c_str());
	if(!file.is_open()){
		cout << "Output File Open Error: [" << file_name << "]" << endl;
		return -1;
	}

	cout << "=====[Result]===============" << endl;
	OutputResult(cout, results);
	OutputResult(file, results);
	cout << endl;

	file.close();

	cout << "=====[Info]=================" << endl;
	cout << "time: "
	     << std::setprecision(2) << std::setiosflags(std::ios::fixed)
	     << time << "sec" << endl;
	cout << endl;
	return 0;
}


//=========================================================================//
//     Solve
//=========================================================================//
clock_t Solve(const std::vector<Input> &inputs, std::vector<Result> *result){
	clock_t start, end;
	start = clock();

	result->resize(inputs.size());
	for(uint i=0; i<inputs.size(); ++i){
		(*result)[i].Solve(inputs[i]);
	}

	end = clock();
	return end - start;
}

//=========================================================================//
//     Main
//=========================================================================//
int main(int argc, char *argv[]){
	// Get File Name
	std::string input_file_name = (argc > 1)? argv[1]: DEFAULT_INPUT;
	uint index = input_file_name.find_last_of(DIRECTORY_SEPARATOR);
	std::string dir = (index+1 < input_file_name.size())? input_file_name.substr(0, index+1): "",
		        output_file_name = dir + DEFAULT_OUTPUT;

	// Get Input
	std::vector<Input> inputs;
	if(GetInput(input_file_name, &inputs) != 0){
		return -1;
	}

	// check data
#if CHECK_DATA
	OutputData(std::cout, inputs);
#endif

	// Solve
	std::vector<Result> results;
	uint time = Solve(inputs, &results);

	// Output Result
	if(OutputResult(output_file_name, results, (time / static_cast<double>(CLOCKS_PER_SEC))) != 0){
		return -1;
	}

	return 0;
}