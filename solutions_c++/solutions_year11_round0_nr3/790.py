#include <cstdio>

int main() {

freopen("c.in","r",stdin);
freopen("c.out","w",stdout);

int t;
scanf("%d",&t);

for (int j=0;j<t;j++) {
	int n;
	scanf("%d",&n);
	int a[1000];
	for (int i=0;i<n;i++) scanf("%d",&a[i]);
	int xsum=0;
	int sum=0;
	int min=999999;
	for (int i=0;i<n;i++) 
		{
		xsum^=a[i];
		sum+=a[i];
		if (a[i]<min) min=a[i];
		}
	printf("Case #%d: ",j+1);
	if (xsum) printf("NO\n");
		else printf("%d\n",sum-min);
	}

}
