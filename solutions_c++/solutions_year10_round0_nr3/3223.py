#include <stdio.h>
#include <math.h>

int main()
{
	//freopen("in.in","r",stdin);freopen("out.out","w",stdout);
	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
//	freopen("C-small-attempt1.in","r",stdin);freopen("C-small-attempt1.out","w",stdout);
//	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
	int testcase = 0;
	scanf("%d",&testcase);
	for (int caseId=1; caseId<=testcase; caseId++)
	{
		int R = 0; // raz za den
		int k = 0; // mest
		int N = 0; // kol-vo
		scanf("%d %d %d", &R, &k, &N);

		int* queue = new int[N];

		for (int i = 0; i < N; i++)
		{
			scanf("%d", &queue[i]);
		}

		int tail = 0;
		int money = 0;

		for (int NRaz = 0; NRaz < R; NRaz++)
		{
			int FreePlace = k;
			int endQueue = N;
			do
			{
				if (((FreePlace - queue[tail]) >= 0) && (endQueue > 0))
				{
					money += queue[tail];
					
					FreePlace -= queue[tail];

					tail = (tail+1)%N;

					endQueue--;
				}
				else
					break;
			}while(true);
		}

		printf("Case #%d: %d\n", caseId, money);

		delete [] queue;
	}

	return 0;
}