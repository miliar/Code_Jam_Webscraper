#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
using namespace std;
char to[26][26];
int in[26];
bool op[26][26];
char s[1000],ans[1000];
int main()
{
	freopen("large.in","r",stdin);
	freopen("large.out","w",stdout);
	int _,cas=0;
	scanf("%d",&_);
	while(_--)
	{
		memset(in,0,sizeof(in));
		memset(to,0,sizeof(to));
		memset(op,0,sizeof(op));
		int c,d,n;
		scanf("%d",&c);
		for(int i=0;i<c;i++)
		{
			scanf("%s",s);
			to[s[0]-'A'][s[1]-'A']=s[2];
			to[s[1]-'A'][s[0]-'A']=s[2];
		}
		scanf("%d",&d);
		for(int i=0;i<d;i++)
		{
			scanf("%s",s);
			op[s[0]-'A'][s[1]-'A']=true;
			op[s[1]-'A'][s[0]-'A']=true;
		}
		scanf("%d%s",&n,s);
		int top=0;
		for(int i=0;i<n;i++)
		{
			if(top&&to[s[i]-'A'][ans[top-1]-'A']!=0)
			{
				in[ans[top-1]-'A']--;
				ans[top-1]=to[s[i]-'A'][ans[top-1]-'A'];
			}
			else
			{
				bool dis=false;
				for(int j=0;j<26;j++)
				{
					if(in[j]&&op[j][s[i]-'A'])
					{
						dis=true;
						top=0;
						memset(in,0,sizeof(in));
						break;
					}
				}
				if(!dis)
				{
					ans[top++]=s[i];
					in[s[i]-'A']++;
				}
			}
		}
		printf("Case #%d: [",++cas);
		for(int i=0;i<top;i++)
		{
			if(i) printf(", ");
			printf("%c",ans[i]);
		}
		puts("]");
	}
	return 0;
}
