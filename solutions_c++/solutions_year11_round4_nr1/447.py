#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string.h>
#include <cassert>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define INF (int)1e9
#define EPS LD(1e-9)
#define DINF LD(1e50)

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef pair<int,int> PII;
typedef double LD;

const int mn=1005;
int x,s,r,n;
LD t;

struct node{
	int b,e,w;	
};
node a[mn];

bool cmp(const node & p,const node & q){
	return p.w<q.w;	
}

int main(){
	
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int Kase=GI;
	FOR(kase,1,Kase+1){
		x=GI, s=GI, r=GI, t=GI, n=GI;
		REP(i,n)	a[i].b=GI, a[i].e=GI, a[i].w=GI;
		int tot=0;
		REP(i,n)	tot+=a[i].e-a[i].b;
		tot=x-tot;
		sort(a,a+n,cmp);
		LD tosub=min(t*r,LD(tot));
		t-=tosub/LD(r);
		LD ans=0;
		ans+=(tosub)/LD(r)+(tot-tosub)/LD(s);
		REP(i,n){
			tosub=min(t*(r+a[i].w),LD(a[i].e-a[i].b));
			t-=tosub/LD(r+a[i].w);
			ans+=(tosub)/LD(r+a[i].w)+(a[i].e-a[i].b-tosub)/LD(s+a[i].w);
		}
		printf("Case #%d: %.9lf\n",kase,ans);
		cerr<<"Completed "<<kase<<endl;
	}
	
	cerr<<"Completed all"<<endl;
	while(1);
	return 0;
}
