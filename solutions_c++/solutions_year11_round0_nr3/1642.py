#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <sstream>
#include <utility>
#pragma comment (linker, "/STACK:90000000")
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define forv(i, v) for (int i = 0; i < (int)(v.size()); ++i)
#define fors(i, s) for (int i = 0; i < (int)(s.length()); ++i)
#define all(a) a.begin(), a.end()
#define pb push_back
#define PII pair<int, int>
#define mp make_pair
#define VI vector<int>
#define VS vector<string>
using namespace std;

int type[100];
int val[100];

void solve(int tc){
	int n;
	cin >> n;
	forn(i,n)cin>>val[i];
	int xor=0;
	forn(i,n)xor^=val[i];
	int res=0;
	forn(i,n)res+=val[i];
	res-=*min_element(val, val+n);
	if (xor)printf("Case #%d: NO\n",tc);else
		printf("Case #%d: %d\n", tc, res);
}

int main(){
#ifdef __ASD__
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
	int q=0,w=0;
	int tc;
	cin >> tc;
	forn(i,tc){
		solve(i+1);
	}

	return 0;
} 