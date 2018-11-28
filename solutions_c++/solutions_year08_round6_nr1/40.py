#include <cstdio>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <iomanip>
#include <iostream>
#include <cassert>
#include <ext/hash_map>
#include <ext/hash_set>
#include <ext/rope>
#include <ext/slist>

using namespace std;
using namespace __gnu_cxx;

typedef vector<int>VI;
typedef vector<string>VS;
typedef long long LL;
#define SIZE(c) ((int)(c).size())
#define SEQ(c) (c).begin(),(c).end()
#define FOR(i,a,b) for(int _U(b),i=(a);i<_U;++i)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int _U(a),i=(b)-1;i>=_U;--i)
#define FORS(i,c) FOR(i,0,SIZE(c))
#define REPD(i,n) FORD(i,0,n)
template<class T>string tostr(T v){ostringstream o;o<<v;return o.str();}
const int inf = 1000100100; 

#define maxn 1024

int x[maxn],y[maxn];
bool f[maxn];
int N,M;
int BC;
int fx[]={-1,0,1,-1,0,1,-1,0,1};
int fy[]={-1,-1,-1,0,0,0,1,1,1};

int msk[maxn];

int u,d,l,r;
int U,D,L,R;

int check(int xx,int yy){
	int i;
	int code=0;
	if (BC==0){
		for (i=0;i<N;i++) if (!f[i] && xx==x[i] && yy==y[i]) return -1;
		return 0;
	}
	if (xx<=L || xx>=R || yy<=D || yy>=U) return -1;
	if (xx>=l && xx<=r && yy>=d && yy<=u) return 1;
	if (xx<l) code+=0;
	else if (xx>r) code+=2;
	else code+=1;
	if (yy<d) code+=0;
	else if (yy>u) code+=6;
	else code+=3;
	for (i=0;i<N;i++) if (!f[i] && code==msk[i]){
		if (xx*fx[code]>=x[i]*fx[code] && yy*fy[code]>=y[i]*fy[code]) return -1;
	}
	return 0;
}

void solve(int cas){
	int i;
	int xx,yy;
	char tmp[10];
	scanf("%d",&N);
	u=-inf;
	d=inf;
	l=inf;
	r=-inf;
	BC=0;
	for (i=0;i<N;i++){
		scanf("%d%d%s",x+i,y+i,tmp);
		if (tmp[0]=='B'){
			f[i]=1;
			BC++;
		}
		else{
			f[i]=0;
			scanf("%*s");
		}
		if (f[i]==0) continue;
		u=max(u,y[i]);
		d=min(d,y[i]);
		l=min(l,x[i]);
		r=max(r,x[i]);
	}
	memset(msk,0,sizeof(msk));
	for (i=0;i<N;i++) if (!f[i]){
		if (x[i]<l) msk[i]+=0;
		else if (x[i]>r) msk[i]+=2;
		else msk[i]+=1;
		if (y[i]<d) msk[i]+=0;
		else if (y[i]>u) msk[i]+=6;
		else msk[i]+=3;	
	}
	U=R=inf;
	L=D=-inf;
	for (i=0;i<N;i++) if (msk[i]==1) D=max(D,y[i]);
	else if (msk[i]==3) L=max(L,x[i]);
	else if (msk[i]==5) R=min(R,x[i]);
	else if (msk[i]==7) U=min(U,y[i]);
	scanf("%d",&M);
	printf("Case #%d:\n",cas);
	while (M--){
		scanf("%d%d",&xx,&yy);
		i=check(xx,yy);
		switch (i){
			case 1: printf("BIRD\n"); break;
			case -1: printf("NOT BIRD\n"); break;
			case 0: printf("UNKNOWN\n"); break;
		}
	}
}

int main(){
	int t,cas;
	scanf("%d",&t);
	for (cas=1;cas<=t;cas++)
		solve(cas);
	return 0;
}

