#include<stdio.h>
#include<math.h>
#include<string.h>
#include<algorithm>
#define sqr(x) ((x)*(x))
using namespace std;
double a[10][3];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int nn;
	scanf("%d",&nn);
	for (int ii=1;ii<=nn;ii++) {
		printf("Case #%d: ",ii);
		int n;
		scanf("%d",&n);
		for (int i=1;i<=n;i++) scanf("%lf%lf%lf",&a[i][0],&a[i][1],&a[i][2]);
		if (n==1) printf("%lf\n",a[1][2]);
		else if (n==2) printf("%lf\n",max(a[1][2],a[2][2]));
		else {
		//	double tp=sqrt(sqr(a[1][0]-a[2][0])+sqr(a[1][1]-a[2][1]));
			double t1=(sqrt(sqr(a[1][0]-a[2][0])+sqr(a[1][1]-a[2][1]))+a[1][2]+a[2][2])/2;
			double t2=(sqrt(sqr(a[1][0]-a[3][0])+sqr(a[1][1]-a[3][1]))+a[1][2]+a[3][2])/2;
			double t3=(sqrt(sqr(a[3][0]-a[2][0])+sqr(a[3][1]-a[2][1]))+a[3][2]+a[2][2])/2;						
			t1=max(t1,a[3][2]);
			t2=max(t2,a[2][2]);
			t3=max(t3,a[1][2]);
			t1=min(t1,t2);
			t1=min(t1,t3);
			printf("%lf\n",t1);
		}
	}
}
