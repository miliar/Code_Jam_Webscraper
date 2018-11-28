#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <regex.h>
using namespace std;

int main (int argc, char * const argv[]) {
	
    // HANDLE COMMAND-LINE ARGUMENTS
	//freopen("example.in", "rt", stdin);
	
	freopen(argv[1], "rt", stdin);
	if(argc == 3){
		freopen(argv[2], "wt", stdout);
	}
	else if(argc==2){
		string out = argv[1];
		out = out.substr(0, out.size() - 2);
		out += "out";
		cout << "Result file: " << out << endl;
		freopen(out.c_str(), "wt", stdout);
	}
	else {
		cout << "Input file required!\nUsage: ./" << argv[0] << " example.in [example.out]" << endl;
		return 0;	
	}
	

	int T = 0;
	cin >> T;
	
	for (int i=0; i<T; ++i) {
		int N, S, P;
		cin >> N >> S >> P;
		
		int totals[N];
		for (int j=0; j<N; ++j) {
			cin >> totals[j];
		}
		
		int answer = 0;

		for (int k=0; k<N; ++k) {
			if (totals[k]/3 >= P) { // avg score higher than P
				++answer;
			}
			else if (totals[k]) {
				// all cases below are less than P
				if (totals[k] % 3 == 0) {
					// score, score, score
					// nothing
					
					// score-1, score, score+1 (*)
					// 5,6,7=18
					// 6,7,8=21
					// 7,8,9=24
					if (S > 0 && totals[k]/3 + 1 == P) {
						++answer;
						--S;
					}
				}
				else if (totals[k] % 3 == 1){
					// score, score, score+1
					// 6,6,7=19
					// 7,7,8=22
					// 8,8,9=25
					if (totals[k]/3 + 1 == P) {
						++answer;
					}
					
					// score-1, score+1, score+1 (*)
					// 3,5,5=13
					// 5,7,7=19
					// 7,9,9=25
				}
				else if (totals[k] % 3 == 2){
					// score-1, score, score
					// 3,4,4=11
					// 4,5,5=14
					if (totals[k]/3 + 1 == P) {
						++answer;
					}
					
					// score-1, score-1, score+1 (*)
					// 2,2,4=8
					// 6,6,8=20
					// 8,8,10=26
					if (S > 0 && totals[k]/3 + 2 == P) {
						++answer;
						--S;
					}
				}
			}
				
		}
		
		cout << "Case #" << i+1 << ": " << answer << endl;
	}
	
	
	
	return 0;
}

























