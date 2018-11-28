#include <iostream>
#include <string.h>
using namespace std;

char s1[101][101];
char s2[1001][101];
int b[1001];
bool f[101];

int main()
{
	freopen("1.in","r",stdin);
	freopen("1o.in","w",stdout);
	int ii,i,j,k,n,nn,m,t;
	scanf("%d\n",&nn);
	for(ii=1;ii<=nn;ii++)
	{
		printf("Case #%d: ",ii);
		scanf("%d\n",&n);
		for(i=1;i<=n;i++)
			gets(s1[i]);
		scanf("%d\n",&m);
		for(i=1;i<=m;i++)
			gets(s2[i]);
		for(j=1;j<=m;j++)
			for(i=1;i<=n;i++)
				if(!strcmp(s1[i],s2[j]))
				{
					b[j]=i;
					break;
				}
		memset(f,0,sizeof(f));
		k=n;
		t=0;
		for(i=1;i<=m;i++)
		{
			if(!f[b[i]])
			{
				f[b[i]]=true;
				k--;
				if(k==0)
				{
					k=n-1;
					memset(f,0,sizeof(f));
					f[b[i]]=true;
					t++;
				}
			}
		}
		printf("%d\n",t);
	}
	return 0;
}