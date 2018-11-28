#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0
#pragma comment(linker, "/STACK:200000000")

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <fstream>
#include <iostream>
#include <map>
#include <memory.h>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <sstream>
#include <vector>
#include <utility>
#include <cmath>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()

#define forn(i,n) for (int i=0; i<int(n); ++i)
#define fornd(i,n) for (int i=int(n)-1; i>=0; --i)
#define forab(i,a,b) for (int i=int(a); i<=int(b); ++i)

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

const int INF = (int) 1e9;
const long long INF64 = (long long) 1e18;
const long double eps = 1e-9;
const long double pi = 3.14159265358979323846;

int main(){
#ifndef ONLINE_JUDGE
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
#endif
	int t;
	scanf("%d", &t);
	forn(testcase,t){
		int n;
		scanf("%d", &n);
		vector <int> d(n),l(n);
		forn(i,n)
			scanf("%d%d", &d[i], &l[i]);
		int D;
		scanf("%d", &D);
		vector <int> lg(n+100,-1);
		lg[0] = min(l[0],d[0]);
		forn(i,n){
			for (int j=0; j<i; j++){
				if (lg[j]!=-1 && lg[j]>=d[i]-d[j]){
					lg[i] = min(l[i],d[i]-d[j]);
					break;
				}
			}
		}
		bool ok = false;
		forn(i,n)
			if (d[i]+lg[i]>=D)
				ok = true;
		if (ok)
			printf("Case #%d: YES\n", testcase+1);
		else
			printf("Case #%d: NO\n", testcase+1);
	}
	return 0;
}