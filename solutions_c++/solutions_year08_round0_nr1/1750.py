//============================================================================
// Name        : GCJ_Q_1.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <vector>
#include <list>
#include <map>
#include <multimap.h>
#include <set>
#include <multiset.h>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <fstream>

using namespace std;

#define INF 1000000000

#define ALL(x) (x).begin(),(x).end()
#define SZ(x) int((x).size())
#define PB(x) push_back((x))
#define PW(a,b) int(pow(double(a), double(b)))
#define FILL(a,b) memset(a,b,sizeof(a))
#define RP2(i,m,n) for(int i=int(m);i<int(n);i++) 
#define RP(i,n) RP2(i,0,n)

#define PRT2(mat) RP(_i,sizeof(mat)/sizeof(mat[0])){RP(_j,sizeof(mat[0])/sizeof(mat[0][0]))cerr<<mat[_i][_j]<<'\t';cerr<<endl;}
#define PRT(mat) RP(_i,sizeof(mat)/sizeof(mat[0]))cerr<<mat[_i]<<'\t';cerr<<endl;

inline int s2i(string s){stringstream ss(s);int n;ss>>n;return n;}
inline string i2s(int n){stringstream ss;ss<<n;return ss.str();}

using namespace std;

int main() {
	
	ifstream ifs("A-large.in", ios::in);
	ofstream ofs("A-large.out", ios::out);
	set<string> searchEngs;
	
	int N;
	ifs >> N;
	RP(i,N){
		int S;
		ifs >> S;
		string line;
		getline(ifs,line);
		RP(j,S) getline(ifs,line);
		int Q;
		ifs >> Q;
		getline(ifs,line);
		searchEngs.clear();
		int sw = 0;
		RP(j,Q){
			getline(ifs,line);
			searchEngs.insert(line);
			if (SZ(searchEngs)==S){
				sw++;
				searchEngs.clear();
				searchEngs.insert(line);
			}
		}	
		ofs <<"Case #" << i+1 << ": " << sw << endl;
	}
	
	return 0;
}
