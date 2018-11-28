#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;
struct point {int x,y;};

int cross(point a,point b,point c){
	return abs(  (b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x));
}

int N,M,A;
bool solve(){

	point a,b,c;
	int x[10],y[10];
	
	int x1,y1,x2,y2,x3,y3;
       
		
        for(x1=0;x1<=N;x1++)
			for(y1=0;y1<=M;y1++){
				if( (N-x1)*(M-y1)<A)continue;
				for(x2=x1;x2<=N;x2++)
					for(y2=y1;y2<=M;y2++)
						for(x3=x1<x2?x1:x2;x3<=N;x3++)
							for(y3=y1<y2?y1:y2;y3<=M;y3++){
								x[1]=x1;x[2]=x2;x[3]=x3;
								y[1]=y1;y[2]=y2;y[3]=y3;

								a.x=x1;a.y=y1;
								b.x=x2;b.y=y2;
								c.x=x3;c.y=y3;
								if( cross(a,b,c)==A ){

									printf("%d %d %d %d %d %d\n",x[1],y[1],x[2],y[2],x[3],y[3]);
									return true;
								}
							}
			}

	return false;
}
int main(){
	int S,E,I,i,k,t,n;	
	int x[110],y[110],dx,dy;

	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	scanf("%d",&t);
	
	for(k=1;k<=t;k++){

		 scanf("%d%d%d",&N,&M,&A);
		printf("Case #%d: ",k);
		bool flag=solve();
		if(!flag)printf("IMPOSSIBLE\n");

	}
	return 0;
}
