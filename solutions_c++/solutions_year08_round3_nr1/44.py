#include <iostream>
#include <algorithm>
using namespace std;

__int64 a[1002];
int n,m,l;

bool com(__int64 a,__int64 b)
{
	return a>b;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int nn,ii;
	int i,j;
	__int64 t;
	scanf("%d",&nn);
	for(int ii=1;ii<=nn;ii++)
	{
		t=0;
		printf("Case #%d: ",ii);
		scanf("%d%d%d",&n,&m,&l);
		for(i=0;i<l;i++)
			scanf("%I64d",&a[i]);
		sort(a,a+l,com);
		for(i=0;i<l;i++)
			t+=(__int64)(i+m)/m*a[i];
		printf("%I64d\n",t);
	}

	return 0;
}