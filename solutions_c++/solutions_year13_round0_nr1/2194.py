#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)

char *states[] = {"X won", "O won", "Draw", "Game has not completed"};

int check(vector<string>& mp, char c){
	int good;
	REP(i,4){
		good=1;
		REP(w,4){
			if((mp[i][w]!= c) && (mp[i][w] != 'T')){
				good = 0;
				break;
			}
		}
		if(good)return 1;
	}
	REP(i,4){
		good=1;
		REP(w,4){
			if((mp[w][i]!= c) && (mp[w][i] != 'T')){
				good = 0;
				break;
			}
		}
		if(good)return 1;
	}

	good = 1;
	REP(i,4){
		if((mp[i][i]!= c) && (mp[i][i] != 'T')){
			good = 0;
			break;
		}
	}
	if(good)return 1;

	good = 1;
	REP(i,4){
		if((mp[3-i][i]!= c) && (mp[3-i][i] != 'T')){
			good = 0;
			break;
		}
	}
	if(good)return 1;
	return 0;
}

int getState(vector<string>& mp){
	if(check(mp,'X'))return 0;
	if(check(mp,'O'))return 1;

	REP(i,4){
		REP(w, 4){
			if(mp[i][w] == '.'){
				return 3;
			}
		}
	}

	return 2;
}

int main(void){
	vector <string> mp;
	int ntest;
	string str;
	int ret;
	mp.resize(4);

	ifstream fin("A-large.in");
	ofstream fout("out.txt");

	fin >> ntest;
	REP(w, ntest){
		REP(i,4) fin >> mp[i];

		fout << "Case #" << w + 1 << ": " << states[getState(mp)] << endl;
	}

	fin.close();
	fout.close();
	return 0;
}