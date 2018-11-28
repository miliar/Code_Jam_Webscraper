#include <iostream>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

#define pb push_back
#define sz size()
#define MAXN 

void opens(){
	freopen("Dsmall.in","r",stdin);
	freopen("Dsmall.out","w",stdout);
}

void openb(){
	freopen("Dlarge.in","r",stdin);
	freopen("Dlarge.out","w",stdout);
}

int Ax,Ay,Bx,By,x,y;
double ans,a,b,c,sdt;

double sqr(double a){
	return a*a;
}

double dist(int x,int y,int x2,int y2){
	return sqrt(sqr(x-x2)+sqr(y-y2));
}

int main(){
	opens();
	//openb();
	int t;
	scanf("%d",&t);
	int xx=1;
	while (t--){
		int n,m;
		scanf("%d%d",&n,&m);
		scanf("%d%d",&Ax,&Ay);scanf("%d%d",&Bx,&By);
		printf("Case #%d:",xx++);
		for (int i=0;i<m;i++){
			scanf("%d%d",&x,&y);
			a=dist(Ax,Ay,Bx,By);
			b=dist(Ax,Ay,x,y);
			c=dist(Bx,By,x,y);
			sdt=acos((sqr(a)+sqr(c)-sqr(b))/(2*a*c));
			sdt*=2;
			ans=(sdt/2*c*c-sin(sdt)*c*c/2.0);
			sdt=acos((sqr(a)+sqr(b)-sqr(c))/(2*a*b));
			sdt*=2;
			ans+=(sdt/2*b*b-sin(sdt)*b*b/2.0);
			printf(" %lf",ans);
		}
		printf("\n");
	}
	//system("pause");
	return 0;
}
