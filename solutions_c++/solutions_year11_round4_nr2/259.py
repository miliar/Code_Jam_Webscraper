#include <iostream>
#include <cstdio>
#include <algorithm>
#define EPSILON 1e-8
using namespace std;

int T,R,C,D,G[505][505],MAX,t1,t2,t3,tmp,ans;
double ax,ay,bx,by;
char chara;

bool eq(double x,double y){
	return (x-y < EPSILON && y-x < EPSILON);
}

void sum(int x1,int y1,int x2,int y2){
	t1 = 0;
	for(int i=x1;i<=x2;++i)
		for(int j=y1;j<=y2;++j) t1 += G[i][j]+D;
	t1 -= (G[x1][y1] + G[x2][y1] + G[x1][y2] + G[x2][y2] + 4*D);
}

void fx(int x1,int y1,int x2,int y2){
	t2 = 0;
	for(int i=x1;i<=x2;++i)
		for(int j=y1;j<=y2;++j) t2 += i*(G[i][j]+D);
	t2 -= ( x1*(G[x1][y1]+G[x1][y2]+2*D) + x2*(G[x2][y1]+G[x2][y2]+2*D));
}

void fy(int x1,int y1,int x2,int y2){
	t3 = 0;
	for(int i=x1;i<=x2;++i)
		for(int j=y1;j<=y2;++j) t3 += j*(G[i][j]+D);
	t3 -= ( y1*(G[x1][y1]+G[x2][y1]+2*D) + y2*(G[x1][y2]+G[x2][y2]+2*D));
}

int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&T);
	for(int testcase=1;testcase<=T;++testcase){
		scanf("%d%d%d",&R,&C,&D);
		ans = 0;
		for(int i=1;i<=R;++i)
			for(int j=1;j<=C;++j){
				scanf(" %c",&chara);
			//	printf("entered %c\n",chara);
				G[i][j] = chara - '0';
			}
	/*	for(int i=1;i<=R;++i,printf("\n"))
			for(int j=1;j<=C;++j) printf("%d",G[i][j]);*/
		MAX = min(R,C);
		for(int k=3;k<=MAX;++k){
			for(int i=1;i<=R-k+1;++i)
				for(int j=1;j<=C-k+1;++j){
					sum(i,j,i+k-1,j+k-1);
					fx(i,j,i+k-1,j+k-1);
					fy(i,j,i+k-1,j+k-1);
				//	printf("%d %d %d\n",t1,t2,t3);
					ax = (double)(2*i+k-1)/2.0;
					ay = (double)(2*j+k-1)/2.0;
					bx = (double)(t2)/(double)(t1);
					by = (double)(t3)/(double)(t1);
					if(eq(ax,bx) && eq(ay,by)) ans = k;
				//	printf("(%d %d %d %d) (%lf %lf) (%lf %lf)\n",i,j,i+k-1,j+k-1,ax,ay,bx,by);
				}
		}
		if(ans == 0) printf("Case #%d: IMPOSSIBLE\n",testcase);
		else printf("Case #%d: %d\n",testcase,ans);
	}
}
