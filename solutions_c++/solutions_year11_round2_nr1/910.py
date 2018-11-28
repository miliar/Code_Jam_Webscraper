#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<queue>
#include<vector>
#define MAXL 110
using namespace std;

int main()
{
	int T;
	int t = 0;
	int win,total,count;
	int i,j,k,N;
	bool flag;
	double temp;
	double WP[MAXL];
	double OWP[MAXL];
	double OOWP[MAXL];
	char s[MAXL][MAXL];
	freopen("A-large.in","r",stdin);
	freopen("A-large.txt","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&N);
		for(i=0;i<N;i++)
			scanf("%s",s[i]);
		for(i=0;i<N;i++)
		{
			win = 0;
			total = 0;
			for(j=0;j<N;j++)
			{
				if(s[i][j] == '1')
				{
					win++;
					total++;
				}
				else if(s[i][j] == '0')
					total++;
			}
			WP[i] = ( (double)win) / total;
		}
	
		for(i=0;i<N;i++)
		{
			count = 0;
			temp = 0.0;
			for(j=0;j<N;j++)
			{
				win = 0;
				total = 0;
				flag = false;
				if(i == j)
					continue;
				for(k=0;k<N;k++)
				{
					if(i == k)
					{
						if(s[j][k] == '.')
						{
							flag = true;
							break;
						}
						else
						{
							count++;
							continue;
						}
					}
					if(s[j][k] == '1')
					{
						win++;
						total++;
					}
					else if(s[j][k] == '0')
						total++;
				}
				if(flag == false)
				{
					temp += ( ( (double)win) / total );
				//	printf("hu %d %lf\n",j,temp);
				//	system("pause");
				}
			}
			OWP[i] = temp / (double)count;
		}
		for(i=0;i<N;i++)
		{
			count = 0;
			temp = 0.0;
			for(j=0;j<N;j++)
			{
				if(s[i][j] != '.')
				{
					temp += OWP[j];
					count++;
				}
			}
			OOWP[i] = temp / count;
		}
		
		printf("Case #%d:\n",++t);
		for(i=0;i<N;i++)
		{
			printf("%lf\n",0.25*WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]);
		}
		
	}
	return 0;
}
/*
4
.11.
0.00
01.1
.10.
*/
