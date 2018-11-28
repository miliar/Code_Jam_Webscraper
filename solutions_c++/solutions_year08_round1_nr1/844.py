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

	ifstream inf("B-small.in");
	ofstream outf("B-small.out");

	
	
	int NumberOfCase = 0;
	inf >> NumberOfCase;
	REP(i_noc, NumberOfCase){
		int result=0;
		vector<int> v1;
		vector<int> v2;
		int count;


		inf >> count;
		REP(j, count){
			int tmp;
			inf >> tmp;
			v1.push_back(tmp);
		}
		REP(j, count){
			int tmp;
			inf >> tmp;
			v2.push_back(tmp * -1);
		}
		sort(ALL(v1));
		sort(ALL(v2));
		REP(j, count){
			result += (v1[j] * v2[j] * -1);
		}
		outf << "Case #" << i_noc +1 << ": " << result << endl;
	}

	outf.close();
	inf.close();
	return 0;
}