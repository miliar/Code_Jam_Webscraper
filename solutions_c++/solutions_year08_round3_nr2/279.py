#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstdlib>
#include <cstring>

using namespace std;

vector<long long> members;
vector<int> primes;
long long result = 0;
string s;

const int PLUS = 0;
const int MINUS = 1;

inline int isUgly(long long num)
{
	if (num == 0)
	{
		return true;
	}
	if (num < 0)
	{
		num = - num;
	}

	for (int i = 0; i < (int)primes.size(); ++i)
	{
		if ((num % primes[i]) == 0)
		{
			return 1;
		}
	}

	return 0;
}

inline long long parse(string &s)
{
	long long factor = 1;
	long long ret = 0;
	for (int i = s.size() - 1; i >= 0; --i)
	{
		ret += (s[i] - '0') * factor;
		factor *= 10;
	}
	return ret;
}

void solve(long long val, int pos)
{
	if (pos == members.size())
	{
		result += isUgly(val);
		return;
	}

	solve(val + members[pos], pos + 1);
	solve(val - members[pos], pos + 1);
}

int main()
{
	int C;
	cin >> C;

	int caseNum = 1;

	primes.push_back(2);

	long long k = 10;
	for(long long i = 3; i <= k; ++i)   
	{   
		bool flag = false;
		int sk = sqrt(double(i)); 
		for(int j = 2; j <= sk; ++j)   
		{   
			if(i % j == 0)   
			{   
				flag = true;
				break;
			}   
		}   
		if(!flag)
		{   
			primes.push_back(i); 
		}   
	}

	do
	{
		cin >> s;

		result = 0;
		int first = 0;
		int sign = PLUS;
		for (long long i = 0; i < 1 << (s.size() - 1); ++i)
		{
			vector<int> poses;
			for (int j = 0; j < s.size() - 1; ++j)
			{
				if ((i & (1 << j)))
				{
					poses.push_back(j + 1);
				}
			}
			members.clear();
			int start = 0;
			for (int j = 0; j < poses.size(); ++j)
			{
				members.push_back(parse(s.substr(start, poses[j] - start)));
				start = poses[j];
			}
			members.push_back(parse(s.substr(start, s.size() - start)));
			solve(members[0], 1);
		}

		printf("Case #%d: %ld\n", caseNum++, result);
	} while (caseNum <= C);

	return 0;
}

