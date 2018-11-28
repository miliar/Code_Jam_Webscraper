#pragma comment (linker, "/STACK:90000000")
#define _CRT_SECURE_NO_DEPRECATE
#define _CRT_SECURE_NO_WARNINGS
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>
#include <cfloat>
#include <cstdio>
#include <sstream>
#include <utility>
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define forv(i, v) for (int i = 0; i < (int)(v.size()); ++i)
#define fors(i, s) for (int i = 0; i < (int)(s.length()); ++i)
#define all(a) a.begin(), a.end()
#define pb push_back
#define PII pair<int, int>
#define mp make_pair
#define VI vector<int>
#define VS vector<string>
#define lng long long
using namespace std;

void solve(int tc){
	int n, l, h;
	cin >> n >> l >> h;
	int *a=new int[n];
	forn(i,n)cin>>a[i];
	printf("Case #%d: ", tc);
	for(int i=l;i<=h;++i){
		bool ok=true;
		forn(j,n) if (a[j]%i && i%a[j]){
			ok=false;
			break;
		}
		if (ok){
			printf("%d\n", i);
			return;
		}
	}
	printf("NO\n");
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tc;
	cin >> tc;
	forn(i, tc)solve(i+1);
	return 0;
}
