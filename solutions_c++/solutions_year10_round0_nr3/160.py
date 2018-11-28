#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

const int maxn = 1000 + 1;

int	main()
{
	int	T , now = 0;
	scanf("%d" , &T);
	while (T)
	{
		now ++;
		T --;
		int	R , K , N;
		scanf("%d%d%d" , &R , &K , &N);

		int	a		[maxn];
		vector <int> b;
		vector <__int64> money;
		bool	mark		[maxn];
		memset(a , 0 , sizeof(a));
		memset(mark , false , sizeof(mark));

		for (int i = 1; i <= N; i ++) scanf("%d" , &a[i]);
		b.push_back(1);
		mark[1] = true;
		int	flag;

		while (true)
		{
			int i = b[b.size() - 1];
			int j = i;
			__int64 s = a[i];
			while (s <= K)
			{
				j = j % N + 1;
				s += a[j];
				if (j == i) break;
			}
			s -= a[j];
			money.push_back(s);
			if (mark[j])
			{
				for (flag = 0; flag < b.size(); flag ++)
					if (b[flag] == j) break;
				break;
			}
			mark[j] = true;
			b.push_back(j);
		}

		__int64	res = 0;
		if (R < flag + 1)
		{
			for (int i = 0; i < R; i ++) res += money[i];
		}
		else
		{
			for (int i = 0; i < flag; i ++) res += money[i];
			__int64 tot = 0;
			for (int i = flag; i < b.size(); i ++) tot += money[i];
			res += tot * ((R - flag) / (b.size() - flag));
			for (int i = flag; i < flag + ((R - flag) % (b.size() - flag)); i ++) res += money[i];
		}
		printf("Case #%d: %I64d\n" , now , res);
	}
}
