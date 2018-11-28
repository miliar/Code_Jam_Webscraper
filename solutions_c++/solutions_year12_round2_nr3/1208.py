#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int N;
int mas[600];

vector<int> findSum(vector<int> s, int sum)
{
	vector<int> result;
	int M = s.size();

	int cs = 0;
	for (int i=0; i<M; i++)
	{
		cs += s[i];
	}
	if (cs < sum)
		return result;

	for (int i=1; i<(1<<M); i++)
	{
		int curSum = 0;
		int mask = i;
		int index = 0;
		result.clear();
		while(mask)
		{
			if (mask & 1)
			{
				curSum += s[index];
				if (curSum > sum)
					break;
				result.push_back(s[index]);
			}
			mask >>= 1;
			index++;
		}
		if (mask)
			return vector<int>();
		if (mask == 0 && curSum == sum)
			return result;
	}
	return vector<int>();
}

pair<vector<int>, vector<int> > run()
{
	pair<vector<int>, vector<int> > result;

	for (int i=1; i<(1<<N); i++)
	{
		vector<int> f;
		vector<int> s;
		for (int j=0; j<N; j++)
		{
			if (i & (1<<j))
			{
				f.push_back(mas[j]);
			}
			else
			{
				s.push_back(mas[j]);
			}
		}
		int sum = 0;
		for (int i=0; i<f.size(); i++)
		{
			sum += f[i];
		}
		s = findSum(s,sum);
		if (s.size() > 0)
		{
			result.first = f;
			result.second = s;
			return result;
		}
	}

	return result;
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++)
	{
		scanf("%d", &N);
		for (int i=0; i<N; i++)
		{
			scanf("%d", &mas[i]);
		}
		cerr<<t<<endl;
		pair<vector<int>, vector<int> > result = run();

		bool can = true;
		if (result.first.size() == 0)
			can = false;

		printf("Case #%d:\n", t);
		if (can)
		{
			sort(result.first.begin(), result.first.end());
			for (int i=0; i<result.first.size(); i++)
			{
				if (i != 0)
					printf(" ");
				printf("%d", result.first[i]);
			}
			printf("\n");
			sort(result.second.begin(), result.second.end());
			for (int i=0; i<result.second.size(); i++)
			{
				if (i != 0)
					printf(" ");
				printf("%d", result.second[i]);
			}
			printf("\n");
		}
		else
		{
			printf("Impossible\n");
		}
	}
	return 0;
}

