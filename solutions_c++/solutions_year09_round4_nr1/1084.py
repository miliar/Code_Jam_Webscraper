#include<cstdio>
using namespace std;
int i[1000],v[1000];
char str[1000];
int main()
{
	int a,s,d,n,sum;
int T,X;
scanf("%d",&T);
for(X=1;X<=T;X++)
{
	printf("Case #%d: ",X);
	scanf("%d",&n);
	for(a=0;a<n;a++)
	{
		scanf("%s",str);
		for(s=n-1;s>=0;s--) if( str[s]=='1' ) break;
		i[a]=s;
	}
	for(a=0;a<n;a++) v[a]=0;
	sum=0;
	for(a=0;a<n;a++)
	{
		for(s=0;s<n;s++)
		{
			if( v[s]==0 && i[s]<=a )
			{
				sum+=s;
				for(d=0;d<s;d++) sum-=v[d];
				v[s]=1;
				break;
			}
		}
	}
	printf("%d\n",sum);
}
	return 0;
}
