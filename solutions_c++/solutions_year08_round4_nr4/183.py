#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstring>

using namespace std;

template <class T>
inline const T& TMIN(const T& x, const T& y)
{ return (y<x ? y : x); }

void main()
{
	char buff[60000];
	char perm[60000];

	int N;
	gets(buff);
	sscanf(buff, "%d", &N);

	int permarray[16];
	for(int n = 1; n <= N; n++)
	{
		printf("Case #%d: ", n);

		int k;
		gets(buff);
		sscanf(buff, "%d", &k);

		gets(buff);

		int len = strlen(buff);

		int cnt = 1;
		for(int i=1; i< len; i++)
		{
			if(buff[i]!=buff[i-1])
			{
				cnt++;
			}
		}

		int aa[16]={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};

		while(next_permutation(aa, aa+k))
		{
			int newcnt = 1;

			for(int j = 0; j < len; j+=k)
			{
				for(int jj = 0; jj < k; jj++)
				{
					perm[j+jj] = buff[j+aa[jj]];
				}
			}
			for(int i = 1; i < len; i++)
			{
				if(perm[i] != perm[i-1])
				{
					newcnt++;
				}
			}

			cnt = TMIN(cnt, newcnt);
		}

		printf("%d\n", cnt);
	}
}
