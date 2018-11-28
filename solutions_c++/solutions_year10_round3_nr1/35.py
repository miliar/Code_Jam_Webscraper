#define forn(i, n) for(int i = 0; i<(int) n; i++)
#define ford(i, n) for(int i = (int)n -1; i>=0 ; i--)
#define pb push_back 
#define mp make_pair
#define se second
#define fi first
#define ll long long

#include <vector>
#include <list>
#include <map>
#include <set>
//#include <multiset>
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
#define sss 2000000
using namespace std;
 long long mm[sss+10];
 int t, n, a[20000], b[20000];
int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &t);
	forn(tn, t)
	{
		scanf("%d", &n);	
		forn(i, n)
			scanf("%d%d", &a[i],&b[i]);
		long long ans = 0;
		forn(i,n)
			forn(j, n)
				if (a[i]>a[j]&&b[i]<b[j]) 
					ans++;
		printf("Case #%d: ", tn+1);
		printf("%d", ans);
		printf("\n");
	}
	return 0;
}
