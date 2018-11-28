#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <cstring>
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

#define INF 100000000

#define VISITED -1
#define UNSET -2

char happy[12000000][11];

int mem[(1<<10)];

char is_happy(int n, int b) {
// 	if(f) printf("- %d\n", n);
	
	if(n==1) return 1;
	if(happy[n][b] == VISITED) {
		happy[n][b] = 0;
		return 0;
	}
	if(happy[n][b] == UNSET) {
		happy[n][b] = VISITED;
		int s=0, tn=n;
		while(tn>0) {
			int r=tn%b; tn/=b;
			s+=r*r;
		}
		happy[n][b] = is_happy(s, b);
	}
	return happy[n][b];
}

int main(void)
{
	int i, j, k;
	int T;
	for(i=0; i<12000000; i++) for(j=0; j<11; j++) happy[i][j]=UNSET;

	scanf("%d", &T); getchar();
	int bases[20], nb;
	
	memset(mem, -1, sizeof(mem));
	
	FOR(caso, 1, T+1) {
		char c;
		nb=0; bases[0]=0;
		while(1) {
			c = getchar();
			if(c=='\n' || c==EOF) { ++nb; break; }
			if(c==' ') bases[++nb]=0;
			else bases[nb] = bases[nb]*10+c-'0';
		}
		
		sort(bases, bases+nb);
		int msk=0;
		for(i=0; i<nb; i++) msk |= (1<<(bases[i]-2));
		
		if(mem[msk] < 0) {
			int res=2;
			while(1) {
				char val=1;
				for(i=nb-1; val && i>=0; i--) val = val && is_happy(res, bases[i]);
				if(val) break;
				res++;
			}
			mem[msk]=res;
		}
		
		printf("Case #%d: %d\n", caso, mem[msk]);
		
	}
	return 0;
}
