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
#define DEFAULT_ANSWER "answer.txt"

//=========================================================================//
//     Problem Class
//=========================================================================//
class Problem{
private:
	// input
	uint H, W, D;
	vector<string> map;
	// tmp
	
	// result
	uint64 result;
public:
	//--------------------------------------------------------------------//
	//     Get Input
	//--------------------------------------------------------------------//
	void GetInput(istream& in){
		in >> H >> W >> D;
		char c;
		for(uint i=0; i<H; ++i){
			map.push_back(string());
			for(uint j=0; j<W; ++j){
				in >> c;
				map[i] += c;
			}
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
	struct Position{
		float x, y;
	};

	void Solve(){
		int w = W-2, h = H-2;
		Position X = {};
		for(uint i=0; i<map.size(); ++i){
			for(uint j=0; j<map[i].size(); ++j){
				if(map[i][j] == 'X'){
					X.y = i - 0.5f;
					X.x = j - 0.5f;
					break;
				}
			}
		}
		
		vector<Position> pos;
		// ç∂
		{
			Position d = {0, 0};
			int mod_x = 0;
			do{
				// è„
				{
					d.y = 0;
					int mod_y = 0;
					do{
						if(d.x != 0 || d.y != 0){
							pos.push_back(d);
						}

						d.y -= ((mod_y++ % 2 == 0)? X.y: (h - X.y)) * 2;
					}while(abs(d.y) <= D);
				}
				// â∫
				{
					int mod_y = 1;
					d.y = 0;
					do{
						if(d.x != 0 || d.y != 0){
							pos.push_back(d);
						}

						d.y += ((mod_y++ % 2 == 0)? X.y: (h - X.y)) * 2;
					}while(abs(d.y) <= D);
				}

				d.x -= ((mod_x++ % 2 == 0)? X.x: (w - X.x)) * 2;
			}while(abs(d.x) <= D);
		}
		// âE
		{
			Position d = {0, 0};
			int mod_x = 1;
			do{
				// è„
				{
					d.y = 0;
					int mod_y = 0;
					do{
						if(d.x != 0 || d.y != 0){
							pos.push_back(d);
						}

						d.y -= ((mod_y++ % 2 == 0)? X.y: (h - X.y)) * 2;
					}while(abs(d.y) <= D);
				}
				// â∫
				{
					int mod_y = 1;
					d.y = 0;
					do{
						if(d.x != 0 || d.y != 0){
							pos.push_back(d);
						}

						d.y += ((mod_y++ % 2 == 0)? X.y: (h - X.y)) * 2;
					}while(abs(d.y) <= D);
				}

				d.x += ((mod_x++ % 2 == 0)? X.x: (w - X.x)) * 2;
			}while(abs(d.x) <= D);
		}

		set<float> angle;
		for(uint i=0; i<pos.size(); ++i){
			Position &p = pos[i];
			float d2 = p.x * p.x + p.y * p.y;
			if(d2 <= D*D){
				float a = atan2(p.x, p.y);
				angle.insert(a);
			}
		}

		result = angle.size();
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
int OpenFiles(const int argc, const char *argv[], ifstream *in_file, fstream *out_file, ifstream *answer_file){
	string input_file_name = (argc > 1)? argv[1]: DEFAULT_INPUT;
	uint index = input_file_name.find_last_of(DIRECTORY_SEPARATOR);
	string dir = (index+1 < input_file_name.size())? input_file_name.substr(0, index+1): "",
		        output_file_name = dir + DEFAULT_OUTPUT;
	string answer_file_name = (argc > 1)? argv[2]: DEFAULT_ANSWER;

	in_file->open(input_file_name.c_str());
	if(!in_file->is_open()){
		cout << "Input File Open Error: [" << input_file_name << "]" << endl;
		return -1;
	}

	out_file->open(output_file_name.c_str(), ios::in | ios::out | ios::trunc);
	if(!out_file->is_open()){
		cout << "Output File Open Error: [" << output_file_name << "]" << endl;
		return -1;
	}

	answer_file->open(answer_file_name.c_str());
	if(!answer_file->is_open()){
	}

	return 0;
}

//=========================================================================//
//     Main
//=========================================================================//
int main(const int argc, const char *argv[]){
	// Get File Name
	ifstream in_file, answer_file;
	fstream out_file;
	if(OpenFiles(argc, argv, &in_file, &out_file, &answer_file) != 0){
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
	char buf[256 * 1024];
	out_file.seekg(0);
	out_file.clear();
	out_file.get(buf, sizeof(buf));
	string result = buf;

	string answer;
	if(answer_file.is_open()){
		answer_file.get(buf, sizeof(buf));
		answer = buf;
	}

	cout << endl;
	cout << "=====[Info]=================" << endl;
	cout << "time: "
	     << setprecision(2) << setiosflags(ios::fixed)
	     << (end - start) << "sec" << endl;
	if(answer.size() > 0){
		cout << ((result == answer)? "Correct": "Incorrect") << endl;
	}
	cout << endl;

	// File Close
	in_file.close();
	out_file.close();

	return 0;
}