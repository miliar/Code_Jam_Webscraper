#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>
#include <iostream>
const int INF = 1000*1000*1000;

using namespace std;

#define forn(i,n) for(int i=0; i<(int)n; i++)
#define sz(a) a.size()

int v_max(vector<int>v) {
	int r = -1;
	forn(i,sz(v))
		r=max(r,v[i]);
	return r;
}

int v_min(vector<int>v) {
	int r = INF;
	forn(i,sz(v))
		r=min(r,v[i]);
	return r;
}

bool ok(vector<int> v, int s) {
	if (v[0]+v[1]+v[2]!=s) return false;
	if (v_max(v)-v_min(v)>2) return false;
	return true;
}
bool isgood(vector<int>v) {
	return (v_max(v)-v_min(v)<2);
}
int d[33][2], T;

int main () {
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	vector<int> v(3);
	forn(i,31) {
		forn(j,11)
			forn(k,11)
				forn(t,11)
				{
					v[0]=j, v[1]=k, v[2]=t;
					if (ok(v,i)) {
						d[i][!isgood(v)]=max(v_max(v),d[i][!isgood(v)]);
					}
				}
	}
	//forn(i,31)
		//printf("%d %d %d\n",i,d[i][1],d[i][0]);
	scanf("%d",&T);
	forn(i,T) {
		scanf("\n");
		printf("Case #%d: ",i+1);
		int ans = 0, N, S, P;
		scanf("%d %d %d",&N, &S, &P);
		int u;
		if (N==1) u=2;
		if (N==2) u=4;
		if (N==3) u=8;
		vector <int> y(N);
		forn(j,N) 
			scanf("%d",&y[j]);
		forn(j,u) {
			int cnt = 0;
			forn(o,N)
				if (j & (1<<o))
					cnt++;
			if (cnt==S) {
			cnt = 0;
			forn(o,N)
				if (j & (1<<o))
					cnt+=(d[y[o]][1]>=P);
				else 
					cnt+=(d[y[o]][0]>=P);
				ans=max(ans,cnt);
			}
		}
		printf("%d\n",ans);
	}
}