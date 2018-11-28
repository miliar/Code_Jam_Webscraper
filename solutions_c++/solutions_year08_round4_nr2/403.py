#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <math.h>
#include <map>
#include <set>

using namespace std;

#define max(a, b) a > b ? a : b
#define min(a, b) a < b ? a : b
#define fr(i, n) for(i = 0; i < n; i++)
#define frd(i, n) for(i = n-1; i >= 0; i--)
#define lo(i, a, b) for(i = a; i < b; i++)
#define lod(i, a, b) for(i = a; i > b; i--)

#define pb push_back
#define Max 10000

#define Eps 1e-09
#define Inf 0x7fffffff

typedef vector <int> vi;
typedef vector <vi > vvi;
typedef pair <int, int> ii;

FILE *inf = fopen("B.in", "r"), *outf = fopen("B.out", "w");

int Prime[ Max], P;
int N, M, A;
int Have[ Max], Count[ Max], Limit[ Max], H;

void setting()
{
	int i, j;

	Prime[1] = 2;
	P = 1;

	for(i = 3; i <= Max; i+=2)
	{
		for(j = 1; j <= P; j++)
		{
			if( i % Prime[j] == 0)
				break;
		}

		if(j > P)
		{
			P++;
			Prime[ P] = i;
		}
	}
}

void input()
{
	fscanf(inf, "%d%d%d", &N, &M, &A);
}

void work(int x)
{
/*
	H = 0;

	lo(i, 1, (P+1))
	{
		if( A % Prime[i] == 0)
		{
			Have[ H] = Prime[i];
			Limit[ H] = 0;

			while( A % Prime[i] == 0)
			{
				A /= Prime[i];
				Limit[ H]++;
			}

			H++;
		}
	}*/
	
	int i, j, k, l;
	int p, q, r, m;
	int su;

	fprintf(outf, "Case #%d:", x);

	lo(i, 1, (N+1))
	{
		lo(j, 1, (M+1))
		{
			if( i * j < A)
				continue;

			// Case 1

			lo(k, 1, (i+1))
			{
				su = A + (i-k)*j;
				if(su % i != 0)
					continue;

				l = su / i;

				if(su > k*j)
					continue;

				p = i, q = j, r = k, m = j - l;
				break;
			}

			if(k != i+1)
				break;

			// Case 2

			lo(k, 1, i)
			{
				su = i*j - A;
				if(su % k != 0)
					continue;

				l = su / k;
				if(l <= 0 || l >= j)
					continue;

				p = k, q = j, r = i, m = l;
				break;
			}
			if(k != i+1)
				break;

			// Case 3

			if( i*j == A)
			{
				p = 0, q = j, r = i, m = 0;
				break;
			}
		}

		if(j != M+1)
			break;
	}

	if(i == N+1)
		fprintf(outf, " IMPOSSIBLE\n");
	else
		fprintf(outf, " 0 0 %d %d %d %d\n", p, q, r, m);
}

int main()
{
	int i, T;
	fscanf(inf, "%d", &T);
//	setting();

	fr(i, T)
	{
		input();
		work(i+1);
	}
	return 0;
}