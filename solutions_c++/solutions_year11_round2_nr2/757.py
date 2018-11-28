#include <cstdio>
#include <algorithm>
using namespace std;

int main() {

freopen("b.in","r",stdin);
freopen("b.out","w",stdout);

int t;
scanf("%d",&t);

for (int j=1;j<=t;j++) {
	int c,d;
	scanf("%d%d",&c,&d);
	int l=0;
	int p[200];
	for (int i=0;i<c;i++) {
		int pp,v;
		scanf("%d%d",&pp,&v);
		for (int k=0;k<v;k++) {p[l]=pp;l++;}
		}
	sort(p,p+l);
//	for (int i=0;i<l;i++) printf("%d ",p[i]);
//	printf("\n");
	int delta[200];
	int r[200];	
	for (int i=0;i<l;i++) r[i]=0;

	for (int i=0;i<l-1;i++) delta[i]=p[i+1]-p[i];
	
	for (int i=0;i<l-1;i++) {
		if ((delta[i]-r[i])<d) r[i+1]=d-delta[i]+r[i];
		}
	int rmax=0;
	for (int i=0;i<l;i++) if (r[i]>rmax) rmax=r[i];
	double ans=rmax/2.0;
	printf("Case #%d: %lf\n",j,ans);
	
	}

return 0;
}
