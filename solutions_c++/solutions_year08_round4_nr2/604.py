#include<iostream>
#include<algorithm>
#include<cmath>
#include<cassert>
using namespace std;

#define INF 10010
#define N 64
int n,m,a;
#define min(a,b) ((a)<(b)?(a):(b))
int area2(int ax,int ay,int bx,int by,int cx,int cy){
	return (bx-ax)*(cy-ay)-(cx-ax)*(by-ay);
}
int main()
{	
#ifndef ONLINE_JUDGE
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int cas;
	scanf("%d",&cas);
	for(int ii=1;ii<=cas;ii++){
		printf("Case #%d: ",ii);
		scanf("%d%d%d",&n,&m,&a);
		if(n*m<a) printf("IMPOSSIBLE\n");
		else if(n*m==a){
			printf("0 0 %d 0 %d %d\n",n,n,m);
		}else{
			bool f=false;
			for(int i1=0;i1<=n&&!f;i1++) for(int j1=0;j1<=m&&!f;j1++){
				for(int i2=0;i2<=n&&!f;i2++) for(int j2=0;j2<=m&&!f;j2++){
					for(int i3=0;i3<=n&&!f;i3++) for(int j3=0;j3<=m&&!f;j3++){
							if(!((i1==i2&&i1==i3) || (j1==j2&&j1==j3)) ){
							int re=area2(i1,j1,i2,j2,i3,j3);
							if(re==a){
								printf("%d %d %d %d %d %d\n",i1,j1,i2,j2,i3,j3);
								f=true;
								break;
							}
						}
					}
				}
			}
			if(!f)
				printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}