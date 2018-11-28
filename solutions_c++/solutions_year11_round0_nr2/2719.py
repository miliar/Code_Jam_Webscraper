#include <stdio.h>
#include <vector>
#include <string>
using namespace std;
const int maxn=1000;
int cb[maxn][maxn];
int num[maxn];
string op[maxn];
int main()
{	
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++)
	{
		for(int i='A';i<='Z';i++)
		for(int j='A';j<='Z';j++)
		cb[i][j]=-1;
		for(int i='A';i<='Z';i++)
		num[i]=0;
		int m,n,l;
		scanf("%d",&m);
		for(int i=1;i<=m;i++)
		{
			char s[10];
			scanf("%s",s);
			cb[s[0]][s[1]]=s[2];
			cb[s[1]][s[0]]=s[2];
		}
		
		for(int i='A';i<='Z';i++)
		{
			op[i].clear();
		}
		scanf("%d",&n);
		for(int i=1;i<=n;i++)
		{
			char s[10];
			scanf("%s",s);
			op[s[0]].push_back(s[1]);
			op[s[1]].push_back(s[0]);			
		}
		scanf("%d",&l);
		char s[10000];
		scanf("%s",s);
		char tmp[10000];
		int tail=0;
		for(int i=0;i<l;i++)
		{
			tmp[tail++]=s[i];
			num[s[i]]++;
			while(1)
			{
				if(tail>=2&&cb[tmp[tail-1]][tmp[tail-2]]!=-1)
				{
					num[tmp[tail-1]]--;
					num[tmp[tail-2]]--;
					num[cb[tmp[tail-1]][tmp[tail-2]]]++;
					
					tmp[tail-2]=cb[tmp[tail-1]][tmp[tail-2]];
					tail--;
				}
				else 
				{
					bool flag=false;
					if(tail>0)
					for(int i=0;i<op[tmp[tail-1]].size();i++)
					{
						if(num[op[tmp[tail-1]][i]]>0)
						{
							flag=true;
							break;
						}
					}
					
					if(flag)
					{
						for(int i='A';i<='Z';i++)num[i]=0;
						tail=0;
					}
					break;
				}
			}
		}	
		tmp[tail]='\0';
		printf("Case #%d: [",cas);
		for(int i=0;i<tail-1;i++)
		printf("%c, ",tmp[i]);
		if(tail>0)printf("%c",tmp[tail-1]);
		printf("]\n");				
	}
}
