#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>
#include <math.h>
using namespace std;
typedef long long LL;
typedef vector<string> vs;
typedef vector<int> vi;

double res[3];
int n,ntc,x[4],y[4],r[4];

double pyta(int x1,int y1,int x2,int y2){
	double dx=x2-x1;
	double dy=y2-y1;
	return (sqrt(dx*dx+dy*dy));
}

int main(){
	freopen("Dsmall.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&ntc);
	for (int tc=1;tc<=ntc;tc++){
		scanf("%d",&n);
		for (int i=0;i<n;i++)
			scanf("%d %d %d",&x[i],&y[i],&r[i]);
		if (n==3){
			res[0]=pyta(x[0],y[0],x[1],y[1])+r[0]+r[1];
			res[1]=pyta(x[0],y[0],x[2],y[2])+r[0]+r[2];
			res[2]=pyta(x[1],y[1],x[2],y[2])+r[1]+r[2];
			res[0]/=2.0;
			res[1]/=2.0;
			res[2]/=2.0;
			res[0]=max(res[0],1.0*r[2]);
			res[1]=max(res[1],1.0*r[1]);
			res[2]=max(res[2],1.0*r[0]);
			sort(res,res+3);
		}
		else if (n==2){
			res[0]=pyta(x[0],y[0],x[1],y[1])+r[0]+r[1];
			res[0]/=2.0;
			res[1]=max(r[0],r[1]);
			sort(res,res+2);
		}
		else if (n==1) res[0]=r[0];
		printf("Case #%d: %.7lf\n",tc,res[0]);
	}
	return 0;
}