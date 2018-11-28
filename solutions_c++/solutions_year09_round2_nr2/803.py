#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int cs;
char in[100];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("b-out.txt","w",stdout);
	int i,j,len,cn=1;
	scanf("%d",&cs);
	while(cs--)
	{
		scanf("%s",in);
		len = strlen(in);
		printf("Case #%d: ",cn++);
		if(next_permutation(in,in+len))
		{
			puts(in);
		}
		else
		{
			int mm = 10;
			for(i=0;i<len;i++){
				if(in[i]!='0' && in[i]-'0' < mm) mm = in[i] - '0';
			}
			in[len++] = '0';
			in[len] = '\0';
			sort(in,in+len);
			int vis[100];
			memset(vis,0,sizeof(vis));
			for(i=0;i<len;i++)
			{
				if(in[i]-'0' == mm)
				{
					vis[i] = 1;
					break;
				}
			}
			printf("%d",mm);
			for(i=0;i<len;i++)
			{
				if(!vis[i]) putchar(in[i]);
			}
			puts("");
		}
	}
	return 0;
}

