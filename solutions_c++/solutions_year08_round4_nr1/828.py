/*
	Problem		::	A
	Date		::	2nd August, 2008
	Author		::	MIB
	Environment	::	Microsoft Visual Studio 2005
*/

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>

using namespace std;

typedef __int64 i64;
const int INF = 0x7F7F7F7F;

int R, C;

#define mini(x,y) ((x)<(y)?(x):(y))
#define maxi(x,y) ((x)>(y)?(x):(y))
#define valid(x,y) ((x)>=0 && (x)<R && (y)>=0 && (y)<C)
#define CLR(x, v) memset((x), (v), sizeof((x)))


class compare_desc
{
	public:
	bool operator () (const int &obj1, const int &obj2)
	{
		return obj1 > obj2;	
	}
};


const int MAX = 10005;

int store[MAX][2];
int num[MAX], change[MAX];
int nn, nl;


void compute(int n)
{
	if(n > nn)
	{
		if(num[n] == 0)
		{
			store[n][0] = 0;
			store[n][1] = -2;
		}

		else
		{
			store[n][1] = 0;
			store[n][0] = -2;
		}

		return;
	}

	if(store[n][0] == -1 || store[n][1] == -1)
	{
		compute(2*n);
		compute(2*n + 1);
		
		int r1, r2;


		if(num[n] == 1)
		{
			if(store[2*n][0] < 0 && store[2*n+1][0] < 0)
			{
				r1 = -2;
			}
			else
			{
				if(store[2*n][0] < 0)
					r1 = store[2*n+1][0];
				else if(store[2*n+1][0] < 0)
					r1 = store[2*n][0];
				else
					r1 = mini(store[2*n][0], store[2*n+1][0]);
			}

			if(change[n] == 1)
			{

				if(store[2*n][0] < 0 || store[2*n+1][0] < 0)
				{
					r2 = -2;
				}
				else
				{
					r2 = store[2*n][0] + store[2*n+1][0];
				}
			}
			else
				r2 = -2;


			if(r1 < 0 && r2 < 0)
				store[n][0] = -2;
			else
			{
				if(r1 < 0)
					store[n][0] = r2 + 1;
				else if(r2 < 0)
					store[n][0] = r1;
				else
					store[n][0] = mini(r1, r2+1);
			}


			if(store[2*n][1] < 0 || store[2*n+1][1] < 0)
			{
				r1 = -2;
			}
			else
			{
				r1 = store[2*n][1] + store[2*n+1][1];
			}


			if(change[n] == 1)
			{
				if(store[2*n][1] < 0 && store[2*n+1][1] < 0)
				{
					r2 = -2;
				}
				else
				{
					if(store[2*n][1] < 0)
						r2 = store[2*n+1][1];
					else if(store[2*n+1][1] < 0)
						r2 = store[2*n][1];
					else
						r2 = mini(store[2*n][1], store[2*n+1][1]);
				}
			}
			else
				r2 = -2;


			if(r1 < 0 && r2 < 0)
				store[n][1] = -2;
			else
			{
				if(r1 < 0)
					store[n][1] = r2 + 1;
				else if(r2 < 0)
					store[n][1] = r1;
				else
					store[n][1] = mini(r1, r2+1);
			}

		}

		else
		{
			if(store[2*n][1] < 0 && store[2*n+1][1] < 0)
			{
				r1 = -2;
			}
			else
			{
				if(store[2*n][1] < 0)
					r1 = store[2*n+1][1];
				else if(store[2*n+1][1] < 0)
					r1 = store[2*n][1];
				else
					r1 = mini(store[2*n][1], store[2*n+1][1]);
			}

			if(change[n] == 1)
			{
				if(store[2*n][1] < 0 || store[2*n+1][1] < 0)
				{
					r2 = -2;
				}
				else
				{
					r2 = store[2*n][1] + store[2*n+1][1];
				}
			}
			else
				r2 = -2;

			if(r1 < 0 && r2 < 0)
				store[n][1] = -2;
			else
			{
				if(r1 < 0)
					store[n][1] = r2 + 1;
				else if(r2 < 0)
					store[n][1] = r1;
				else
					store[n][1] = mini(r1, r2+1);
			}



			if(store[2*n][0] < 0 || store[2*n+1][0] < 0)
			{
				r1 = -2;
			}
			else
			{
				r1 = store[2*n][0] + store[2*n+1][0];
			}


			if(change[n] == 1)
			{
				if(store[2*n][0] < 0 && store[2*n+1][0] < 0)
				{
					r2 = -2;
				}
				else
				{
					if(store[2*n][0] < 0)
						r2 = store[2*n+1][0];
					else if(store[2*n+1][0] < 0)
						r2 = store[2*n][0];
					else
						r2 = mini(store[2*n][0], store[2*n+1][0]);
				}
			}
			else
				r2 = -2;

			if(r1 < 0 && r2 < 0)
				store[n][0] = -2;
			else
			{
				if(r1 < 0)
					store[n][0] = r2 + 1;
				else if(r2 < 0)
					store[n][0] = r1;
				else
					store[n][0] = mini(r1, r2+1);
			}

		}

	}

	return;
}

int main(void)
{
	// freopen( "..//..//codejam//A-large.in", "rt", stdin );
	// freopen( "..//..//codejam//A-large.out", "wt", stdout );

	int t, test;
	int i, M, V;

	scanf( " %d" ,&test);

	for(t=1; t<=test; t++)
	{
		CLR(store, -1);

		scanf( " %d %d" ,&M ,&V);

		nn = (M-1)/2;
		nl = (M+1)/2;

		for(i=1; i<=nn; i++)
		{
			scanf( " %d %d" ,&num[i], &change[i]);
		}

		for(i; i<=M; i++)
			scanf( " %d" ,&num[i]);

		compute(1);

		if(store[1][V] < 0)
			printf( "Case #%d: IMPOSSIBLE\n" ,t);	
		else
			printf( "Case #%d: %d\n" ,t ,store[1][V]);	
	}

	return 0;
}