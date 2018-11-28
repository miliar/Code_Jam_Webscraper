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
	uint N;
	vector<string> strs;
	// tmp
	
	// result
	vector<double> RPI;
public:
	//--------------------------------------------------------------------//
	//     Get Input
	//--------------------------------------------------------------------//
	void GetInput(istream& in){
		in >> N;
		string str;
		for(uint i=0; i<N; ++i){
			in >> str;
			strs.push_back(str);
		}
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
		vector<double> wp(N), owp(N), oowp(N);
		vector<uint> win(N), lose(N);
		for(uint i=0; i<N; ++i){
			win[i]= 0, lose[i] = 0;
			for(uint j=0; j<N; ++j){
				if(strs[i][j] == '1'){
					++win[i];
				}
				else if(strs[i][j] == '0'){
					++lose[i];
				}
			}
			if(win[i] + lose[i] == 0){
				wp[i] = 0;
			}
			else{
				wp[i] = ((double)win[i])/(win[i] + lose[i]);
			}
		}
		for(uint i=0; i<N; ++i){
			owp[i] = 0;
			uint count = 0;
			for(uint j=0; j<N; ++j){
				if(strs[i][j] != '.'){
					++count;
					uint win = 0, lose = 0;
					for(uint k=0; k<N; ++k){
						if(i != k){
							if(strs[k][j] == '1'){
								++win;
							}
							else if(strs[k][j] == '0'){
								++lose;
							}
						}
					}
					if(win + lose == 0){
						owp[i] = 0;
					}
					else{
						owp[i] += ((double)lose) / (win + lose);
					}
				}
			}
			owp[i] /= count;
		}
		for(uint i=0; i<N; ++i){
			oowp[i] = 0;
			uint count = 0;
			for(uint j=0; j<N; ++j){
				if(strs[i][j] != '.'){
					++count;
					oowp[i] += owp[j];
				}
			}
			oowp[i] /= count;
		}

		RPI.resize(N);
		for(uint i=0; i<N; ++i){
			RPI[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
		}
	}

	//--------------------------------------------------------------------//
	//     Output Result
	//--------------------------------------------------------------------//
	void OutputResult(ostream& out) const{
		out << endl;
		for(uint i=0; i<N; ++i){
			out << RPI[i] << endl;
		}
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