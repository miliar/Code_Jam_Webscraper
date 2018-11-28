#include<set>
#include<map>
#include<cmath>
#include<cstdio>
#include<vector>
#include<string>
#include<iostream>
#include<sstream>
#include<algorithm>
using namespace std;
#define FOR(i,a,b) for(int i=(a); i<(b); ++i)
#define FORE(i,a) for(typeof(a.begin()) i = a.begin(); i!= a.end(); ++i)
#define SET(x,v) memset(x,v,sizeof(x))
#define cs c_str()
#define sz size()
#define mp make_pair
#define pb push_back
int K;
string dat;
int calc (string& t) {
	char prev = '.';
	int cnt = 0;
	FORE(x,t) {
		cnt+= (*x) != prev;
		prev = *x;
	}
	return cnt;
}
int main() {
	freopen("D.in","r",stdin);
	int e = 0, T, ans;
	char buff[1024];
	scanf("%d",&T);
	while(T--) {
		scanf("%d%s",&K,buff);
		dat = buff;
		ans = calc(dat);
		vector<int> perm;
		FOR(i,0,K)
			perm.pb(i);
		int n = dat.sz;
		do {
			string p = string(n, ' ');
			for(int i = 0 ; i < n ; i+= K) {
				FOR(j,0,K) {
					p[i+perm[j]] = dat[i + j];
				}
			}
			int now = calc(p);
			if(ans>now)ans = now;
		} while(next_permutation(perm.begin(), perm.end()));
		printf("Case #%d: %d\n",++e,ans);
	}
	return 0;
}