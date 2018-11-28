#include<stdio.h>

using namespace std;

int data[100][100];
int sumWin[100][2];
double OWP[100];
double OOWP[100];

int main()
{
	int T;
	scanf("%d",&T);
	for(int t = 1;t<=T;t++)
	{
		int N;
		scanf("%d",&N);
		//input
		for(int i=0;i<N;i++)
		{
			sumWin[i][0] = sumWin[i][1] = 0;
			char temp[200];
			scanf("%s",temp);
			for(int j=0;j<N;j++)
				if(temp[j] == '.')
					data[i][j] = -1;
				else if(temp[j] == '1')
				{
					data[i][j] = 1;
					sumWin[i][0]++;
					sumWin[i][1]++;
				}
				else
				{
					data[i][j] = 0;
					sumWin[i][1]++;
				}
		}		
		//process
		for(int i=0;i<N;i++)
		{
			double sumWP = 0;
			for(int j=0;j<N;j++)
				if(data[i][j] == 0)
				{
					sumWP += (sumWin[j][0]-1)/(double)(sumWin[j][1]-1);
				} 
				else if(data[i][j] == 1)
				{
					sumWP += (sumWin[j][0])/(double)(sumWin[j][1]-1);
				}
			//printf("--%.12f--",sumWP);
			OWP[i] = sumWP/(1.0*sumWin[i][1]);
			//printf("--%.12f--",OWP[i]);
		}
		for(int i=0;i<N;i++)
		{
			double sumOWP = 0;
			for(int j=0;j<N;j++)
				if(data[i][j] != -1)
					sumOWP += OWP[j];
			OOWP[i] = sumOWP/(1.0*sumWin[i][1]);
		}
		printf("Case #%d:\n",t);
		for(int i=0;i<N;i++)
		{
			//printf("%.12f %.12f %.12f\n",sumWin[i][0]/(double)(sumWin[i][1]),OWP[i],OOWP[i]);
			printf("%.12f\n",0.25*sumWin[i][0]/(double)(sumWin[i][1]) + 0.5*OWP[i] + 0.25 * OOWP[i]);
		}
	}
	return 0;
}
