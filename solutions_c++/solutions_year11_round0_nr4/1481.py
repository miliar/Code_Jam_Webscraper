#include<stdio.h>
#include<vector>
#include<algorithm>

using namespace std;

double D[111];
int coeff[111];
int all;

int T;
int a[111], b[111];
int n;

int main(void)
{
	int l0, l1, l2;

	freopen("D1.in","r",stdin);
	freopen("D1.out","w",stdout);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%d",&n);
		for(l1=0;l1<n;l1++)
		{
			scanf("%d",&a[l1]);
			b[l1] = a[l1];
		}
		sort(b, b+n);
		int ret = 0;
		for(l1=0;l1<n;l1++)
			if(a[l1] != b[l1]) ret++;
		printf("Case #%d: %.6lf\n",l0,(double)ret);
	}


	return 0;
}