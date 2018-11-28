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
	uint64 N, PD, PG;
	vector<string> array;
	// tmp
	
	// result
	bool result;
public:
	//--------------------------------------------------------------------//
	//     Get Input
	//--------------------------------------------------------------------//
	void GetInput(istream& in){
		in >> N >> PD >> PG;
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
		
		uint64 stepG = 100, stepD = 100, stepWinD = PD, stepWinG = PG;
		bool change;
		do{
			change = false;
			for(uint64 i=2; i<=100; ++i){
				if(stepG % i == 0 && stepWinG % i == 0){
					stepG /= i;
					stepWinG /= i;
					change = true;
				}
				if(stepD % i == 0 && stepWinD % i == 0){
					stepD /= i;
					stepWinD /= i;
					change = true;
				}
			}
		}while(change);
		if((stepD > N) || (stepWinG == 0 && stepWinD > 0) || ((stepD - stepWinD) > 0 && (stepG - stepWinG) == 0)){
			result = false;
			return;
		}
		else{
			result = true;
			return;
		}

		uint64 G = 0, WinG = 0, D = 0, WinD = 0, LoseD, LoseG;
		// D�𑝂₷
		while(D <= N){
			D += stepD;
			WinD += stepWinD;
			LoseD = D - WinD;
		}
		// G�𑝂₷
		do{
			G += stepG;
			WinG += stepWinG;
			LoseG = G - WinG;
		}while(!(D <= G && WinD <= WinG && LoseD <= LoseG));

		if(
			!((PD * D) == WinD * 100) ||
			!((PG * G) == WinG * 100)
			)
		{
			return;
		}

		result = true;
	}
	/*
		80% 4/5 G += 5, WinG += 4
		50% 1/2 D += 2, WinD += 1

		100% 10/10
		 10%  1/10
		
		PD * D = WinD
		PG * G = WinG
		D <= N
		D <= G
		WinD <= WinG
	*/

	//--------------------------------------------------------------------//
	//     Output Result
	//--------------------------------------------------------------------//
	void OutputResult(ostream& out) const{
		out << " " << ((result)? "Possible": "Broken") << endl;
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