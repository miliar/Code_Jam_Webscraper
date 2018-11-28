#include<stdio.h>
#include<string.h>
#include<string>
#include<map>
#include<algorithm>
using namespace std;

const int N=1001;

map<string,int> hash;

char ch[128];
int a[N],f[N][N];

int main()
{
	int test,n,m,i,j,k,t=1;
	freopen("alarge.txt","r",stdin);
	freopen("alarge.out","w",stdout);
	scanf("%d",&test);
	while (t<=test)
	{
		scanf("%d\n",&n);
		hash.clear();
		for (i=0;i<n;i++)
		{
			gets(ch);
			hash[ch]=i+1;
		}
		scanf("%d\n",&m);
		for (i=0;i<m;i++)
		{
			gets(ch);
			a[i]=hash[ch];
		}
		memset(f,0xff,sizeof(f));
		for (i=1;i<=n;i++) f[0][i]=0;
		f[0][a[0]]=-1;

		for (i=1;i<m;i++)
		 for (j=1;j<=n;j++)
			 if (a[i]!=j)
			 {
				 if (f[i-1][a[i]]>=0)
				  f[i][j]=f[i-1][a[i]]+1;
				 k=f[i-1][j];
				 if (k>=0 && (f[i][j]<0 || k<f[i][j])) 
				  f[i][j]=k;
			 }
		k=10000;
		for (i=1;i<=n;i++)
		if (f[m-1][i]>=0 && f[m-1][i]<k) k=f[m-1][i];
		printf("Case #%d: %d\n",t++,k);
	}
	return 0;
}