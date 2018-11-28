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

typedef long long i64;

int ans ;
int R, C, n;
int r[12], c[12];
bool no[128][128];
int cach[128][128];
const int mod = 10007;
int doit(int x, int y) {
	int& ret = cach[x][y];
	if(ret!=-1)return ret;
	ret = 0;
	if (no[x][y])return ret;
	if (x>R || y>C) return ret;
	if(x==R && y==C) return ret = 1;
	int v1 = doit(x+1, y+2);
	int v2 = doit(x+2, y+1);
	ret = v1 + v2;
	if (ret >= mod) ret -= mod;
	return ret;
}

int main() {
	freopen("D.in","r",stdin);
	int e = 0, T;
	scanf("%d",&T);
	while(T--) {	
		ans = 0;
		scanf("%d%d%d",&R,&C,&n);
		SET(no,0);
		FOR(i,0,n) {
			scanf("%d%d",&r[i],&c[i]);
			no[r[i]][c[i]] = 1;
		}
		SET(cach, -1);
		ans = doit(1, 1);
		printf("Case #%d: %d\n",++e,ans);
	}

	return 0;
}


