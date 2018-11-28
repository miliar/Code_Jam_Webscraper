// gcj2r.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
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
#include <cmath>
using namespace std;

// 현재의 template
#define sz(v) ((int)(v).size())
#define F(i,a,b) for(int i=(a);i<(b);++i)
#define FSZ(i,a,v) F(i,a,sz(v))
#define all(v) v.begin(),v.end()
string itoa(int i) { stringstream ss; ss<<i; return ss.str(); }
#define same(a,b) (fabs((a)-(b))<0.0000001)
inline int loop(int size, int now, int add) { return (now+add)%size; }
#define two(N) (1<<(N))
#define contain(S,N) (((S)&two(N))!=0)
#define subset(S,X) (((S)&(X))==(X))
// 해당 위치에 비트의 값 체크 (0인지, 1인지)
#define bitpos(X,P) ((X&(1<<(P)))&&(1<<(P)))
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
#define bound(i,j,isize,jsize) (0<=(i)&&(i)<(isize)&&0<=(j)&&(j)<(jsize))

const long double PI = acos(0.0)*2;

void test() {
	int size(0);
	char sz[1024];
	cin >> size;
	cin.getline(sz, 1024);
	for(int z=0; z<size; ++z) {
		int v;
		cin >> v;
		cin.getline(sz, 1024);
		cerr << "Case #" << z+1 << ": " << v << endl;
		cout << "Case #" << z+1 << ": " << v << endl;
	}
}

// return changed or -1
int in_size;
int out_size;
int in_node[10004][2];
int out_node[10004];
int dp[10004][2];

int go(int pos, int need) {
	if(pos>=out_size) {
		if(need == out_node[pos]) return 0;
		else return -1;
	}
//	if(dp[pos][need]!=-2) return dp[pos][need];
	int r1, r2, minr(INT_MAX), minr2(INT_MAX);
	if(in_node[pos][0]==0 || in_node[pos][1]==1) {	// or
		if(need==0) {
			r1 = go(pos*2, 0);
			r2 = go(pos*2+1, 0);
			if(r1>=0 && r2>=0) minr = min(minr, r1+r2);
		} else {
			r1 = go(pos*2, 1);
			r2 = go(pos*2+1, 0);
			if(r1>=0 && r2>=0) minr = min(minr, r1+r2);
			r1 = go(pos*2, 0);
			r2 = go(pos*2+1, 1);
			if(r1>=0 && r2>=0) minr = min(minr, r1+r2);
			r1 = go(pos*2, 1);
			r2 = go(pos*2+1, 1);
			if(r1>=0 && r2>=0) minr = min(minr, r1+r2);
		}
		if(minr!=INT_MAX && in_node[pos][0]==1) minr += 1;
	}
	minr2 = INT_MAX;
	if(in_node[pos][0]==1 || in_node[pos][1]==1) {	// and
		if(need==0) {
			r1 = go(pos*2, 0);
			r2 = go(pos*2+1, 0);
			if(r1>=0 && r2>=0) minr2 = min(minr2, r1+r2);
			r1 = go(pos*2, 0);
			r2 = go(pos*2+1, 1);
			if(r1>=0 && r2>=0) minr2 = min(minr2, r1+r2);
			r1 = go(pos*2, 1);
			r2 = go(pos*2+1, 0);
			if(r1>=0 && r2>=0) minr2 = min(minr2, r1+r2);
		} else {
			r1 = go(pos*2, 1);
			r2 = go(pos*2+1, 1);
			if(r1>=0 && r2>=0) minr2 = min(minr2, r1+r2);
		}
		if(minr2!=INT_MAX && in_node[pos][0]==0) minr2 += 1;
	}
	int rr = min(minr, minr2);
	if(rr == INT_MAX) return dp[pos][need] = -1;
	else return dp[pos][need] = rr;
}

void btree() {
	int size(0);
	cin >> size;
	for(int z=0; z<size; ++z) {
		int M, V;
		cin >> M >> V;
		memset(in_node, 0, sizeof(in_node));
		memset(out_node, 0, sizeof(out_node));
		for(int i=0; i<10004; ++i) for(int j=0; j<2; ++j) dp[i][j] = -2;
		in_size = (M-1)/2;
		for(int i=1; i<=(M-1)/2; ++i) {
			cin >> in_node[i][0] >> in_node[i][1];
		}
		out_size = (M+1)/2;
		for(int i=(M+1)/2; i<=M; ++i) {
			cin >> out_node[i];
		}
		long long rr = go(1, V);
		cerr << "Case #" << z+1 << ": ";
		if(rr == -1) cerr << "IMPOSSIBLE" << endl;
		else cerr << rr << endl;
		cout << "Case #" << z+1 << ": ";
		if(rr == -1) cout << "IMPOSSIBLE" << endl;
		else cout << rr << endl; 
	}
}

int main(int argc, char* argv[])
{
	btree();
	return 0;
}

