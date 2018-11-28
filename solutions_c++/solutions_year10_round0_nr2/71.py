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
#define CHECK_DATA TRUE

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
	   800000000000000000001
	   900000000000000000001
	y=  99999999999999999999

	   900000000000000000000
	  1000000000000000000000
	T= 100000000000000000000

	  26000000
	  11000000
	   6000000
	y= 4000000

	  30000000
	  15000000
	  10000000
	T= 5000000

	   91287578
	   36390448
	y= 18506682

	  109794260
	   54897130
    T= 54897130

	   8116574
	   7138432
	   3109700
	y=     514

	   8117088
	   7138432
	   3110214
	T=     514


	0 <= y <= T
	1 <= T <= min(t[i] - t[j])  ※ ただし、i != j && t[i] != t[j]

	((t[0] + y) % T == 0) && ((t[1] + y) % T == 0) && ...
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
	vector<uint64> t;

public:
	// Get
	void Get(istream& in){
		/*
			TODO: 一問分のデータを読み込む
		*/

		uint64 N;
		in >> N;
		uint64 x;
		for(uint i=0; i<N; ++i){
			in >> x;
			if(find(t.begin(), t.end(), x) == t.end()){
				t.push_back(x);
			}
		}
		sort(t.begin(), t.end(), greater<uint64>());
	}

	// Output
	void Output(ostream& out) const{
		/*
			TODO: 一問分のデータを出力する(※読み込みが成功したかどうかの確認用)
		*/
		
		for(uint i=0; i<t.size(); ++i){
			out << t[i] << endl;
		}
	}
};

//=========================================================================//
//     Result Class
//=========================================================================//
class Result{
private:
	uint64 y, T;
public:
	// Solve
	void Solve(const Input &in){
		/*
			TODO: 問題を一問解く
		*/
		uint64 min = UINT_MAX;
		for(uint i=0; i<in.t.size()-1; ++i){
			uint j=i+1;
			uint64 d = in.t[i] - in.t[j];
			if(min > d){
				min = d;
			}
		}

		for(T = min; T > 1; --T){
			bool bad = false;
			y = T - in.t[0] % T;
			for(uint i=1; i<in.t.size(); ++i){
				if(T - in.t[i] % T != y){
					bad = true;
					break;
				}
			}
			if(!bad){
				if(y == T){
					y = 0;
				}
				return;
			}
		}
		y = 0;
		T = 1;
	}
	// Output
	void Output(ostream& out) const{
		/*
			TODO: 一問分の結果を出力する
		*/

		out << " " << y << endl;
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