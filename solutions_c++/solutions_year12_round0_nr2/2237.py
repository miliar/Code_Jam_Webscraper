#include <iostream>
using namespace std;
int T,N,S,P;
int score;
int good, normal;
int main()
{
	freopen("D:\\in.txt","r",stdin);
	freopen("D:\\out.txt","w",stdout);
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		printf("Case #%d: ",i+1);	
		scanf("%d%d%d",&N,&S,&P);
		good=normal=0;
		for(int j=0;j<N;j++)
		{
			scanf("%d",&score);
			if(P>=2)
			{
				if(score>=(3*P-2)) good++;
				else if(score>=(3*P-4)) normal++;
			}
			else if(P==1)
			{
				if(score>=1) good++;
			}
			else
			{
				good++;
			}
		}
		printf("%d\n",good+min(normal,S));
	}
}