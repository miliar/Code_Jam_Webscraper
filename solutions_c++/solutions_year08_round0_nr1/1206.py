#include <map>
#include <string>
#include <cstdio>
using namespace std;
#define REP(i,a)for(int i=0;i<(a);i++)

int T,S,Q;
char s[2000];
bool em[100];
map<string,int> no;

int main()
{
	freopen("A.in","r",stdin);freopen("A.out","w",stdout);
	scanf("%d",&T);
	REP(i,T)
	{
		no.clear();
		scanf("%d",&S);gets(s);
		REP(j,S)
		{
			gets(s);
			no[s]=j;
		}
		scanf("%d",&Q);gets(s);
		memset(em,0,sizeof(em));
		int cnt=0,ans=0;
		REP(j,Q)
		{
			gets(s);
			if(no.find(s)!=no.end())
			{
				int w=no[s];
				if(!em[w])
				{
					cnt++;
					if(cnt==S)
					{
						memset(em,0,sizeof(em));
						ans++;
						cnt=1;
					}
					em[w]=1;
				}
			}
		}
		printf("Case #%d: %d\n",i+1,ans);
	}
	return 0;
}
