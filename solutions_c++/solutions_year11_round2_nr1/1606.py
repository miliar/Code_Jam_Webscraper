#include<cstdio>
#include<cstring>


const int NMAX(100);

char map[NMAX+2][NMAX+2];

double wp[NMAX+2];
double owp[NMAX+2];
double oowp[NMAX+2];
int nWin[NMAX+2];
int nLose[NMAX+2];

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int nTest; scanf("%d",&nTest);
	for(int test=1;test<=nTest;test++)
	{
		int nInput; scanf("%d",&nInput);
		for(int i=1;i<=nInput;i++)
			scanf("%s",map[i]+1);
		for(int i=1;i<=nInput;i++)
		{
			int win(0),lose(0);
			for(int j=1;j<=nInput;j++)
			{
				if(map[i][j]=='1')win++;
				else if (map[i][j]=='0')lose++;
			}
			wp[i] = (double)(win) / (double)(win+lose);
			nWin[i] = win; nLose[i] = lose;
		}
		for(int i=1;i<=nInput;i++)
		{
			double sum(0);
			for(int j=1;j<=nInput;j++)
			{
				if(i!=j)
				{
					if(map[j][i]=='1')
						sum += (double)(nWin[j]-1)/(double)(nWin[j]+nLose[j]-1);
					else if(map[j][i]=='0')
						sum += (double)(nWin[j])/ (double)(nWin[j]+nLose[j]-1);
				}
			}
			owp[i] = sum/(double)(nWin[i]+nLose[i]);
		}
		for(int i=1;i<=nInput;i++)
		{
			double sum(0);
			for(int j=1;j<=nInput;j++)
			{
				if(i!=j && map[i][j]!='.')
				{
					sum += owp[j];
				}
			}
			oowp[i] = sum/(double)(nWin[i]+nLose[i]);
		}
		printf("Case #%d:\n",test);
		//printf("WP====================\n");
		//for(int i=1;i<=nInput;i++)
		//	printf("%c : %lf\n",'A'+i-1,wp[i]);
		//printf("OWP===================\n");
		//for(int i=1;i<=nInput;i++)
		//	printf("%c : %lf\n",'A'+i-1,owp[i]);
		//printf("OOWP==================\n");
		//for(int i=1;i<=nInput;i++)
		//	printf("%c : %lf\n",'A'+i-1,oowp[i]);


		for(int i=1;i<=nInput;i++)
			printf("%lf\n",wp[i]*0.25 + owp[i]*0.50 + oowp[i]*0.25);

	}
	return 0;
}