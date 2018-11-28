#ifdef LOCAL
#pragma warning(disable:4786)
#define ll __int64
#define FORMATLL "%I64d" 
#else
#define ll long long
#define FORMATLL "%lld"
#endif
#include <iostream>
#include <strstream>
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
#define forab(i,a,b) for(i=(a);i<(b);++i)
#define MAX(a,b) ((a)<(b)?(b):(a))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define clr(a) memset(a,0,(sizeof a));
#define SWAP(a,b) a^=b,b^=a,a^=b;
using namespace std;

// template here

// template end

// global variable
int n;
char strtmp[30];
// global end

void solve()
{
	int i, k, lv;
	char ch;
	for(i=n-2; i>=0; --i){
		if(strtmp[i+1] > strtmp[i]){
			break;
		}
	}
	char best;
	if(i>=0){
		best = i+1;
		for(k=i+1; k< n; k++)if(strtmp[k] > strtmp[i] && strtmp[k] < strtmp[best]){
			best = k;
		}
		swap(strtmp[i], strtmp[best]);
		sort(strtmp+i+1, strtmp+n);
		return;
	}

	int cnt[256];
	clr(cnt);
	forn(i,n){
		cnt[strtmp[i]]++;
	}

	k = '1';
	while(cnt[k] ==0){
		k++;
	}
	lv = 0;
	cnt[k]--;

	sprintf(strtmp+lv, "%c", (char)k);
	lv += strlen(strtmp);

	strtmp[lv++] = '0';
	strtmp[lv] = 0;
	
	for(k='0'; k<='9'; ++k){
		forn(i,cnt[k])sprintf(strtmp+lv+i, "%c", (char)k);
		lv += strlen(strtmp+lv);
	}
}

char input()
{
	int i, k;
	scanf("%s", strtmp);
	n = strlen(strtmp);

	return 1;
}

int main()
{
#ifdef LOCAL
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int i, k, lv, ca, ica;
	scanf("%d", &ca);
	
	forn(ica,ca){
		input();
		solve();
		printf("Case #%d: ", ica+1);
		puts(strtmp);
	}
	return 0;
}
