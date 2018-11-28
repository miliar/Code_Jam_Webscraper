#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <ctime>
#include <algorithm>
#include <iostream>

using namespace std;

int data[1005] = {1,2,3,4,-3};

int comp(int a, int b)
{
	return a > b;
}

int main()
{

//////////////////////////////////////////////////////////////////////////


	int N;
	scanf("%d", &N);
	
	for (int i = 1; i <= N; ++i)
	{
		int P, K, L;
		scanf("%d%d%d", &P, &K, &L);

		bool pp = L <= P*K;
		
		int ret = 0;

		if (pp)
		{
			memset(data, 0, sizeof(data));

			for (int j = 0; j < L; ++j)
			{
				scanf("%d", &data[j]);
			}

			sort(data, data + L, comp);

			
			int level = 1;

			int pt = 0;
			while (pt < L)
			{
				for (int k = 0; k < K && pt +k <L; ++k)
				{
					ret += data[pt +k]*level;
				}

				pt += K;
				level++;
			}

			printf("Case #%d: %d\n",i, ret);
		}
		else
			printf("Case #%d: ------------------------------------\n", i);

	}

	
//////////////////////////////////////////////////////////////////////////
	long ti2 = clock();
	//cout << ti2 - ti1 << endl;
	return 0;
}