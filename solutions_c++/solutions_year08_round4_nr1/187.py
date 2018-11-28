#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <string>


using namespace std;

const int INF=1000000;

#define OR 0
#define AND 1
template <class T>
inline const T& TMIN(const T& x, const T& y)
{ return (y<x ? y : x); }

template <class T>
inline const T& TMIN(const T& x, const T& y, const T& z)
{ return (y<x ? TMIN(y,z) : TMIN(x,z)); }

#define MAX_GATE 10000

void main()
{
	int N;
	scanf("%d", &N);

	int gate[MAX_GATE];
	int change[MAX_GATE];
	int one[MAX_GATE];
	int zero[MAX_GATE];

	for(int n = 1; n <= N; n++)
	{
		printf("Case #%d: ", n);

		int M, V;
		scanf("%d %d", &M, &V);

		for(int i = 1; i <= (M-1)/2; i++)
		{
			scanf("%d %d", &gate[i], &change[i]);
		}
		for(int i = (M-1)/2 + 1; i <= M; i++)
		{
			scanf("%d", &gate[i]);
			if(gate[i] == 0)
			{
				one[i] = INF;
				zero[i] = 0;
			}
			else
			{
				one[i] = 0;
				zero[i] = INF;
			}
		}

		for(int j = (M-1)/2; j >= 1; j--)
		{
			if(gate[j] == OR)
			{
				one[j] = TMIN(one[j*2] + one[j*2+1], one[j*2] + zero[j*2+1], zero[j*2] + one[j*2+1]);
				zero[j] = zero[j*2] + zero[j*2+1];

				if(change[j])
				{
					zero[j]= TMIN(zero[j], TMIN(zero[j*2] + zero[j*2+1] , one[j*2] + zero[j*2+1] , zero[j*2] + one[j*2+1]) +1);
				}
			}
			else
			{
				one[j] = one[j*2] + one[j*2+1];
				zero[j] = TMIN(zero[j*2] + zero[j*2+1], one[j*2] + zero[j*2+1], zero[j*2] + one[j*2+1]);

				if(change[j])
				{
					one[j] = TMIN(one[j], TMIN(one[j*2] + one[j*2+1], one[j*2] + zero[j*2+1], zero[j*2] + one[j*2+1]) + 1);
				}
			}
		}

		if(V == 0)
		{
			if(zero[1] >= INF)
			{
				printf("IMPOSSIBLE\n");
			}
			else
			{
				printf("%d\n", zero[1]);
			}
		}
		else
		{
			if(one[1] >= INF)
			{
				printf("IMPOSSIBLE\n");
			}
			else
			{
				printf("%d\n", one[1]);
			}
		}

	}

}
