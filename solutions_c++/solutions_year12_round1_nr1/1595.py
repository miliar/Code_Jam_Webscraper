#include<iostream>
#include<cstdio>
using namespace std;

const int MAXA = 99999 + 10;
double p[MAXA];
	int A,B;

double   ExpectedIfKeepType();

double BackNStep(int N);

int main()
{
	freopen("datain.txt", "r", stdin);
	freopen("dataout.txt", "w", stdout);
	int T;
	int i,j;
	double Min;//anawer
	double KeepType;
	double PressEnter;

	//cin>>T;
	scanf("%d", &T);

	for (i=0; i<T; i++)
	{
		//cin>>A>>B;
		scanf("%d%d", &A, &B);

		for (j=0; j<A; j++)
		{
			//cin>>p[j];
			scanf("%lf", &p[j]);
		}

		KeepType = ExpectedIfKeepType();
		Min = KeepType;

		PressEnter = B + 2;

		if (PressEnter < Min)
		{
			Min = PressEnter;
		}

		for(j=1; j<=A; j++)
		{
			double Tmp = BackNStep(j);
			if (Tmp < Min)
			{
				Min = Tmp;
			}
		}
		printf("Case #%d: ", i + 1);
		printf("%.6lf\n", Min);
	}

	return 0;
}

double   ExpectedIfKeepType()
{
	int i;
	double Answer;
	double pAllRight = 1.0;

	for (i=0; i<A; i++)
	{
		pAllRight *= p[i];
	}

	Answer = pAllRight * (B - A + 1);
	Answer += (1 - pAllRight) * (2 * B + 2 - A);
	return Answer;
}

double BackNStep(int N)
{
	double Answer;
	double pBeforeNAllRight = 1.0;
	int i;

	for (i=0; i<A-N; i++)
	{
		pBeforeNAllRight *= p[i];
	}

	Answer = pBeforeNAllRight * ( 2 * N + B + 1 - A);
	Answer += (1 - pBeforeNAllRight) * (2 * N + 2 * B + 2 - A);

	return Answer;
}