#include <iostream>
#include <string>
#include <string.h>
using namespace std;
char map[26][26];
char ans[205];
char ch[105],c;
int num[26];
int a[26][26];
int main()
{
	int i,j,k,n,m,len,t,now,co=1;
	freopen("B-large.in","r",stdin);
	freopen("outb.text","w",stdout);
	scanf("%d",&t);
	while (t--)
	{
		memset(map,0,sizeof(map));
		memset(a,0,sizeof(a));
		memset(num,0,sizeof(num));
		scanf("%d",&n);
		for (i=0;i<n;i++)
		{
			scanf("%s",ch);
			map[ch[0]-'A'][ch[1]-'A']=map[ch[1]-'A'][ch[0]-'A']=ch[2];
		}
		scanf("%d",&m);
		for (i=0;i<m;i++)
		{
			scanf("%s",ch);
			a[ch[0]-'A'][ch[1]-'A']=a[ch[1]-'A'][ch[0]-'A']=1;
		}
		now=0;
		scanf("%d",&len);
		scanf("%c",&c);
		for (i=0;i<len;i++)
		{
			scanf("%c",&c);
			num[c-'A']++;
			ans[now++]=c;
			while (now>=2&&map[ans[now-2]-'A'][ans[now-1]-'A']!=0)
			{
				num[ans[now-2]-'A']--;
				num[ans[now-1]-'A']--;
				num[map[ans[now-2]-'A'][ans[now-1]-'A']-'A']++;
				ans[now-2]=map[ans[now-2]-'A'][ans[now-1]-'A'];now--;
			}
			for (k=0;k<26;k++)
				for (j=0;j<26;j++)
					if (a[k][j]==1&&num[k]*num[j]!=0)
					{
						now=0;
						memset(num,0,sizeof(num));
					}
		}
		printf("Case #%d: [",co++);
		if (now==0)
			printf("]\n");
		else
			for (i=0;i<now;i++)
			{
				printf("%c%c%c",ans[i],i==now-1?']':',',i==now-1?'\n':' ');
			}
	}
	return 0;
}