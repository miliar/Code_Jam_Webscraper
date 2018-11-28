#include <cstdio>
#include <vector>
#include <stack>

#define MAXBASE 10

using namespace std;

void grow(vector<bool>& arr, int minSize)
{
	int newSize = 1;
	while (newSize < minSize)
		newSize <<= 1;
	if ((int)arr.size() < newSize)
		arr.resize(newSize, false);
}

int computeNext(int base, int n)
{
	int next = 0;
	while (n > 0)
	{
		int digit = n % base;
		next += digit * digit;
		n /= base;
	}
	return next;
}

void computeIsHappy(int base, int n, vector<bool>& isKnown, vector<bool>& isHappy)
{
	stack<int> s;
	while ((int)isKnown.size() <= n || !isKnown[n])
	{
		if ((int)isKnown.size() <= n)
		{
			grow(isKnown, n + 1);
			grow(isHappy, n + 1);
		}
		isKnown[n] = true;
		s.push(n);
		n = computeNext(base, n);
	}
	if (isHappy[n])
	{
		while (!s.empty())
		{
			int t = s.top();
			s.pop();
			isHappy[t] = true;
		}
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	vector<vector<bool> > isKnown(MAXBASE + 1);
	vector<vector<bool> > isHappy(MAXBASE + 1);
	for (int base = 2; base <= MAXBASE; ++base)
	{
		isKnown[base].resize(2);
		isKnown[base][1] = true;
		isHappy[base].resize(2);
		isHappy[base][1] = true;
	}
	for (int testcase = 0; testcase < T; ++testcase)
	{
		vector<int> bases;
		do
		{
			int base;
			scanf("%d", &base);
			bases.push_back(base);
		} while (getchar() == ' ');
		int cBases = (int)bases.size();
		for (int n = 2; ; ++n)
		{
			bool found = true;
			for (int i = 0; i < cBases; ++i)
			{
				computeIsHappy(bases[i], n, isKnown[bases[i]], isHappy[bases[i]]);
				if (!isHappy[bases[i]][n])
				{
					found = false;
					break;
				}
			}
			if (found)
			{
				printf("Case #%d: %d\n", testcase + 1, n);
				break;
			}
		}
	}
	return 0;
}
