#include <stdio.h>
#define LIMITE 2000

int total;
//int f[2][LIMITE+5][17];
int n;
int arreglo[17];
int t;

int max(int a, int b)
{
	if (a > b)
		return a;
	return b;
}



int f(int i, int j, int cuantos)
{
	if (cuantos == n)
		return -1000000000;
	if (cuantos == 0 && (i == n))
		return -1000000000;
	if (i == n)
	{
		if ((j^total) == j)
		{
			//printf("r%d\n", j);
			return 0;
		}
		else
		{
			return -1000000000;
		}
	}
	return max(f(i+1, j, cuantos), f(i+1, j^arreglo[i+1], cuantos+1) + arreglo[i+1]);

}

int k(int i, int a, int b, int cuantos)
{
	if (cuantos == n)
		return -10000;
	if ((cuantos == 0) && (i == n))
		return -123213;
	if ((i == n) && (a == b))
		return 0;
	if ((i == n) && (a != b))
		return -10000;


	return max(k(i+1, a^arreglo[i+1], b, cuantos + 1) + arreglo[i+1], k(i+1, a, b^arreglo[i+1], cuantos));
}

int main()
{
	FILE * ent, * sal;

	ent = fopen("input.txt", "r");
	sal = fopen("output.txt", "w");

	fscanf(ent, "%d", &t);
	for (int caso = 1; caso <= t; caso++)
	{
		fscanf(ent, "%d", &n);
		for(int i = 1; i <= n; i++)
		{
			fscanf(ent, "%d", &arreglo[i]);
			total ^= arreglo[i];
		}
		int res = f(0, 0, 0);
		//int res = k(0, 0, 0, 0);
		if (res < 0)
			fprintf(sal, "Case #%d: NO\n", caso);
		else
			fprintf(sal, "Case #%d: %d\n", caso, res);
		total = 0;
	}
	return 0;
}


