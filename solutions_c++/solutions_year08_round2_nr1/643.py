#define _CRT_SECURE_NO_WARNINGS

#include "stdlib.h"
#include <list>
#include <string>
#include <vector>

#define INPUT "A-small-attempt2.in"
#define OUTPUT "A-small-attempt2.out"
//#define INPUT "A-test.in"
//#define OUTPUT "A-test.out"


struct COORD
{
	unsigned __int64 x;
	unsigned __int64 y;
};


void parseTrees(std::vector<COORD> &v, unsigned __int64 n, unsigned __int64 A, unsigned __int64 B, unsigned __int64 C, unsigned __int64 D, unsigned __int64 x0, unsigned __int64 y0, unsigned __int64 M)
{
COORD c;
unsigned __int64 X, Y;

	v.clear();

	X = x0;
	Y = y0;
	c.x = X;
	c.y = Y;
	v.push_back(c);
	//printf("(%I64d %I64d) ", c.x, c.y);
	for(int i = 1; i < n; i++)
	{
		X = (A * X + B) % M;
		Y = (C * Y + D) % M;
		c.x = X;
		c.y = Y;
		v.push_back(c);
		//printf("(%I64d %I64d) ", c.x, c.y);
	}
}

bool isDivisible(unsigned __int64 n)
{
unsigned __int64 sum;

	sum = 0;
	while(n != 0)
	{
		sum+=(n%10);
		n = n/10;
	}

	if(sum < 10)
		return ((sum == 0) || (sum == 3) || (sum == 6) || (sum == 9));
	else
		return isDivisible(sum);
}

bool validCenter(COORD c1, COORD c2, COORD c3)
{
	return (isDivisible(c1.x+c2.x+c3.x) && isDivisible(c1.y+c2.y+c3.y));
}

bool findinvec(std::vector<int>&v, int n)
{
	for(int i=0; i < v.size(); i++)
		if(n == v[i])
			return true;

	return false;
}


unsigned __int64 calc(std::vector<COORD> v)
{
std::vector<int> used;
int sz = v.size();
unsigned __int64 total = 0;

	for(int i=0; i < sz; i++)
	{
		for(int j=i+1; j < sz; j++)
		{
			for(int k=j+1; k < sz; k++)
			{
				//if(findinvec(used, i) || findinvec(used, j) || findinvec(used, k))
				//	continue;

				if(validCenter(v[i], v[j], v[k]))
				{
					//printf("%d, %d, %d\n", i, j, k);
					//printf("valid: (%I64d %I64d) (%I64d %I64d) (%I64d %I64d)\n", v[i].x, v[i].y, v[j].x, v[j].y, v[k].x, v[k].y);
					used.push_back(i);
					used.push_back(j);
					used.push_back(k);
					total++;
				}
			}
		}
	}
	return total;
}

void main(void)
{
FILE* fpIn;
FILE* fpOut;
char line[1024];
unsigned int N;
unsigned int i;
int n, A, B, C, D, x0, y0, M;
std::vector<COORD> trees;
unsigned __int64 answer;

	// Abre arquivos
	fpIn = fopen(INPUT, "rb");
	fpOut = fopen(OUTPUT, "wb");

	// Lê numero de casos
	N = atoi(fgets(line, 1024, fpIn));

	// Loop nos casos
	for(i=0; i < N; i++)
	{
		// Lê parametros para cada caso
		fgets(line, 1024, fpIn);
		sscanf(line, "%d %d %d %d %d %d %d %d", &n, &A, &B, &C, &D, &x0, &y0, &M);
		parseTrees(trees, n, A, B, C, D, x0, y0, M);

		// Processa parametros
		answer = calc(trees);

		// Imprime saída no arquivo e no prompt
		printf("Case #%d: %I64d\r\n", i+1, answer);
		fprintf(fpOut, "Case #%d: %I64d\n", i+1, answer);
	}

	// Fecha arquivos
	fclose(fpIn);
	fclose(fpOut);
}

