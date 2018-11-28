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

int   isPrime(int   x)   
  {   
  int   i;   
  if(x   <   2)   return   0;   
  for(i   =   2;   i   <=   sqrt(x);   i++)   
  if(x   %   i   ==   0)   return   0;   
  return   1;   
  }

struct iUnionFind{
	iUnionFind(int size){pre = new int[size]; RP(i,size) pre[i] = -1;}
	~iUnionFind(void){delete[] pre;}
	void set(int a, int b){int aTop = getTop(a); int bTop = getTop(b); if(aTop != bTop) pre[aTop] = bTop;}
	bool check(int a, int b){return getTop(a)==getTop(b);}
	int getTop(int a){if (pre[a] == -1) return a; else return pre[a] = getTop(pre[a]);}	
private:
	int* pre;
};

int main() {
	
	string filename = "B-small-attempt0";
	string fnIn = filename + ".in";
	string fnOut = filename + ".out";
	ifstream fin(fnIn.c_str(), ios::in);
	ofstream fout(fnOut.c_str(), ios::out);
	int Case;
	fin >> Case;
	set<int> sets;
	RP(_case,Case){
		sets.clear();
		int A, B, P;
		fin >> A >> B >> P;
		iUnionFind iuf(B+1);
		RP2(a,A,B+1) RP2(b,A,a)
		for(int i=b; i>=P; i--){
			if (b%i == 0 && isPrime(i) && a%i == 0)
				iuf.set(a,b);
		}
		
		RP2(i,A,B+1) sets.insert(iuf.getTop(i));
		
		fout << "Case #" << _case+1 << ": " << sets.size() << endl;	
	}
	return 0;
}
