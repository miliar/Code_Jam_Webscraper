#ifdef LOCAL
#pragma warning(disable:4786)
#define ll __int64
#define FORMATLL "%I64d" 
#else
#define ll long long
#define FORMATLL "%lld"
#endif
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
using namespace std;

// template here

// template end

// global variable
int n;
char strtmp[1000];
const int N = 40;
int g[N];
// global end


char input()
{
	int i, j, lv;
	scanf("%d", &n);

	clr(g);
	forn(i,n){
		scanf("%s", strtmp);
		forn(j,n)if(strtmp[j] == '1')g[i] = j;
	}
	
	return 1;
}

int solve()
{
	int i, j, k, cnt1, cnt2;
	cnt1 = 0; cnt2 = 0;
	int ans= 0;
//	forn(i,n)cerr << g[i] << ' ' ; cerr <<endl;

	forn(i,n){
		k = 0;
		for(j=0; j< i; ++j)if(g[j] < g[i])k++;
		if(g[i]-k>=0)ans += g[i]-k;
	}
	return ans;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("c:/out.txt", "w", stdout);
	
	int i, j, k, ca, ica, lv;
	scanf("%d", &ca);
	
	forn(ica,ca){
		input();
		
		printf("Case #%d: %d\n", ica+1, solve());
		
	}
	return 0;
}
