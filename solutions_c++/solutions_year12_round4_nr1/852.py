#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cstdlib>
#include <cctype>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FORS(i,s) for(int i=0;(s)[i];i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define CLR(s) memset(s,0,sizeof(s))
typedef long long LL;
#define PB push_back

int n;

typedef pair<int,int> P;
#define X second
#define R first

struct XS{
	bool operator()(const P &a, const P &b){
		if(a.X != b.X) return a.X<b.X;
		return a.R < b.R;
	}
};

P a[100000];
int lx[100000];

int main() {

int nt, tt=0; scanf("%d", &nt); while(nt--){
	scanf("%d", &n);
	FOR(i,0,n){
		int r;
		scanf("%d%d", &a[i].X, &r);
		a[i].R = r;
	}
	int d;
	scanf("%d", &d);

	FOR(i,0,n) lx[i] = -1;
	lx[0]  = 0;

	bool ans = false;

	FOR(i,0,n){
		if(lx[i] < 0)continue;
		int cmx = min(a[i].X*2-lx[i], a[i].X+a[i].R);
		if(cmx >= d){
			ans = true;
			break;
		}
		FOR(j,i+1,n){
			if(cmx < a[j].X) break;
			if(lx[j]<0) lx[j] = a[i].X;
		}
	}

	/*
	int cr = a[0].R;
	int c = 0;
	//int x = 0;

	//sort(a,a+n,XS());
	FOR(i,0,n){
		int kr = 0;
		FOR(j,0,n){
			if(a[j].X > a[i].X)break;
			if(a[j].X < a[i].X-a[i].R) continue;
			kr = a[i].X - a[j].X;
			break;
		}
		a[i].R = max(a[i].R+a[i].X
	}

	priority_queue<P> q;

	while(1){
		bool did = false;
		//int far = -1;
		//int ox = x;
		while(c<n && a[c].X<=cr){
			q.push(a[c]);
			//int t = min(a[c].R, a[c].X*2-x);
			c++;
			did = true;
		}
		if(!did) break;
		cr = q.top().R;
	}
	*/

	printf("Case #%d: ", ++tt);
	if(ans)printf("YES\n"); else printf("NO\n");
}
	return 0;
}


