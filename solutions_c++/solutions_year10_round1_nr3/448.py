#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <list>
#include <map>
#include <queue>
#include <ctime>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <climits>

using namespace std;

// typedef
typedef __int64 int64;
typedef unsigned __int64 uint64;
typedef unsigned int uint;

#define TRUE 1
#define FALSE 0

// define
#define OUTPUT_CONSOLE TRUE

#ifdef _DEBUG
#	define CHECK_DATA TRUE
#else
#	define CHECK_DATA FALSE
#endif

#ifdef    WIN32
#	define DIRECTORY_SEPARATOR '\\'
#else
#	define DIRECTORY_SEPARATOR '/'
#endif

#define DEFAULT_INPUT "data.txt"
#define DEFAULT_OUTPUT "result.txt"
#define DEFAULT_LOG "log.txt"

class Result;

/*
	i < jのとき	(i, j)
		j % i == 0
		i % (j - i*k) == 0 (k = j / i)
	なら勝ち

*/

//=========================================================================//
//     Input Class
//=========================================================================//
class Input{
	friend class Result;

private:
	/*
		TODO: 一問分のデータを格納する変数を追加する
	*/
	uint64 A1, A2, B1, B2;

public:
	// Get
	void Get(istream& in){
		/*
			TODO: 一問分のデータを読み込む
		*/

		in >> A1 >> A2 >> B1 >> B2;
	}

	// Output
	void Output(ostream& out) const{
		/*
			TODO: 一問分のデータを出力する(※読み込みが成功したかどうかの確認用)
		*/
		
		out << A1 << " " << A2 << " " << B1 << " " << B2 << endl;
	}
};

//=========================================================================//
//     Result Class
//=========================================================================//
class Result{
private:
	uint64 value;
public:
	// Solve
	void Solve(const Input &in){
		/*
			TODO: 問題を一問解く
		*/
		value = 0;
		for(uint64 A=in.A1; A<=in.A2; ++A){
			for(uint64 B=in.B1; B<=in.B2; ++B){
				if(Check(A, B)){
					++value;
				}
			}
		}
	}

	bool Check(const uint64 i0, const uint64 j0){
		// i < j にする
		uint64 i, j;
		if(i0 < j0){
			i = i0;
			j = j0;
		}
		else{
			i = j0;
			j = i0;
		}

		if(j % i == 0){
			return (j != i);
		}
		else{
			uint64 k = j / i;
			if(k >= 2){
				if(i % (j - i*k) == 0){
					return true;
				}
				else{
					return true;
				}
			}
			else{
				return !Check(i, j-i);
			}
		}
	}

	// Output
	void Output(ostream& out) const{
		/*
			TODO: 一問分の結果を出力する
		*/

		out << " " << value << endl;
	}
};


//=========================================================================//
//     Input & Result Stream
//=========================================================================//
ostream& operator<<(ostream& out, const Result& result){
	result.Output(out);
	return out;
}

istream& operator>>(istream& in, Input &input){
	input.Get(in);
	return in;
}
ostream& operator<<(ostream& out, const Input& input){
	input.Output(out);
	return out;
}

//=========================================================================//
//     Get Input
//=========================================================================//
int GetInput(const string &file_name, vector<Input> *inputs){
	// Open File
	ifstream file(file_name.c_str());
	if(!file.is_open()){
		cout << "Input File Open Error: [" << file_name << "]" << endl;
		return -1;
	}

	// get number
	uint T;
	file >> T;
	getline(file, string());
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
void OutputData(ostream &out, const vector<Input> &inputs){
	out << "=====[Input]================" << endl;
	out << inputs.size() << endl;
	for(uint i=0; i<inputs.size(); ++i){
		out << "-----[" << (i+1) << "]-----------------" << endl;
		out << inputs[i];
	}
	out << endl;
}

//=========================================================================//
//     Output Result
//=========================================================================//
void OutputResult(ostream &out, const vector<Result> &results){
	for(uint i=0; i<results.size(); ++i){
		out << "Case #" << (i+1) << ":" << results[i];
	}
}

int OutputResult(const string &output_file_name, ostream &log, const vector<Result> &results, double time){
	ofstream file(output_file_name.c_str());
	if(!file.is_open()){
		cout << "Output File Open Error: [" << output_file_name << "]" << endl;
		return -1;
	}

	OutputResult(file, results);
	file.close();

	stringstream str;
	str << "=====[Result]===============" << endl;
	OutputResult(str, results);
	str << endl;

	str << "=====[Info]=================" << endl
		<< "time: "
		<< setprecision(2) << setiosflags(ios::fixed)
	    << time << "sec" << endl
		<< endl;
	log << str.str();

#if OUTPUT_CONSOLE
	cout << str.str();
#endif
	return 0;
}


//=========================================================================//
//     Solve
//=========================================================================//
clock_t Solve(const vector<Input> &inputs, vector<Result> *result){
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
	string input_file_name = (argc > 1)? argv[1]: DEFAULT_INPUT;
	uint index = input_file_name.find_last_of(DIRECTORY_SEPARATOR);
	string dir = (index+1 < input_file_name.size())? input_file_name.substr(0, index+1): "",
				log_file_name = dir + DEFAULT_LOG,
		        output_file_name = dir + DEFAULT_OUTPUT;
	// Open Log Stream
	ofstream log(log_file_name.c_str());
	if(!log.is_open()){
		cout << "Log File Open Error: [" << log_file_name << "]" << endl;
		return -1;
	}

	// Get Input
	vector<Input> inputs;
	if(GetInput(input_file_name, &inputs) != 0){
		return -1;
	}

	// check data
#if CHECK_DATA
	OutputData(log, inputs);
#if OUTPUT_CONSOLE
	OutputData(cout, inputs);
#endif
#endif

	// Solve
	vector<Result> results;
	uint time = Solve(inputs, &results);

	// Output Result
	if(OutputResult(output_file_name, log, results, (time / static_cast<double>(CLOCKS_PER_SEC))) != 0){
		return -1;
	}

	return 0;
}