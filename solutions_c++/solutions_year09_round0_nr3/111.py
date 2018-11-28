#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>

#define REP(i, T) for(int (i)=0; (i) < T; (i) ++)
#define FOR(i, L, R) for(int (i)=L; (i) < R; (i) ++)
#define PB push_back
#define ALL(v) v.begin(), v.end()
#define SZ(v) (int)v.size()

#define vi vector<int>
#define vs vector<string>
#define ui unsigned int
#define ll long long

using namespace std;

string w = "welcome to code jam";
string s;

int dp[600][50];

int go(int i, int j) {
	if(j==w.size()) return 1;
	if(i==s.size()) return 0;
	if(dp[i][j] < 0) {
		int aux=0;
		if(s[i]==w[j]) aux += go(i+1, j+1);
		aux += go(i+1, j);
		dp[i][j] = aux%10000;
	}
	return dp[i][j];
}

int main()
{
	int T, i,j, k;
	scanf("%d", &T);
	getchar();
	for(int caso=1; caso<=T; caso++) {
		s="";
		char c;
		while(1) {
			c = getchar();
			if(c=='\n') break;
			s += c;
		}
		
		memset(dp, -1, sizeof(dp));
		
		printf("Case #%d: %.4d\n", caso, go(0,0));
	}
	return 0;
}
