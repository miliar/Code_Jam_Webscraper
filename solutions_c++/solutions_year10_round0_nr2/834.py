#include <iostream>
using namespace std;

int buf[100];
int cmp(const void *a,const void *b)
{
	return *(int *)b-*(int *)a;
}

int gcd(int a,int b)
{
	return b==0 ? a : gcd(b,a%b);
}

int main(void)
{
	freopen("fair.in","r",stdin);
	freopen("fair.out","w",stdout);
	int t;
	cin>>t;
	for(int m=1;m<=t;m++)
	{
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%d",&buf[i]);
		}
		qsort(buf,n,sizeof(int),cmp);
		int g=buf[0]-buf[1];
		for(int i=1;i<n-1;i++)
		{
			g=gcd(g,buf[i]-buf[i+1]);
		}
		int p=-buf[n-1];
		p=(p%g+g)%g;
		printf("Case #%d: %d\n",m,p);
	}
	return 0;
}