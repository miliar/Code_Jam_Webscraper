#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <list>
#include <map>
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
//     Problem Class
//=========================================================================//
class Problem{
private:
	// input
	int C;
	vector<string> c_str;
	int D;
	vector<string> d_str;
	int N;
	string n_str;
	// tmp
	
	// result
	string result;
public:
	//--------------------------------------------------------------------//
	//     Get Input
	//--------------------------------------------------------------------//
	void GetInput(istream& in){
		in >> C;
		string str;
		for(int i=0; i<C; ++i){
			in >> str;
			c_str.push_back(str);
		}
		in >> D;
		for(int i=0; i<D; ++i){
			in >> str;
			d_str.push_back(str);
		}
		in >> N;
		in >> n_str;
	}
	//--------------------------------------------------------------------//
	//     Output for Debug
	//--------------------------------------------------------------------//
	void DebugOutput(ostream& out) const{

	}
	//--------------------------------------------------------------------//
	//     Solve
	//--------------------------------------------------------------------//
	void Solve(){
		result.clear();
		for(uint i=0; i<n_str.size(); ++i){
			char c;
			if(result.size() == 0){
				result.push_back(n_str[i]);
			}
			else if(check(result.back(), n_str[i], &c)){
				result.resize(result.size()-1);
				result += c;
			}
			else if(check(result, n_str[i])){
				result.clear();
			}
			else{
				result.push_back(n_str[i]);
			}
		}
	}

	bool check(char c1, char c2, char *r){
		for(uint i=0; i<c_str.size(); ++i){
			if(
				(c_str[i][0] == c1 && c_str[i][1] == c2) ||
				(c_str[i][0] == c2 && c_str[i][1] == c1)
			){
				*r = c_str[i][2];
				return true;
			}
		}
		return false;
	}

	bool check(string &str, char c2){
		for(uint j=0; j<str.size(); ++j){
			char c1 = str[j];
			for(uint i=0; i<d_str.size(); ++i){
				if(
					(d_str[i][0] == c1 && d_str[i][1] == c2) ||
					(d_str[i][0] == c2 && d_str[i][1] == c1)
				){
					return true;
				}
			}
		}
		return false;
	}

	//--------------------------------------------------------------------//
	//     Output Result
	//--------------------------------------------------------------------//
	void OutputResult(ostream& out) const{
		out << " [";
		for(uint i=0; i<result.size(); ++i){
			out << result[i];
			if(i != result.size()-1){
				out << ", ";
			}
		}
		out << "]" << endl;
	}
};

//=========================================================================//
//     Open Files
//=========================================================================//
int OpenFiles(const int argc, const char *argv[], ifstream *in_file, ofstream *out_file){
	string input_file_name = (argc > 1)? argv[1]: DEFAULT_INPUT;
	uint index = input_file_name.find_last_of(DIRECTORY_SEPARATOR);
	string dir = (index+1 < input_file_name.size())? input_file_name.substr(0, index+1): "",
		        output_file_name = dir + DEFAULT_OUTPUT;

	in_file->open(input_file_name.c_str());
	if(!in_file->is_open()){
		cout << "Input File Open Error: [" << input_file_name << "]" << endl;
		return -1;
	}

	out_file->open(output_file_name.c_str());
	if(!out_file->is_open()){
		cout << "Output File Open Error: [" << output_file_name << "]" << endl;
		return -1;
	}
	return 0;
}

//=========================================================================//
//     Main
//=========================================================================//
int main(const int argc, const char *argv[]){
	// Get File Name
	ifstream in_file;
	ofstream out_file;
	if(OpenFiles(argc, argv, &in_file, &out_file) != 0){
		return -1;
	}

	// Get Start Time
	clock_t start, end;
	start = clock();

	// Get number of problems
	uint number_of_problems;
	in_file >> number_of_problems;
	getline(in_file, string());
	
	cout << "=====[Result]===============" << endl;
	Problem problem;
	for(uint i=0; i<number_of_problems; ++i){
		problem = Problem();
		// Get Input
		problem.GetInput(in_file);
		// Solve
		problem.Solve();
		// Output
		out_file << "Case #" << (i+1) << ":";
		cout << "Case #" << (i+1) << ":";
		problem.OutputResult(cout);
		problem.OutputResult(out_file);
#if CHECK_DATA
		problem.DebugOutput(cout);
#endif
	}

	// Get End Time
	end = clock();

	// Output Result
	cout << endl;
	cout << "=====[Info]=================" << endl;
	cout << "time: "
	     << setprecision(2) << setiosflags(ios::fixed)
	     << (end - start) << "sec" << endl;
	cout << endl;

	// File Close
	in_file.close();
	out_file.close();

	return 0;
}