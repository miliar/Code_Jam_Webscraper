#include <cstdio>
#include <vector>
#include <memory>
#include <algorithm>

using namespace std;

int res = -1;
vector<int> vec;

int Add(int a, int b)
{
	int res = 0;
	int step = 0;
	while(a != 0 || b != 0)
	{
		int aadd = a&1;
		int badd = b&1;
		int add = (aadd+badd)&1;
		res += (add<<step);
		a >>= 1;
		b >>= 1;
		step++;
	}
	return res;
}

void Input()
{
	res = -1;
	vec.clear();
	int N;
	scanf("%d", &N);
	for (int i=0; i<N; i++)
	{
		int a;
		scanf("%d", &a);
		vec.push_back(a);
	}
}

void Solve()
{
	int N = vec.size();
	int UP = 1<<N;
	int best = -1;
	for (int i=0; i<UP; i++)
	{
		int first = i;
		int second = (UP-1)&(~first);
		if (first == 0 || second == 0)
			continue;

		int a = first;
		int curSum = 0;
		int index = 0;
		while (a)
		{
			if (a&1)
				curSum += vec[index];
			a >>= 1;
			index++;
		}

		if (curSum <= best)
			continue;

		int sumFirst = 0;
		index = 0;
		a = first;
		while (a)
		{
			if (a&1)
				sumFirst = Add(sumFirst, vec[index]);
			a >>= 1;
			index++;
		}
		int sumSecond = 0;
		index = 0;
		a = second;
		while (a)
		{
			if (a&1)
				sumFirst = Add(sumFirst, vec[index]);
			a >>= 1;
			index++;
		}
		if (sumFirst == sumSecond)
		{
			best = curSum;
		}
	}
	res = best;
}


void SolveLarge()
{
	int xor = 0;
	for (int i=0; i<vec.size(); i++)
	{
		xor ^= vec[i];
	}
	if (xor != 0)
		return;

	sort(vec.begin(), vec.end());
	for (int i=1; i<vec.size(); i++)
	{
		res += vec[i];
	}
	res++;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++)
	{
		Input();
		SolveLarge();
		if (res == -1)
			printf("Case #%d: NO\n", t);
		else
			printf("Case #%d: %d\n", t, res);
	}
	return 0;
}