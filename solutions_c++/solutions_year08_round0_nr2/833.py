#include <stdio.h>
#include <string.h>
#include <algorithm>
#define A 0
#define B 1
#define NMAX 101
using namespace std;

struct TimeTable
{
	char departure[6];
	char arrival[6];
	int depN;
	int arrN;
	int dir;
	int flag;
};

int N, NA, NB, T;
int AStart, BStart;
TimeTable stationA[NMAX];
TimeTable stationB[NMAX];

int t2n(char* timeStr)
{
	int h = (timeStr[0]-'0')*10+(timeStr[1]-'0');
	int m = (timeStr[3]-'0')*10+(timeStr[4]-'0');

	return h*60+m;
};

bool cmp(TimeTable ta, TimeTable tb)
{
	return ta.depN < tb.depN;
}

void print()
{
	int i,j;
	for(i=0; i<NA;i++)
	{
		printf("%s %s\n", stationA[i].departure, stationA[i].arrival);
	}

	for(i=0; i<NB;i++)
	{
		printf("%s %s\n", stationB[i].departure, stationB[i].arrival);
	}

}

void init()
{
	scanf("%d", &T);
	scanf("%d %d", &NA, &NB);
	
	int i, j;
	for(i=0; i<NA; i++)
	{
		scanf("%s %s", stationA[i].departure, stationA[i].arrival);
		stationA[i].depN = t2n(stationA[i].departure);
		stationA[i].arrN = t2n(stationA[i].arrival);
		stationA[i].dir = A;
		stationA[i].flag = 0;
	}

	for(i=0; i<NB; i++)
	{
		scanf("%s %s", stationB[i].departure, stationB[i].arrival);
		stationB[i].depN = t2n(stationB[i].departure);
		stationB[i].arrN = t2n(stationB[i].arrival);
		stationB[i].dir = B;
		stationB[i].flag = 0;
	}

	sort(&stationA[0], &stationA[NA], cmp);
	sort(&stationB[0], &stationB[NB], cmp);
}

int solve()
{
	AStart = NA; BStart = NB;
	int ADec = 0, BDec = 0;
	int i,j;

	for(i=0; i<NA; i++)
	{
		for(j=0; j<NB; j++)
		{
			if (!stationB[j].flag && ((stationB[j].arrN + T) <= stationA[i].depN))
			{
				ADec++;
				stationB[j].flag = 1;
				break;
			}
		}		
	}

	for(j=0; j<NB; j++)
	{
		for(i=0; i<NA; i++)
		{
			if (!stationA[i].flag && ((stationA[i].arrN + T) <= stationB[j].depN))
			{
				BDec++;
				stationA[i].flag = 1;
				break;
			}
		}
	}

	AStart -= ADec;
	BStart -= BDec;

	return 0;
}

int main()
{
	freopen("2.in", "r", stdin);
	freopen("2.out", "w", stdout);

	scanf("%d", &N);

	for(int i=0; i<N; i++)
	{
		init();
		solve();

		printf("Case #%d: %d %d\n", i+1, AStart, BStart);

	}

	return 0;
}