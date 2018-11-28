//============================================================================
// Name        : GCJ_1_A.cpp
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


int main() {
	
	string filename = "A-large";
	string fnIn = filename + ".in";
	string fnOut = filename + ".out2";
	ifstream fin(fnIn.c_str(), ios::in);
	ofstream fout(fnOut.c_str(), ios::out);
	
	vector<long long > v1;
	vector<long long > v2;
	
	long long  T;
	fin >> T;
	RP(t,T){
		long long  N;
		fin >> N;
		long long  num;
		RP(i,N) {
			fin >> num;
			v1.push_back(num);
		}
		RP(i,N){
			fin >> num;
			v2.push_back(num);
		}
		sort(ALL(v1));
		sort(ALL(v2));
		reverse(ALL(v2));
		long long  product = 0;
		RP(i,N) 
			product += v1[i]*v2[i];
		fout << "Case #" <<t+1<< ": " << product << endl;
		v1.clear();
		v2.clear();		
	}
	
	return 0;
}
