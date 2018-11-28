#include <cstdio>
using namespace std;

int TypeRest(int n, int a, int mis)
{
	if(mis == 0)
		return n - a + 1;
	else
		return 2 * n - a + 2;
}

int OneBack(int n, int a, int mis)
{
	if(mis <= 1)
		return n - a + 3;
	else
		return 2 * n - a + 4;
}

int TwoBack(int n, int a, int mis)
{
	if(mis <= 3)
		return n - a + 5;
	else
		return 2 * n - a + 6;
}

int Enter(int n)
{
	return n + 2;
}

double comple(double x)
{
	return 1.0 - x;
}

double min(double a, double b)
{
	return (a<b)?a:b;
}

int main()
{
	int iNumTestCases;
	int iTestCaseIndex;
	int iNumTyped;
	int iTotalChars;
	int iToBeTyped;
	int iProbIndex;
	int misind;
	double p[3];
	double c[8];
	int maxmis;
	double e[4];


	scanf("%d", &iNumTestCases);

	for(iTestCaseIndex = 0; iTestCaseIndex < iNumTestCases; iTestCaseIndex++)
	{
		scanf("%d%d", &iNumTyped, &iTotalChars);
		
		p[0] = p[1] = p[2] = 1.0;

		for(iProbIndex = 3 - iNumTyped; iProbIndex < 3; iProbIndex++)
		{
			scanf("%lf", &p[iProbIndex]);
		}

		c[0] = p[0] * p[1] * p[2];
		c[1] = p[0] * p[1] * comple(p[2]);
		c[2] = p[0] * comple(p[1]) * p[2];
		c[3] = p[0] * comple(p[1]) * comple(p[2]);
		c[4] = comple(p[0]) * p[1] * p[2];
		c[5] = comple(p[0]) * p[1] * comple(p[2]);
		c[6] = comple(p[0]) * comple(p[1]) * p[2];
		c[7] = comple(p[0]) * comple(p[1]) * comple(p[2]);

		maxmis = 1 << iNumTyped;

		e[0] = 0;
		for(misind = 0; misind < maxmis; misind++)
		{
			e[0] += TypeRest(iTotalChars, iNumTyped, misind) * c[misind];
		}

		e[1] = 0;
		for(misind = 0; misind < maxmis; misind++)
		{
			e[1] += OneBack(iTotalChars, iNumTyped, misind) * c[misind];
		}

		e[2] = 0;
		for(misind = 0; misind < maxmis; misind++)
		{
			e[2] += TwoBack(iTotalChars, iNumTyped, misind) * c[misind];
		}

		e[3] = 0;
		for(misind = 0; misind < maxmis; misind++)
		{
			e[3] += Enter(iTotalChars) * c[misind];
		}

		printf("Case #%d: %lf\n", iTestCaseIndex + 1, min(min(e[0],e[1]), min(e[2],e[3])));
	}
	return 0;
}