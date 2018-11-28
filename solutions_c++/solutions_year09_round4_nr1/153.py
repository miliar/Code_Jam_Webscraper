#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int a[100];
int main()
{
	int nn;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&nn);
	for (int ii=1;ii<=nn;ii++) {
		printf("Case #%d: ",ii);
		int n;
		scanf("%d",&n);
		char ts[50];
		int tem;
		gets(ts);
		for (int i=1;i<=n;i++){ 
			gets(ts);
			tem=-1;
			for (int j=0;j<n;j++) if (ts[j]=='1') tem=j;
			tem++;
			a[i]=tem;
		}
		int ans=0;
		for (int i=1;i<=n;i++) {
			if (a[i]>i) {
				for (int j=i+1;j<=n;j++) if (a[j]<=i) {tem=j;break;}
				for (int j=tem;j>i;j--) {ans++;swap(a[j],a[j-1]);}
			}
		}
		printf("%d\n",ans);
	}
}
