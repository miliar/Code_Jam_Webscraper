#include <cstdio>
#include <algorithm>

using namespace std;

int L,D,N;

char slova[5005][20];
char s[600];
int mam[20][30];

int main()
{
	scanf("%d%d%d",&L,&D,&N);
	for(int i=0;i<D;++i)
	{
		scanf("%s",slova[i]);
	}
	for(int t=1;t<=N;++t)
	{
		memset(mam,0,sizeof mam);
		scanf("%s",s);
		for(int i=0,j=0;i<L;++i)
		{
			if (s[j]=='(')
			{
				++j;
				while(s[j]!=')')
				{
					mam[i][s[j++]-'a']=1;
				}
				++j;
			}
			else
			{
				mam[i][s[j++]-'a']=1;
			}
		}
		int pocet=0;
		for(int i=0;i<D;++i)
		{
			int ok=1;
			for(int j=0;j<L;++j)
			{
				if (mam[j][slova[i][j]-'a']==0)
				{
					ok=0;
					break;
				}
			}
			pocet+=ok;
		}
		printf("Case #%d: %d\n",t,pocet);
	}
	return 0;
}
