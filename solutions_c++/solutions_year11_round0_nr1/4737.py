#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
void main()
{
	int T=0;
	
	int N=0;
	char R;


	bool flag[2]={false};
    freopen("c:/A-large.in","r",stdin);
    freopen("c:/out.txt","w",stdout);
	scanf("%d",&T);
    for(int i=0;i<T;i++)
	{
		int Bp=1;
    	int Op=1;
    	int temp=0;
    	int By=0;
    	int Oy=0;
		int BB=0;
		int OB=0;
    	int y=0;
		//int P[2][100]={0};
		scanf("%d",&N);
		for(int j=0;j<N;j++)
		{
			scanf("%s",&R);
			switch(R)
			{
			case 'B':
			{
				scanf("%d",&temp);
				By+=abs(temp-Bp);
				if(By<=OB)
				{
					By=OB+1;
					BB=By;
				}
				else
				{
					By=By+1;
				    BB=By;
				}
				y=By;
				Bp=temp;
				break;
			}
			case 'O':
			{
				scanf("%d",&temp);
				Oy+=abs(temp-Op);
				if(Oy<=BB)
				{
					OB=BB+1;
					Oy=OB;
				}
				else
				{
					Oy=Oy+1;
				    OB=Oy;
				}
				y=Oy;
				Op=temp;
				break;
			}
			}


		}

	    printf("Case #%d:",i+1);
		printf(" %d\n",y);
	}

}