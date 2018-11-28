#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<string>
#include<queue>
#include<stack>

using namespace std;

#define inf (1<<29)
#define mem(a,b) memset(a,(b),sizeof(a))
#define Max(a,b) ((a) > (b) ? (a) : (b))
#define Min(a,b)  ((a) < (b) ? (a) : (b))

char combine[150][150];
char opp[150][150];

int main()
{
	freopen("magic2.in","r",stdin);
	freopen("magic2.out","w",stdout);
	int t,cs = 0,c,d,n,i,j;
	char s[105];
	scanf("%d",&t);
	while(t--)
	{
		vector<char> now;
		memset(combine,0,sizeof(combine));
		memset(opp,0,sizeof(opp));
		scanf("%d",&c);
		while(c--)
		{
			scanf("%s",s);
			combine[s[0]][s[1]] = s[2];
			combine[s[1]][s[0]] = s[2];
		}
		scanf("%d",&d);
		while(d--)
		{
			scanf("%s",s);
			opp[s[0]][s[1]] = 1;
			opp[s[1]][s[0]] = 1;
		}
		scanf("%d",&n);
		scanf("%s",s);
		
		for(i=0;i<n;i++)
		{
			if(now.size()==0)	
			{
				now.push_back(s[i]);
				continue;
			}
			now.push_back(s[i]);
			j = now.size();
			if(combine[now[j-2]][now[j-1]])
			{
				char v = combine[now[j-2]][now[j-1]];
				now.pop_back();
				now.pop_back();
				now.push_back(v);
				continue;
			}
			
			char v = now[j-1];
			for(j=0;j<now.size();j++)
				if(opp[now[j]][v])
				{
					now.clear();
					break;
				}
		}

		printf("Case #%d: [",++cs);
		if(now.size()>0)
			printf("%c",now[0]);
		for(i=1;i<now.size();i++)
			printf(", %c",now[i]);
		printf("]\n");
	}
	return 0;
}