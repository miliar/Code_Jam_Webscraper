#include <iostream>
using namespace std;

char Map[100][100];
char roteMap[100][100];
char graveMap[100][100];
int flag[100];
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int t,i,j;
	int p,q;
	int N,K;
	scanf("%d",&t);
	for (i=1;i<=t;i++)
	{
		scanf("%d%d",&N,&K);
		for (j=0;j<N;j++)
		{
			scanf("%s",&Map[j]);
		}
		for (p=0;p<N;p++)
		{
			for (q=0;q<N;q++)
			{
				graveMap[p][q]='.';
				roteMap[p][q]=Map[N-1-q][p];
			}
		}
		for (p=0;p<N;p++)
		{
			flag[p]=N-1;
		}
		for (q=0;q<N;q++)
		{
			for (p=N-1;p>=0;p--)
			{
				if (roteMap[p][q]!='.')
				{
					graveMap[flag[q]--][q]=roteMap[p][q];
				}				
			}
		}
		bool reg=false,blue=false;
		int numreg,numblue;
		int s;
		for (p=0;p<N;p++)
		{
			for (q=0;q<N;q++)
			{
				if (graveMap[p][q]=='B')
				{
					numblue=1;
					for (s=q+1;s<N;s++)
					{
						if (graveMap[p][s]==graveMap[p][q])
						{
							numblue++;
						}
						else break;
					}
					if (numblue>=K)
					{
						blue=true;
					}
					numblue=1;
					for (s=p+1;s<N;s++)
					{
						if (graveMap[s][q]==graveMap[p][q])
						{
							numblue++;
						}
						else break;
					}
					if (numblue>=K)
					{
						blue=true;
					}
					numblue=1;
					for (s=1;s<N;s++)
					{
						if (p+s<N&&q+s<N&&graveMap[p+s][q+s]==graveMap[p][q])
						{
							numblue++;
						}
						else break;
					}
					if (numblue>=K)
					{
						blue=true;
					}
					numblue=1;
					for (s=1;s<N;s++)
					{
						if (p+s<N&&q-s>=0&&graveMap[p+s][q-s]==graveMap[p][q])
						{
							numblue++;
						}
						else break;
					}
					if (numblue>=K)
					{
						blue=true;
					}
				}
				else if (graveMap[p][q]=='R')
				{
					numreg=1;
					for (s=q+1;s<N;s++)
					{
						if (graveMap[p][s]==graveMap[p][q])
						{
							numreg++;
						}
						else break;
					}
					if (numreg>=K)
					{
						reg=true;
					}
					numreg=1;
					for (s=p+1;s<N;s++)
					{
						if (graveMap[s][q]==graveMap[p][q])
						{
							numreg++;
						}
						else break;
					}
					if (numreg>=K)
					{
						reg=true;
					}
					numreg=1;
					for (s=1;s<N;s++)
					{
						if (p+s<N&&q+s<N&&graveMap[p+s][q+s]==graveMap[p][q])
						{
							numreg++;
						}
						else break;
					}
					if (numreg>=K)
					{
						reg=true;
					}
					numreg=1;
					for (s=1;s<N;s++)
					{
						if (p+s<N&&q-s>=0&&graveMap[p+s][q-s]==graveMap[p][q])
						{
							numreg++;
						}
						else break;
					}
					if (numreg>=K)
					{
						blue=true;
					}
				}
			}
		}

		
		if (reg&&blue)
		{
			printf("Case #%d: Both\n",i);
		}
		else if (reg)
		{
			printf("Case #%d: Red\n",i);

		}
		else if (blue)
		{
			printf("Case #%d: Blue\n",i);
		}
		else printf("Case #%d: Neither\n",i);		
	}
	return 0;	
}