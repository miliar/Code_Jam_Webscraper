#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;

int	main()
{
	int	T , Tnow = 0;
	scanf("%d" , &T);
	while (T)
	{
		Tnow ++;
		T --;
		int	R , K , N;
		scanf("%d%d%d" , &R , &K , &N);

		int	a[1001];
		vector <int> b;
		vector <__int64> pay;
		int mark[1001];
		memset(a , 0 , sizeof(a));
		memset(mark , 0 , sizeof(mark));

		for (int i = 1; i <= N; i ++) scanf("%d" , &a[i]);
		b.push_back(1);
		mark[1] = 1;
		int	flag;

		while (1)
		{
			int i = b[b.size() - 1] , j = i;
			__int64 sum = a[i];

			while (sum <= K)
			{
				j = j % N + 1;
				sum += a[j];
				if (j == i) break;
			}
			sum -= a[j];
			pay.push_back(sum);

			if (mark[j])
			{
				for (flag = 0; flag < b.size(); flag ++)
					if (b[flag] == j) break;
				break;
			}
			mark[j] = 1;
			b.push_back(j);
		}

		__int64	ret = 0;
		if (R < flag + 1)
		{
			for (int i = 0; i < R; i ++)
				ret += pay[i];
		}
		else
		{
			for (int i = 0; i < flag; i ++)
				ret += pay[i];
			__int64 total = 0;
			for (int i = flag; i < b.size(); i ++)
				total += pay[i];
			ret += total * ((R - flag) / (b.size() - flag));
			for (int i = flag; i < flag + ((R - flag) % (b.size() - flag)); i ++)
				ret += pay[i];
		}
		printf("Case #%d: %I64d\n" , Tnow , ret);
	}
}
