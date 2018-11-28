#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <queue>
#include <utility>
#include <string>
#include <stdio.h>

using namespace std;

#define ALL(container) (container).begin(),(container).end()
#define REP(i,N) for (int i=0; i<(N); ++i)
#define FOR(i,i_begin,i_end) for (int i=(i_begin); i<=(i_end); ++i)
#define FORD(i,i_begin,i_end) for (int i=(i_begin); i>=(i_end); --i)
#define FOREACH(it, container) for(__typeof((container).begin()) it = (container).begin(); it != (container).end(); ++it)
#define clearStream(_stream_, _str_) getline((_stream_),(_str_))

/*
clearStream(inf, clear_str);
string inputLine; getline(inf, inputLine);
istringstream iss(inputLine);
*/
int main(){

	ifstream inf("A-small.in");
	ofstream outf("A-small.out");
	
	
	int NumberOfCase = 0;
	inf >> NumberOfCase;
	
	REP(i_noc, NumberOfCase){
		int P, K, L;
		vector<int> hm;
		vector<int> key[1000];
		int result = 0;
		//bool rfail = false;
		inf >> P >> K >> L;

		REP(j, L){
			int inputNum;
			inf >> inputNum;
			hm.push_back(inputNum);
		}
		sort(ALL(hm));

		int i=0;
		for(int j= hm.size()-1; j>=0; j--){
			key[i].push_back(hm[j]);
			if(key[i].size() > P){
				//rfail = true;
				break;
			}
			i++;
			i = i % K;
		}
		
		//if(rfail){
		//	outf << "Case #" << i_noc + 1 << " : 
		//}
		//else{
			REP(j, K){
				REP(q, key[j].size()){
					result += (key[j][q] * (q+1));
				}
			}
			outf << "Case #" << i_noc +1 << ": " << result << endl;
		//}
		
		
	}

	outf.close();
	inf.close();
	return 0;
}