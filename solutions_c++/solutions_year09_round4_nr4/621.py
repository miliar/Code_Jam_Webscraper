#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double run1()
{
	int X, Y, R;
	scanf("%d%d%d", &X, &Y, &R);
	return R;
}

double run2()
{
	int X1, Y1, R1, X2, Y2, R2;
	scanf("%d%d%d%d%d%d", &X1, &Y1, &R1, &X2, &Y2, &R2);
	return __max(R1, R2);
}

double calc3(int X1, int Y1, int R1, int X2, int Y2, int R2, int X3, int Y3, int R3)
{
	return __max(R1, (sqrt((double)((X2-X3)*(X2-X3)+(Y2-Y3)*(Y2-Y3)))+R2+R3)/2);
}

double run3()
{
	int X1, Y1, R1, X2, Y2, R2, X3, Y3, R3;
	scanf("%d%d%d%d%d%d%d%d%d", &X1, &Y1, &R1, &X2, &Y2, &R2, &X3, &Y3, &R3);
	double r1 = calc3(X1, Y1, R1, X2, Y2, R2, X3, Y3, R3);
	double r2 = calc3(X2, Y2, R2, X3, Y3, R3, X1, Y1, R1);
	double r3 = calc3(X3, Y3, R3, X1, Y1, R1, X2, Y2, R2);
	double r = __min(r1, r2);
	return __min(r, r3);
}

double run()
{
	int N;
	scanf("%d", &N);
	switch (N)
	{
	case 1:
		return run1();
	case 2:
		return run2();
	case 3:
		return run3();
	}
	return 0.0;
}

int main()
{
	int C;
	scanf("%d", &C);
	for (int i = 1; i <= C; i++)
	{
		printf("Case #%d: %.6f\n", i, run());
	}
	return 0;
}