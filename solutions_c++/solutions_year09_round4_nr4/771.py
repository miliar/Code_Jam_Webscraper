#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
struct pp{
	double x;
	double y;
	double dis(pp a){
		return sqrt((x-a.x)*(x-a.x)+(y-a.y)*(y-a.y));
	}
};

pp p[100];
double r[100];
double m[10];

int main(){
	int nn,ii,n;
	scanf("%d",&nn);
	for(int ii=1;ii<=nn;ii++){
		double ans;
		scanf("%d",&n);
		for(int i=0;i<n;i++)scanf("%lf%lf%lf",&p[i].x,&p[i].y,&r[i]);
		if(n==1)ans = r[0];
		else if(n==2)ans = max(r[0],r[1]);
		else{
			ans = 1e40;
			for(int i=0;i<n;i++){
				ans = min(ans, max(r[i],(r[(i+1)%n]+r[(i+2)%n]+p[(i+1)%n].dis(p[(i+2)%n]))*0.5));
			}
		}
		printf("Case #%d: %f\n",ii,ans);
	}
	return 0;
}

