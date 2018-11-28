#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;
struct point {int x,y;};

int cross(point a,point b,point c){
	return abs(  (b.x-a.x)*(c.y-a.y)-(b.y-a.y)*(c.x-a.x));
}

//int gcd(int a,int b){
//	if( b==0 )return a;
//	return gcd(b,a%b);
//}
//double area(int xx[],int yy[]){
//int x[10],y[10];
//	 int i,j,k,S,E,dx,dy;
//	  x[0]=y[0]=0;S=E=0;
//	
//	    for(i=1;i<=3;i++){
//			//scanf("%d%d",&dx,&dy);
//			dx=xx[i];dy=yy[i];
//			x[i]=x[i-1]+dx;y[i]=y[i-1]+dy;
//			E+=gcd( abs(dx),abs(dy) );
//			S+=x[i-1]*y[i]-x[i]*y[i-1];
//		}
//		
//		return double(S)/2.0;
//}

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
	int S,E,I,i,k,cas,n;	
	int x[110],y[110],dx,dy;

	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	scanf("%d",&cas);
	
	for(k=1;k<=cas;k++){

		 scanf("%d%d%d",&N,&M,&A);
		printf("Case #%d: ",k);
		bool flag=solve();
		if(!flag)printf("IMPOSSIBLE\n");
		/*scanf("%d",&n);
		

		printf("Scenario #%d:\n",k);
        printf("%d %d %.1f\n\n",I,E,(double)S/2);*/
	}
	return 0;
}