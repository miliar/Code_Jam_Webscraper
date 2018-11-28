#include <stdio.h>
#include <string.h>
#include   <bitset>  
using namespace std;
struct node{
bitset<5000> flag;
};
int main()
{
	int L,D,N;
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	while(scanf("%d%d%d",&L,&D,&N)==3)
	{
		char words[5000][16];
		for(int i=0;i<D;i++)
		{
			scanf("%s",words[i]);
		}
		struct node bitflag[15][26];
		for(int i=0;i<D;i++)
		{
			for(int j=0;j<L;j++)
			{
				bitflag[j][words[i][j]-'a'].flag.set(i);
			}
		}
		char patt[1024];
		for(int i=0;i<N;i++)
		{
			scanf("%s",patt);
			int level=0;
			bitset<5000> a;
			for(int j=0;j<strlen(patt);j++)
			{
				if(patt[j]=='(')
				{
					bitset<5000> b;
					j++;
					while(patt[j]!=')')
					{
						b|=bitflag[level][patt[j]-'a'].flag;
						j++;
					}
					if(level==0)
						a=b;
					else
						a&=b;
					level++;
				}
				else
				{
					if(level==0)
						a=bitflag[level][patt[j]-'a'].flag;
					else
						a&=bitflag[level][patt[j]-'a'].flag;
					level++;
				}
			}
			int count=0;
			for(int j=0;j<D;j++)
			{
				if(a.test(j)==true)
					count++;
			}
			printf("Case #%d: %d\n",i+1,count);
		}
	}
	return 0;
}