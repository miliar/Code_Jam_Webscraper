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

bool myComp(const int& lhs, const int& rhs){
	if (abs(lhs) == abs(rhs))
		return lhs < rhs;
	else 
		return abs(lhs) < abs(rhs);
}

int main() {
	
	ifstream fin("B-small-attempt0.in", ios::in);
	ofstream fout("B-samll.out", ios::out);

	int N; fin >> N;
	
	vector<int> a2b;
	vector<int> b2a;
	
	RP(i,N){
		int t;
		int ab, ba;
		fin >> t >> ab >> ba;
		RP(j,ab){
			int from1, from2;
			fin >> from1; fin.get(); fin>> from2;
			int from = from1*60+from2;
			a2b.PB(from);
			
			int to1, to2;
			fin >> to1; fin.get(); fin >> to2;
			int to = to1*60+to2;
			b2a.PB((to+t)*-1);			
		}
		RP(j,ba){
			int from1, from2;
			fin >> from1; fin.get(); fin>> from2;
			int from = from1*60+from2;
			b2a.PB(from);
			
			int to1, to2;
			fin >> to1; fin.get(); fin >> to2;
			int to = to1*60+to2;
			a2b.PB((to+t)*-1);			
		}
		
		sort(ALL(a2b), myComp);
		sort(ALL(b2a), myComp);
		
		/*RP(j,SZ(a2b))
			cerr << a2b[j] << " ";
		cerr << endl;
		
		RP(j,SZ(b2a))
			cerr << b2a[j] << " ";
		cerr << endl;*/
		
		int countA = 0;
		int maxA = 0;
		RP(j,SZ(a2b)){
			if (a2b[j]>0) countA++;
			else countA--;
			maxA = max(countA, maxA);
		}
		
		int countB = 0;
		int maxB = 0;
		RP(j,SZ(b2a)){
			if (b2a[j]>0) countB++;
			else countB--;	
			maxB = max(countB, maxB);
		}
		fout <<"Case #" << i+1 << ": " << maxA << ' ' << maxB << endl;
		a2b.clear();
		b2a.clear();
	}	

	
	return 0;
}
