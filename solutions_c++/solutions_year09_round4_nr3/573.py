
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <list>
#include <complex>
#include <cstdio>
#include <string>
#include <stack>
#include <cctype>
#include <cassert>
#include <vector>
#include <cmath>
#include <ctime>
#include <cstring>
#include <functional>
#include <cstdlib>
#include <queue>
using namespace std;
#define trav(it,cont) for(it=(cont).begin(); it!=(cont).end(); ++it)
#define forn(i,n) for(i=0;(i)<(n);++i)
#define clr(a) memset(a,0,(sizeof a));
#define MAX(a,b) ((a)>(b)?(a):(b))
using namespace std;

// template here

// template end

// global variable
int n, m;
char strtmp[1000];
const int N = 110;
struct S
{
	int v[30];
	void scan(){
		int i;forn(i,m)scanf("%d", v+i);
	}
	bool operator<(const S& b)const
	{
		int i;
		forn(i,m){
			if(v[i] >= b.v[i])return false;
		}
		return true;
	}
}stock[N];
char g[N][N];
int cnt[N];

int p[N];
int find_set(int i)
{
	if(p[i] == -1)return p[i] = i;
	if(p[i] == i)return p[i];
	return p[i] = find_set(p[i]);
}

// global end


char input()
{
	int i, j;
	scanf("%d", &n);
	
	scanf("%d", &m);
	forn(i,n){
		stock[i].scan();
	}

	memset(g,1,(sizeof g));

	forn(i,n)forn(j,n){
		if(stock[i] < stock[j])g[i][j] = g[j][i] = 0;
	}
	return 1;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int i, j, k, ca, ica, lv, px, py;
	scanf("%d", &ca);
	
	forn(ica,ca){
		input();
		
		int ans = 0;

		int lv = 0;
		forn(lv,(1<<n)){
			char f = 1;
			int cnt = 0;
			k = lv;
			while(k){
				cnt += k%2;
				k/=2;
			}
			if(cnt <= ans)continue;
		
			for(i=0;i<n;i++)if((1<<i)&lv){
				for(k=0;k<n;k++)if(i!=k &&((1<<k)&lv)){
					if(g[i][k] == 0){
						f=0;
						goto OUT;
					}
				}
			}
OUT:
			if(f == 1){
				ans = MAX(ans,cnt);
			}
		}

		printf("Case #%d: %d\n", ica+1, ans);
		
	}
	return 0;
}
