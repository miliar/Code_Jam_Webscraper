#include<iostream>

using namespace std;

#define MAXL 15
#define MAXD 5000
#define MAXN 500

int L,D,N;

char dict[MAXD][MAXL+1];
char pattern[1000];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d%d%d",&L,&D,&N);
	for(int i=0;i<D;i++) scanf("%s",dict[i]);
	for(int i=0;i<N;i++)
	{
		int count = 0;
		scanf("%s",pattern);
		for(int j=0;j<D;j++)
		{
			int ld=0,lp=0;
			bool ok = true;
			while(dict[j][ld]&&pattern[lp])
			{
				if (pattern[lp]!='(')
					if (dict[j][ld]!=pattern[lp]) { ok=false;break; }
					else { ++ld; ++lp; }
				else
				{
					bool got = false;
					while(pattern[lp]!=')')
					{
						if (!got&&dict[j][ld]==pattern[lp]) got=true;
						++lp;
					}
					if (!got) { ok=false;break; }
					++ld; ++lp;
				}
			}

			if (ok) ++count;
		}
		printf("Case #%d: %d\n",i+1,count);
	}

	return 0;
}
