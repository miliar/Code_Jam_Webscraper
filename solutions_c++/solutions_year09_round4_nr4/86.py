#include<iostream>
#include<cmath>
#define fo(i,u,d) for(int i=u;i<=d;i++)
using namespace std;
int t1=1,tt,n,m,id;
int d[110][3];
double ans;

double max(double x,double y){
		if (x>y)return x;
		else	return y;
}

double cal(int x,int y){
		double len=sqrt((d[x][0]-d[y][0])*(d[x][0]-d[y][0])+
						(d[x][1]-d[y][1])*(d[x][1]-d[y][1]));
		return (len+d[x][2]+d[y][2])/2;
}

int main(){
	freopen("ds.in","r",stdin);
	freopen("d.out","w",stdout);
	for(scanf("%d",&tt);t1<=tt;t1++){
		scanf("%d",&n);
		ans=0;
		fo(i,1,n){
			scanf("%d%d%d",&d[i][0],&d[i][1],&d[i][2]);
			ans>?=d[i][2];
		}
		if (n==3){
		ans=max(cal(1,2),d[3][2]);
		ans<?=max(cal(1,3),d[2][2]);
		ans<?=max(cal(2,3),d[1][2]);}
		printf("Case #%d: %.6lf\n",t1,ans);
	}
	return 0;
}
			
					
					
					
						
				
			
