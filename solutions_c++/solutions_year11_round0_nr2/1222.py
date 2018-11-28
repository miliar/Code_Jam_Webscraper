#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string.h>

using namespace std;

bool is_opposite[26];
char opposite[26];
bool vis[26];
char combine[26];
bool is_combined[26];
char a[26][26];

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int t,c,d,n,i,cur,j;
	char ch,hlam;
	char s[150];
	char res[150];
	int kol;
	scanf("%d",&t);
	for (int cnt=1;cnt<=t;cnt++)
	{
		memset(is_opposite,false,sizeof(is_opposite));
		memset(vis,false,sizeof(vis));
		memset(is_combined,false,sizeof(is_combined));
		scanf("%d",&c);
		for (i=0;i<c;i++)
		{
			scanf("%s",s);
			is_combined[s[0]-'A']=true;
			is_combined[s[1]-'A']=true;
			combine[s[0]-'A']=s[1];
			combine[s[1]-'A']=s[0];
			a[s[0]-'A'][s[1]-'A']=s[2];
			a[s[1]-'A'][s[0]-'A']=s[2];
		}
		scanf("%d",&d);
		for (i=0;i<d;i++)
		{
			scanf("%s",s);
			is_opposite[s[0]-'A']=true;
			is_opposite[s[1]-'A']=true;
			opposite[s[0]-'A']=s[1];
			opposite[s[1]-'A']=s[0];
		}
		scanf("%d",&n);
		scanf("%s",s);
		kol=0;
		for (i=0;i<n;i++)
		{	
			cur=s[i]-'A';
			if (kol==0)
			{
				res[kol++]=s[i];
				vis[cur]=true;
				continue;
			}
			if (is_combined[cur] && (res[kol-1]==combine[cur]))
			{
				res[kol-1]=a[cur][combine[cur]-'A'];
				memset(vis,false,sizeof(vis));
				for (j=0;j<kol;j++)
					vis[res[j]-'A']=true;
				continue;
			}
			if (is_opposite[cur] && vis[opposite[cur]-'A'])
			{
				kol=0;
				memset(vis,false,sizeof(vis));
				continue;
			}
			res[kol++]=s[i];
			vis[cur]=true;
		}
		printf("Case #%d: [",cnt,res);
		for (i=0;i<kol-1;i++)
			printf("%c, ",res[i]);
		if (kol>0) printf("%c",res[kol-1]);
		printf("]\n");
	}
	return 0;
}