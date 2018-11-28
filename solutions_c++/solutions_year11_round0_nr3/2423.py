#include <cstdio>
#include <algorithm>
void work(int i)
{
	int n,a,x,z,s;
	scanf("%d%d",&n,&a);
	x=z=s=a;
	while (--n)
	{
		scanf("%d",&a);
		x^=a;
		z=std::min(z, a);
		s=s+a;
	}
	printf("Case #%d: ",i);
	if (x)
		printf("NO\n");
	else
		printf("%d\n",s-z);
}

int main()
{
	int n;
	scanf("%d", &n);
	for (int i=1;i<= n;i++)
		work(i);
}
