#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
struct plant{
	int x,y,r;
}a[100];
double AC;
int tc,n;
double dis(int p,int q){
	return (1.0*sqrt((a[p].x-a[q].x)*(a[p].x-a[q].x)+(a[p].y-a[q].y)*(a[p].y-a[q].y)));
}

int main(){
	scanf("%d",&tc);
	for (int c=1;c<=tc;c++){
		scanf("%d",&n);
		for (int i=1;i<=n;i++) scanf("%d%d%d",&a[i].x,&a[i].y,&a[i].r);
		if (n==1) AC=a[1].r;
		else if (n==2){
			AC=max(a[1].r,a[2].r);
		}
		else {
			double A[3];
			A[1]=max((dis(1,2)+a[1].r+a[2].r)/2,a[3].r*1.0);
			A[2]=max((dis(2,3)+a[2].r+a[3].r)/2,a[1].r*1.0);
			A[3]=max((dis(1,3)+a[1].r+a[3].r)/2,a[2].r*1.0);
			AC=A[1];
			for (int i=2;i<=3;i++) if (AC>A[i]) AC=A[i];
		}
		printf("Case #%d: %lf\n",c,AC);
	}
	return 0;
}
