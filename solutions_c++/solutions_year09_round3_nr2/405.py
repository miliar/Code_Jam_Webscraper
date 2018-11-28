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
	struct Data{
		int x, y, z, vx, vy, vz;
	};
	vector<Data> data;
	// result
	long double min_d, min_t;
public:
	//--------------------------------------------------------------------//
	//     Get Input
	//--------------------------------------------------------------------//
	void GetInput(istream& in){
		in >> N;
		data.resize(N);
		for(uint i=0; i<N; ++i){
			in >> data[i].x >> data[i].y >> data[i].z >> data[i].vx >> data[i].vy >> data[i].vz;
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
		long double sx, sy, sz, svx, svy, svz;
		sx = sy = sz = svx = svy = svz = 0;
		for(uint i=0; i<N; ++i){
			sx += data[i].x;
			svx += data[i].vx;
			sy += data[i].y;
			svy += data[i].vy;
			sz += data[i].z;
			svz += data[i].vz;
		}

		long double cx, cy, cz, cvx, cvy, cvz;
		cx = sx / N; cvx = svx / N;
		cy = sy / N; cvy = svy / N;
		cz = sz / N; cvz = svz / N;

		if(cvx == 0 && cvy == 0 && cvz == 0){
			min_d = sqrt(pow(cx,2) + pow(cy,2) + pow(cz,2));
			min_t = 0;
			return;
		}

		min_d = (
					(pow(cy,2)+pow(cx,2))*pow(cvz,2) + 
					(pow(cz,2)+pow(cx,2))*pow(cvy,2) + 
					(pow(cz,2)+pow(cy,2))*pow(cvx,2) + 2*(-cy*cvy-cx*cvx)*(cz*cvz) - 2*cx*cy*cvx*cvy
				);
		if(min_d < 0){
			min_d = 0;
		}
		else{
			min_d /= (pow(cvx, 2) + pow(cvy, 2) + pow(cvz, 2));
		}
		min_d = sqrt(min_d);
		long double a = pow(cvx,2) + pow(cvy,2) + pow(cvz,2),
					b = 2*(cx*cvx + cy*cvy + cz*cvz),
					c = pow(cx,2) + pow(cy,2) + pow(cz,2) - pow(min_d,2);
		min_t = sqrt(c/a); //(-b + sqrt(pow(b,2)-4*a*c))/ (2*a);
		long double test = sqrt(pow(cx+min_t*cvx,2) + pow(cy+min_t*cvy,2) + pow(cz+min_t*cvz,2));
		if(abs(test - min_d) >= 0.00001){
			//min_t = -min_t;
			//test = sqrt(pow(cx+min_t*cvx,2) + pow(cy+min_t*cvy,2) + pow(cz+min_t*cvz,2));
			//if(abs(test - min_d) >= 0.00001){
				min_d = sqrt(pow(cx,2) + pow(cy,2) + pow(cz,2));
				min_t = 0;
			//}
		}
	}
	//--------------------------------------------------------------------//
	//     Output Result
	//--------------------------------------------------------------------//
	void OutputResult(ostream& out) const{
		out << " " << setprecision(9) << setiosflags(ios::fixed) << min_d
			<< " " << setprecision(9) << setiosflags(ios::fixed) << min_t << endl;
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