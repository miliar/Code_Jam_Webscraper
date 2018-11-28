#include <iostream>
using namespace std;
int a[1000],n,m;
int main()
{
//	freopen("A-large.in","r",stdin);
//	freopen("A.out","w",stdout);
	int t,i,j,k=0,r=0;
	for (scanf("%d",&t);t;t--)
	{
		r++;
		scanf("%d%d",&n,&m);
		i=1<<(n);
		i--;
		j=i+1;
		printf("Case #%d: ",r);
		if (m%j==i)puts("ON");else puts("OFF");
	}
}