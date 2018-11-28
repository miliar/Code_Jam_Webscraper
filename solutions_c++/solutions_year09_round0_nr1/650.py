#include <iostream>
using namespace std;
int L,D,N;
char trie[5001][20];
char test[100000];
int main()
{
	int cnt;
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	while(scanf("%d %d %d",&L,&D,&N)!=EOF)
	{
		for(int i=0;i<D;i++)
			scanf("%s",trie[i]);
		for(int i=0;i<N;i++)
		{
			scanf("%s",test);
			cnt=0;
			for(int j=0;j<D;j++)
			{
				int p=0;
				int k;
				for(k=0;k<L;k++)
				{
					if(test[p]==trie[j][k])p++;
					else
					{
						if(test[p]=='(')
						{
							p++;
							while(test[p]!=')')
							{
								if(test[p]!=trie[j][k])p++;
								else break;
							}
							if(test[p]==')')break;
							else 
							{
								while(test[p]!=')')p++;
								p++;
							}
						}
						else break;
					}
				}
				if(k>=L)cnt++;
			}
			printf("Case #%d: %d\n",i+1,cnt);
		}
	}
	return 0;
}