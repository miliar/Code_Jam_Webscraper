#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

int n,c,x[3],y[3],r[3];
double AC;

double sqr(int x){return (double)x*x;}

double dist(int a,int b){
	return sqrt(sqr(x[a]-x[b])+sqr(y[a]-y[b]));
}

int main(){
	scanf("%d",&c);
		for (int tc=1;tc<=c;tc++){
		scanf("%d",&n);
			for (int i=0;i<n;i++) scanf("%d%d%d",x+i,y+i,r+i);
			if (n==1) AC=r[0]*2.0;
			else if (n==2) AC=max(r[0]*2.0,r[1]*2.0);			
			else{
			AC=1e9;
			AC=min(AC,max(dist(1,2)+r[1]+r[2],r[0]*2.0));
			AC=min(AC,max(dist(0,2)+r[0]+r[2],r[1]*2.0));
			AC=min(AC,max(dist(0,1)+r[0]+r[1],r[2]*2.0));
			}
		printf("Case #%d: %.9lf\n",tc,AC/2.0);
		}
	return 0;
}

