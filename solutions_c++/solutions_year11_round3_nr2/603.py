// Google Codejam
// May 22, 2011
// Author	::	MIB
// Problem	::	B


#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>


using namespace std;


const int MAX = 1005;

__int64 Cs[MAX];
__int64 dist[MAX];
__int64 L, T1, N, C;
__int64 maxNums[MAX];
bool used[MAX];
int tot;


void getMaxNums(int i1, int j1, __int64 dif)
{
	int i, j, k, k1;

	memset(used, 0, sizeof(used));

	for(i=0; i<L; i++)
	{
		maxNums[i] = dif;
	}

	for(i=i1+1, j=j1+1, k=0; i<N; i++, j++)
	{
		if(j == C)
			j = 0;

		for(k=0; k<L; k++)
		{
			if(Cs[j] > maxNums[k])
			{
				for(k1=k+1; k1<L; k1++)
					maxNums[k1] = maxNums[k1-1];
				maxNums[k] = Cs[j];

				break;
			}
		}
	}

	return;
}

int main(void)
{
	freopen ("C:\\Documents and Settings\\Mainul\\My Documents\\Downloads\\Codejam\\input\\B-small-attempt0.in", "rt", stdin);
	freopen ("C:\\Documents and Settings\\Mainul\\My Documents\\Downloads\\Codejam\\output\\B-small-attempt0.out", "wt", stdout);

	int t, T;
	int i, j, k;
	bool done, found;
	__int64 sum, dif, res;

	scanf(" %d",&T);
	
	for(t=1; t<=T; t++)
	{
		scanf(" %I64d %I64d %I64d %I64d ", &L, &T1, &N, &C);


		for(i=0; i<C; i++)
			scanf(" %I64d" ,&Cs[i]);

		sum = 0;
		tot = 0;
		done = false;

		for(i=0, j=0; i<N; i++, j++)
		{
			if(j == C)
				j = 0;

			dist[i] = Cs[j];

			found = false;

			if(!done && sum + (dist[i]*2) >= T1)
			{
				dif = (sum + (dist[i]*2) - T1) / 2;
				getMaxNums(i, j, dif);
				done = true;

				for(k=0; k<L; k++)
				{
					if(maxNums[k] == dif)
					{
						sum += (dist[i] - dif) * 2;
						sum += dif;
						used[k] = true;
						found = true;
						tot++;
						break;
					}
				}
			}

			else if(tot < L)
			{
				for(k=0; k<L; k++)
				{
					if(maxNums[k] == Cs[j] && !used[k])
					{
						sum += Cs[j];
						used[k] = true;
						found = true;
						tot++;
						break;
					}
				}
			}

			if(!found)
				sum += dist[i] * 2;
		}

		res = sum;

		printf( "Case #%d: %I64d\n", t, res);
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
