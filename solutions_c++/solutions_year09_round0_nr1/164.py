#include <stdio.h>
#include <vector>
using namespace std;
int L,D,N;
char Word[5005][20];
char  Tmp[10000000];
int isAlp[20][26];
int main()
{
	scanf("%d %d %d",&L,&D,&N);
	for (int q=0;q<D;++q)
		scanf("%s",Word[q]);
	for (int kase=1;kase<=N;++kase)
	{
		scanf("%s",Tmp);
		int i=0,open=0;
		for (int q=0;q<L;q++) for (int w=0;w<26;++w)
			isAlp[q][w]=0;
		for (int q=0;Tmp[q];++q)
		{
			switch(Tmp[q])
			{
				case '(':
					open=1;
					break;
				case ')':
					open=0;
					i++;
					break;
				default:
					isAlp[i][Tmp[q]-'a']=1;
					i+=!open;
					break;
			}
		}
		int ret=0;
		for (int q=0;q<D;++q)
		{
			int isGood=1;
			for (int w=0;w<L;++w)
				if ( ! isAlp[w][Word[q][w]-'a'] )
				{
					isGood=0;
					break;
				}
			ret+=isGood;
		}
		printf("Case #%d: %d\n",kase,ret);
	}
	return 0;
}
