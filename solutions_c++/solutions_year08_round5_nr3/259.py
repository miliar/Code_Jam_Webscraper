#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <map>
#include <sstream>
#include <queue>

#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>

#define forn(i, n) for(int i=0;i<int(n);i++)
#define FOR(i, a, b) for(int i=(a);i<int(b);i++)
#define RFOR(i, b, a) for(int i=(b);i>int(a);i--)
#define foreach(it, c)  for(__typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define UNIQUE(a) SORT(a),(a).resize(unique(ALL(a))-a.begin())
#define ALL(x)   (x).begin(),(x).end()
#define SIZE(x)   (int)(x).size()
#define SORT(x) sort(ALL(x))
using namespace std;
#define VI vector<int>
#define VS vector<string>
#define PB push_back
#define ISS istringstream
#define OSS ostringstream
typedef long long ll;

int rows, cols;
vector<string> grid;
int dp[11][1<<10];
vector<int> pos;
int back(int row, int mask){
	if( row == rows ) return 0;
	
	int i,j , k;
	int &res = dp[row][mask];if( res >= 0 ) return res;
	res = 0;
	for(k=0;k<pos.size();k++){
		int m = pos[k];
		int vale = 1;
		for(i=0;i<cols&&vale;i++) if( grid[row][i] == 'x' && ((1<<i)&m))vale=0;
		for(i=0;i<cols&&vale;i++){
			if( i && ((1<<i)&m) && ((1<<(i-1))&mask) ) vale = 0;
			if( i!=cols-1 && ((1<<i)&m) && ((1<<(i+1))&mask) ) vale = 0;
		}
		if(!vale ) continue;
		
// 		if( __builtin_popcount(m) ) printf("YESSS\n");
		res = max( res, __builtin_popcount(m) + back(row+1,m) );
	}
	return res;
}
int main(){
	int i, j, k;int casos;
	cin >> casos;
	for(int h = 0 ; h < casos ; h ++ ){
		cin >> rows >> cols;grid.clear();
		for(i=0;i<rows;i++){string s; cin >> s; grid.PB(s);}
		memset(dp, -1, sizeof(dp));
		pos.clear();
		for(i=0;i<(1<<cols);i++){
			int vale = 1;
			for(j=0;j<cols-1;j++)if( (i&(1<<j)) && (i&(1<<(j+1))) ) vale = 0;
			if( vale ) pos.PB(i);
		}
		printf("Case #%i: %i\n", h+1, back(0,0));
	}return 0;
}


































