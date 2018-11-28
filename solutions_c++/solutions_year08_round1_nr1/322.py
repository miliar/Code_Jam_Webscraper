#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cctype>
#include <stack>
#include <queue>
#include <sstream>

using namespace std;

#define REP(i, T) for(int (i)=0; (i) < T; (i) ++)
#define FOR(i, L, R) for(int (i)=L; (i) < R; (i) ++)
#define PB push_back
#define ERS(v, i) (v).erase((v).begin()+(i))
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define SZ(v) (int)v.size()

#define vi vector<int>
#define vs vector<string>
#define ll long long
#define pi pair<int, int>

vi v, u;
int n;

int mark[1<<8][1<<8];
int mem[1<<8][1<<8];

int go(int m1, int m2) {
	if(m1 == (1<<n)-1) return 0;
	if(mark[m1][m2]) return mem[m1][m2];
	mark[m1][m2] = 1;
	int id = 0;
	while(m1 & (1<<id)) id++;
	mem[m1][m2] = 1000000000;
	
	for(int i=0; i<n; i++) {
		if(!(m2&(1<<i))) mem[m1][m2] = min(mem[m1][m2], v[id]*u[i] + go(m1|(1<<id), m2|(1<<i)));
	}
	
	return mem[m1][m2];
}

int main(void)
{
	int i, j, k;
	
	int t;
	
	scanf("%d", &t);
	for(k=1; k<=t; k++) {
		scanf("%d", &n);
		v.clear(), u.clear();
		for(i=0; i<n; i++) {
			scanf("%d", &j);
			v.PB(j);
		}
		for(i=0; i<n; i++) {
			scanf("%d", &j);
			u.PB(j);
		}
		SORT(v); SORT(u);
		memset(mark, 0, sizeof(mark));
		
		printf("Case #%d: %d\n", k, go(0, 0));
	}
	
	return 0;
}
