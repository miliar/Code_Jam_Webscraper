#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
typedef __int64 int64;

int cs,cn=1;
int a[102],b[105];
int n,m;

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("c-out.txt","w",stdout);
	int i,j;
	scanf("%d",&cs);
	while(cs--)
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<m;i++) scanf("%d",&b[i]);
		sort(b,b+m);
		int ans = 987654321;
		do
		{
			int tt = 0;
			for(i=1;i<=n;i++) a[i] = 1;
			for(i=0;i<m;i++)
			{
				a[b[i]] = 0;
				for(j=b[i]-1;j>=1;j--)
					if(a[j])
						tt++;
					else break;
				for(j=b[i]+1;j<=n;j++)
					if(a[j])
						tt++;
					else break;
			}
			if(tt < ans) ans = tt;
		}while(next_permutation(b,b+m));
		printf("Case #%d: %d\n",cn++,ans);
	}
	return 0;
}

