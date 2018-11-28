#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
using namespace std;

#define MEM(t,v) memset((t), (v), sizeof(t))
#define pb push_back
#define sz size()
#define IO freopen("A-small-attempt1.in","r",stdin); freopen("a.out","w",stdout);

#define SIZE 1000

int dig[200];
bool vis[200];
int N;

int main()
{
	IO
	unsigned __int64 ans;
	int tcase,t,i,base,len;
	char num[70];
	scanf("%d",&tcase);
	for(t=1;t<=tcase;t++)
	{
		MEM(dig,0);
		MEM(vis,0);
		scanf("%s",num);
		base=0;
		int d=2;
		len = strlen(num);
		for(i=0;i<len;i++)
		{
			if(!vis[num[i]])
			{
				if(i==0)
					dig[num[i]]=1;
				else if(base==1)
					dig[num[i]]=0;
				else
					dig[num[i]]=d++;
		
				vis[num[i]]=true;
				base++;
			}
		}
		if(base==1)
			base=2;
		ans=0;
		for(i=0;i<len;i++)
		{
			ans += dig[num[i]]*(int)pow(base,len-1-i);
		}

		printf("Case #%d: %I64u\n",t,ans);
	}
	return 0;
}