#include <cstdio>
#include <vector>

using namespace std;

int N, L;
long long t;

int buff[1010000];

int mas[1010000];

long long Solve(vector<int> sbIndex)
{
	long long res = 0;
	for (int i=0; i<N; i++)
	{
		bool sb = false;
		for (int k=0; k<sbIndex.size(); k++)
		{
			if (sbIndex[k] == i)
				sb = true;
		}
		if (sb)
		{
			long long leftT = t-res;
			if (leftT <= 0)
			{
				res += mas[i];
			}
			else
			{
				if (leftT >= mas[i]*2)
				{
					res += mas[i]*2;
				}
				else
				{
					res += leftT;
					res += mas[i]-(leftT/2);
				}
			}
		}
		else
		{
			res += mas[i]*2;
		}
	}
	return res;
}


int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int tt=1; tt<=T; tt++)
	{
		int C;
		scanf("%d%lld%d%d", &L, &t, &N, &C);
		for (int i=0; i<C; i++)
		{
			scanf("%d", &buff[i]);
		}
		int index = 0;
		for (int i=0; i<N; i++)
		{
			mas[i] = buff[index];
			index++;
			if (index >= C)
				index = 0;
		}

		long long locRes;
		long long res = 10000000;
		res *= res;
		res *= 10;
		
		vector<int> v;
		if (L >= 1)
		{
			for (int i=0; i<N; i++)
			{
				v.push_back(i);
				if (L == 2)
				{
					for (int j=i+1; j<N; j++)
					{
						v.push_back(j);
						locRes = Solve(v);
						if (locRes < res)
							res = locRes;
						v.pop_back();
					}
				}
				locRes = Solve(v);
				if (locRes < res)
					res = locRes;
				v.pop_back();
			}
		}
		locRes = Solve(v);
		if (locRes < res)
			res = locRes;
		printf("Case #%d: %lld\n", tt, res);
	}
	return 0;
}