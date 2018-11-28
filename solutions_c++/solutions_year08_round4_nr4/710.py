#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int t,k,i,j,n,p[20],nr,minim;
char a[60001],b[60001];
int main()
{
	freopen("Input.in","r",stdin);
	freopen("Output.out","w",stdout);
	scanf("%d ",&t);
	for(k=1;k<=t;k++)
	{
		scanf("%d %s",&n,a);
		for(i=1;i<=n;i++)
			p[i]=i;
		j=strlen(a);
		minim=j;
		do
		{
			nr=0;
			for(i=0;i<j;i++)
			{
				b[i]=a[ (i/n)*n + p[(i%n)+1] - 1];
				if(i==0 || b[i]!=b[i-1]) nr++;
			}
			if(minim>nr) minim=nr;				
		}while(next_permutation(&p[1],&p[n+1]));
		printf("Case #%d: %d\n",k,minim);
	}
	fclose(stdout);
	return 0;
}