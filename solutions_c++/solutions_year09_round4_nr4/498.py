#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cstdio>
#include <cctype>
#include <cassert>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,n) FOR(i,0,n)
#define sz size()
#define pb push_back
#define GI ({int t;scanf("%d",&t);t;})
#define INF int(1e9)

typedef long long LL;
typedef vector<int> VI;
typedef vector< vector<int> > VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;

const int mn=42;
struct pt{
	double x,y,r;	
};
pt a[mn];
int n;

bool ispos(int v,double rad){
	if(v==1)	return rad>=a[0].r;
	if(v==2)	return rad>=a[1].r;
	if(v==4)	return rad>=a[2].r;
	if(v==3)	return rad>=a[0].r+a[1].r+sqrt((a[0].x-a[1].x)*(a[0].x-a[1].x)+(a[0].y-a[1].y)*(a[0].y-a[1].y));
	if(v==5)	return rad>=a[0].r+a[2].r+sqrt((a[0].x-a[2].x)*(a[0].x-a[2].x)+(a[0].y-a[2].y)*(a[0].y-a[2].y));
	if(v==6)	return rad>=a[2].r+a[1].r+sqrt((a[2].x-a[1].x)*(a[2].x-a[1].x)+(a[2].y-a[1].y)*(a[2].y-a[1].y));
	
}

bool f(double rad){
	if(ispos(1,rad) && ispos(6,rad))	return 1;
	if(ispos(2,rad) && ispos(5,rad))	return 1;
	if(ispos(4,rad) && ispos(3,rad))	return 1;
	return 0;
}

int main(){
	
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int Kase=GI;
	FOR(kase,1,Kase+1){
		n=GI;
		REP(i,n){
			int x=GI,y=GI,r=GI;
			a[i].x=x,a[i].y=y,a[i].r=r;	
		}
		if(n==1)	{printf("Case #%d: %.5lf\n",kase,a[0].r);continue;}
		if(n==2)	{printf("Case #%d: %.5lf\n",kase,max(a[0].r,a[1].r));continue;}
		double lo=0,hi=1e6,mid=(lo+hi)/2;
		while(hi-lo>1e-8){
			if(f(mid))	hi=mid;
			else	lo=mid;
			mid=(lo+hi)/2;	
		}
		printf("Case #%d: %.5lf\n",kase,mid/2);
		
			
	}
	
	cerr<<"Finished Executing"<<endl;
	while(1);
	return 0;
}
