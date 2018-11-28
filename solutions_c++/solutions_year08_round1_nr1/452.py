#include<iostream>
#include<algorithm>
using namespace std;

__int64 a[1024];
__int64 b[1024];

__int64 s;

int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("1.out","w",stdout);
	__int64 i,j,k,n,num,seq;
	scanf("%I64d",&num);
	for(seq=1;seq<=num;seq++)
	{
		scanf(" %I64d",&n);
		for(i=1;i<=n;i++)
			scanf("%I64d",&a[i]);
		for(i=1;i<=n;i++)
			scanf("%I64d",&b[i]);
		sort(a+1,a+n+1);
		sort(b+1,b+n+1);
		s=0;
		for(i=1;i<=n;i++)
			s+=a[i]*b[n+1-i];
		printf("Case #%I64d: %I64d\n",seq,s);
	}
	return 0;
}