#include <iostream>
#include <cmath>
using namespace std;
#define MAX 10000

int x[MAX];
int y[MAX];

int main()
{
	int n,t,i,j,k,l,ans;

	freopen("testout.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for (k=1;k<=t;++k)
	{
		scanf("%d",&n);
		for (i=0;i<n;++i) scanf("%d%d",&x[i],&y[i]);
		ans=0;
		for (i=0;i<n;++i)
			for (j=i+1;j<n;++j)
				for (l=j+1;l<n;++l)
					if ((x[i]+x[j]+x[l])%3==0&&(y[i]+y[j]+y[l])%3==0) ans++;
						
		
		printf("Case #%d: %d\n",k,ans);
	}
	return 0;
}

