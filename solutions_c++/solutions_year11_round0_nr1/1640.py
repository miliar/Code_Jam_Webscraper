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
	forn(i,n){
		char c;
		cin >> c;
		if (c=='O')type[i]=0;else type[i]=1;
		cin>>val[i];
	}
	int res=0;
	int q=1,w=1;
	forn(i,n){
		int qwe=-1;
		forn(j,n)if(j>i&&type[j]!=type[i]){
			qwe=j;
			break;
		}
		if (qwe!=-1)qwe=val[qwe];
		if (type[i]==0){
			res+=abs(val[i]-q)+1;
			int dt = abs(val[i]-q)+1;
			if (qwe>w)w=min(qwe, w+dt);
			else if (qwe<w)w=max(qwe, w-dt);
			q=val[i];
		}else{
			res+=abs(val[i]-w)+1;
			int dt = abs(val[i]-w)+1;
			if (qwe>q)q=min(qwe, q+dt);
			else if (qwe<q)q=max(qwe, q-dt);
			w=val[i];
		}
	}
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