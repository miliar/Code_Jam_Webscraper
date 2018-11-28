#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
typedef __int64 int64;

int cs,cn=1;
int tab[256];
char in[1000];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a-out.txt","w",stdout);
	int i,j;
	scanf("%d",&cs);
	while(cs--)
	{
		scanf("%s",in);
		memset(tab,-1,sizeof(tab));
		int lb = 0;
		tab[in[0]] = 1;
		for(i=0;in[i];i++)
		{
			if(tab[in[i]] == -1)
			{
				tab[in[i]] = lb++;
				if(lb == 1) lb++;
			}
		}
		if(lb == 0) lb = 2;
		int len = strlen(in);
		int64 ans = 0,c = 1;
		for(i=len-1;i>=0;i--)
		{
			ans += tab[in[i]] * c;
			c *= lb;
		}
		printf("Case #%d: %I64d\n",cn++,ans);
	}
	return 0;
}

