
#include <stdio.h>
#include <vector>


double WP[100]={0};
double OWP[100]={0};
double OOWP[100]={0};

char *pMatch = NULL;


char getMatch(int teamA , int teamB, int teamNum)
{
	return pMatch[teamA*teamNum + teamB];
}

int main(int argc, char* argv[])
{

	freopen("c:\\input.in","r",stdin);
	freopen("C:\\output.txt","w",stdout);

	int T = 0;

	scanf("%d", &T);

	for(int t = 0 ; t < T ; t++)
	{
		long long N = 0 ;
		scanf("%d", &N);

		pMatch = new char[N*N];
		memset(pMatch, 0, N*N*sizeof(char));
		int *pTotalWin = new int[N];
		memset(pTotalWin, 0, N*sizeof(int));

		int *pTotalGame = new int[N];
		memset(pTotalGame, 0, N*sizeof(int));

		char str[101] = {0};

		char* ptrMatchSlot = pMatch;
		for(int i = 0 ; i < N ;i++)
		{
			scanf("%s", str);
			for(int j = 0 ; j < N ; j++)
			{
				if (str[j]=='1')
				{
					pTotalGame[i]++;
					pTotalWin[i]++;
					*ptrMatchSlot = 2;
				}
				else if(str[j]=='0')
				{
					pTotalGame[i]++;
					*ptrMatchSlot = 1;
				}
				else{
					*ptrMatchSlot = 0;
				}
				ptrMatchSlot++;
			}
		}

		for(int i =0 ; i < N ; i++)
		{
			WP[i] = (double)(pTotalWin[i])/(double)(pTotalGame[i]);

			//OWP
			OWP[i] = 0;
			int OWPCount = 0;
			for(int j = 0 ; j < N ; j++)
			{
				char matRet = getMatch(j,i, N);
				if( matRet )
				{
					if(matRet == 2)
						OWP[i]+= ((double)(pTotalWin[j] - 1) / (double)(pTotalGame[j]-1));
					else
						OWP[i]+= ((double)(pTotalWin[j]) / (double)(pTotalGame[j]-1));
					OWPCount++;
				}
			}
			OWP[i] /= OWPCount;
		}

		//OOWP
		for(int i =0 ; i < N ; i++)
		{
			OOWP[i] = 0;
			for(int j = 0 ; j < N ; j++)
			{
				if(getMatch(i, j, N))
				{
					OOWP[i]+=OWP[j];
				}
			}
			OOWP[i] /= pTotalGame[i];
		}



		printf("Case #%d:\n", t+1);
		for(int i = 0 ; i < N ; i++)
		{
			double r = (WP[i] + OWP[i] + OWP[i] + OOWP[i])/4 ;
			printf("%lf\n", r);
		}

		delete [] pMatch;
		delete [] pTotalWin;
		delete [] pTotalGame;
	}

	return 0;
}