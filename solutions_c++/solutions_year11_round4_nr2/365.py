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

const int mr=503;
int r,c,d;
char buf[mr][mr];
int grid[mr][mr], sumgrid[mr][mr], xgrid[mr][mr], xsumgrid[mr][mr], ygrid[mr][mr], ysumgrid[mr][mr];

inline int getsumgrid(int i1,int j1,int i2,int j2){
	return sumgrid[i2][j2]-sumgrid[i1-1][j2]-sumgrid[i2][j1-1]+sumgrid[i1-1][j1-1];
}

inline int getxsumgrid(int i1,int j1,int i2,int j2){
	return xsumgrid[i2][j2]-xsumgrid[i1-1][j2]-xsumgrid[i2][j1-1]+xsumgrid[i1-1][j1-1];
}

inline int getysumgrid(int i1,int j1,int i2,int j2){
	return ysumgrid[i2][j2]-ysumgrid[i1-1][j2]-ysumgrid[i2][j1-1]+ysumgrid[i1-1][j1-1];
}

int main(){
	
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int Kase=GI;
	FOR(kase,1,Kase+1){
		r=GI, c=GI, d=GI;
		REP(i,r)	scanf("%s",buf[i]);
		REP(i,r)	REP(j,c)	grid[i+1][j+1]=(buf[i][j]-'0');
		REP(i,r+1)	xsumgrid[i][0]=ysumgrid[i][0]=sumgrid[i][0]=0;
		REP(j,c+1)	xsumgrid[0][j]=ysumgrid[0][j]=sumgrid[0][j]=0;
		FOR(i,1,r+1)	FOR(j,1,c+1)	xgrid[i][j]=i*grid[i][j];
		FOR(i,1,r+1)	FOR(j,1,c+1)	ygrid[i][j]=j*grid[i][j];
		FOR(i,1,r+1)	FOR(j,1,c+1)	sumgrid[i][j]=sumgrid[i-1][j]+sumgrid[i][j-1]-sumgrid[i-1][j-1]+grid[i][j];
		FOR(i,1,r+1)	FOR(j,1,c+1)	xsumgrid[i][j]=xsumgrid[i-1][j]+xsumgrid[i][j-1]-xsumgrid[i-1][j-1]+xgrid[i][j];
		FOR(i,1,r+1)	FOR(j,1,c+1)	ysumgrid[i][j]=ysumgrid[i-1][j]+ysumgrid[i][j-1]-ysumgrid[i-1][j-1]+ygrid[i][j];
		
		int k;
		for(k=min(r,c);k>=3;k--){
			FOR(i,1,r+1)	FOR(j,1,c+1)	if(i+k<=r+1 && j+k<=c+1){
				int i1=i+k-1, j1=j+k-1;
				int cx=(i+i1)/2, cy=(j+j1)/2;
				LD sx=0, sy=0;
				int kby2=k/2;
				if(k&1){
					sx=getxsumgrid(cx+1,cy-kby2,cx+kby2,cy+kby2)-cx*getsumgrid(cx+1,cy-kby2,cx+kby2,cy+kby2);
					sx+=getxsumgrid(cx-kby2,cy-kby2,cx-1,cy+kby2)-cx*getsumgrid(cx-kby2,cy-kby2,cx-1,cy+kby2);
					sy=getysumgrid(cx-kby2,cy+1,cx+kby2,cy+kby2)-cy*getsumgrid(cx-kby2,cy+1,cx+kby2,cy+kby2);
					sy+=getysumgrid(cx-kby2,cy-kby2,cx+kby2,cy-1)-cy*getsumgrid(cx-kby2,cy-kby2,cx+kby2,cy-1);
				}
				else{
					sx=getxsumgrid(cx+1,cy-kby2+1,cx+kby2,cy+kby2)-(cx+0.5)*getsumgrid(cx+1,cy-kby2+1,cx+kby2,cy+kby2);
					sx+=getxsumgrid(cx-kby2+1,cy-kby2+1,cx,cy+kby2)-(cx+0.5)*getsumgrid(cx-kby2+1,cy-kby2+1,cx,cy+kby2);
					sy=getysumgrid(cx-kby2+1,cy+1,cx+kby2,cy+kby2)-(cy+0.5)*getsumgrid(cx-kby2+1,cy+1,cx+kby2,cy+kby2);
					sy+=getysumgrid(cx-kby2+1,cy-kby2+1,cx+kby2,cy)-(cy+0.5)*getsumgrid(cx-kby2+1,cy-kby2+1,cx+kby2,cy);
				}
				int x,y;
				LD cix=(2*i+k-1)/2.0+0.5, ciy=(2*j+k-1)/2.0+0.5;
				{
					x=i, y=j;
					sx+=(cix-x-0.5)*grid[x][y], sy+=(ciy-y-0.5)*grid[x][y];	
				}
				{
					x=i, y=j1;
					sx+=(cix-x-0.5)*grid[x][y], sy+=(ciy-y-0.5)*grid[x][y];	
				}
				{
					x=i1, y=j;
					sx+=(cix-x-0.5)*grid[x][y], sy+=(ciy-y-0.5)*grid[x][y];	
				}
				{
					x=i1, y=j1;
					sx+=(cix-x-0.5)*grid[x][y], sy+=(ciy-y-0.5)*grid[x][y];	
				}
				if(fabs(sx)<EPS && fabs(sy)<EPS)	goto fin;
			}
		}
		fin:;
		printf("Case #%d: ",kase);
		if(k>=3)	printf("%d\n",k);
		else	printf("IMPOSSIBLE\n");
		cerr<<"Completed "<<kase<<endl;
	}
	
	cerr<<"Completed all"<<endl;
	while(1);
	return 0;
}
