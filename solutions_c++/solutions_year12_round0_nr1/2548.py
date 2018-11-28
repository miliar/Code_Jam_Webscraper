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
	string input;
	// tmp
	
	// result
	string result;
public:
	//--------------------------------------------------------------------//
	//     Get Input
	//--------------------------------------------------------------------//
	void GetInput(istream& in){
		char buf[1024];
		in.getline(buf, sizeof(buf));
		input = buf;
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
		map<char, char> m;
		m.insert(make_pair(' ', ' '));
		m.insert(make_pair('a', 'y'));
		m.insert(make_pair('b', 'h'));
		m.insert(make_pair('c', 'e'));
		m.insert(make_pair('d', 's'));
		m.insert(make_pair('e', 'o'));
		m.insert(make_pair('f', 'c'));
		m.insert(make_pair('g', 'v'));
		m.insert(make_pair('h', 'x'));
		m.insert(make_pair('i', 'd'));
		m.insert(make_pair('j', 'u'));
		m.insert(make_pair('k', 'i'));
		m.insert(make_pair('l', 'g'));
		m.insert(make_pair('m', 'l'));
		m.insert(make_pair('n', 'b'));
		m.insert(make_pair('o', 'k'));
		m.insert(make_pair('p', 'r'));
		m.insert(make_pair('q', 'z'));
		m.insert(make_pair('r', 't'));
		m.insert(make_pair('s', 'n'));
		m.insert(make_pair('t', 'w'));
		m.insert(make_pair('u', 'j'));
		m.insert(make_pair('v', 'p'));
		m.insert(make_pair('w', 'f'));
		m.insert(make_pair('x', 'm'));
		m.insert(make_pair('y', 'a'));
		m.insert(make_pair('z', 'q'));

		for(uint i=0; i<input.size(); ++i){
			result += m[input[i]];
		}
	}

	//--------------------------------------------------------------------//
	//     Output Result
	//--------------------------------------------------------------------//
	void OutputResult(ostream& out) const{
		out << " " << result << endl;
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