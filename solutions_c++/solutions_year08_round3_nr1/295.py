/*
	Probelm :: A
	Microsoft VS 2005
*/

#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

typedef __int64 i64;

const int MAX = 1005;

i64 num[MAX];

int main(void)
{
	// freopen("..//..//A-large.in", "rt", stdin);
	// freopen("..//..//A-large.out", "wt", stdout);


	int test, t;
	i64 i, j, m, n;
	i64 P, K, L, res;

	scanf( " %d" ,&test);

	for(t=1; t<=test; t++)
	{
		scanf( " %I64d %I64d %I64d" ,&P ,&K ,&L);

		for(i=0; i<L; i++)
		{
			scanf( " %I64d" ,&num[i]);
			num[i] = -num[i];
		}

		sort(num, num+L);
		
		res = 0;
		m = 0;
		n = 1;

		for(i=0; i<L; i++)
		{
			num[i] = -num[i];

			if(m < K)
			{
				res += num[i] * n;
				m++;

				if(m == K)
				{
					m = 0;
					n++;
				}
			}
		}
	
		printf("Case #%d: %I64d\n" ,t ,res);
	}

	return 0;
}