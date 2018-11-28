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
	int64 L, t, N, C;
	vector<int64> a;
	// tmp
	
	// result
	int64 result;
public:
	//--------------------------------------------------------------------//
	//     Get Input
	//--------------------------------------------------------------------//
	void GetInput(istream& in){
		in >> L >> t >> N >> C;
		int64 t;
		for(int64 i=0; i<C; ++i){
			in >> t;
			a.push_back(t);
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
		if(L == 0){
			int64 time = 0;
			for(uint i=0; i<N; ++i){
				// boost‚È‚µ
				time += a[i % a.size()] * 2;
			}
			result = time;
		}
		else{
			// boost‚·‚é‚Æ‚±
			bool use1 = true;
			int64 index1 = -1, index2 = -1;
			vector<int64> boost;
			{
				int64 time = 0;
				vector<pair<int64, int64> > list;
				for(uint i=0; i<N; ++i){
					int64 ai = a[i%a.size()];
					time += ai * 2;
					if(time >= t){
						if(list.size() == 0){
							if(time == t){
								use1 = false;
							}
							else{
								use1 = true;
							}
						}
						list.push_back(make_pair(ai, i));
					}
				}
				if(list.size() > 0){
					index1 = list[0].second;
				}
				else{
					int64 time = 0;
					for(uint i=0; i<N; ++i){
						// boost‚È‚µ
						time += a[i % a.size()] * 2;
					}
					result = time;
					return;
				}
				list.erase(list.begin(), list.begin()+1);
				sort(list.begin(), list.end(), greater<pair<int64, int64> >());
				list.resize(min((uint)L, list.size()));
		
				if(list.size() > 0){
					for(uint i=list.size(); i>0; --i){
						boost.push_back(list[i-1].second);
					}
					index2 = boost[0];
					boost.erase(boost.begin(), boost.begin()+1);
				}
				else{
					index2 = index1;
				}
			}

			// ŒvŽZ
			{
				int64 time = 0, index1_time = 0;
				for(uint i=0; i<N; ++i){
					if(index1 == i){
						int64 s = time + a[i % a.size()]*2 - t;
						index1_time = (a[i % a.size()]*2 - s) + s/2;
					}
					else if(index2 == i){
					}
					else{
						if(find(boost.begin(), boost.end(), i) == boost.end()){
							// boost‚È‚µ
							time += a[i % a.size()] * 2;
						}
						else{
							// boost‚ ‚è
							time += a[i % a.size()];
						}
					}
				}
				int64 time1 = time, time2 = time;
				time1 += index1_time + ((index1 != index2)? a[index2 % a.size()]*2: 0);
				time2 += (index1 != index2)? (a[index2 % a.size()] + a[index1 % a.size()] * 2): (a[index1 % a.size()] * 2);

				result = min(time1, time2);
			}
		}
	}

	/*
	19 * 2 + 5 = 43
		[2ŒÂ 20hour] [3, 5,| 3, 5, 3, [5], 3, [5]]
		(3 + 5 + 3 + 5 + 3 + 3) * 2 + (5 + 5) = 22 * 2 + 10 = 54

		[|3 3 3 3]
		18 + 3

		¦‘Ò‚Â•K—v‚Í‚È‚¢
		

		[1ŒÂ 4hour] [10, 4]

	*/

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