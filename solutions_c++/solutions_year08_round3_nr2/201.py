#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <cmath>

using namespace std;

__int64 atoi64(string::iterator first, string::iterator last)
{
	__int64 i=0;
	for (string::iterator it=first;it!=last;it++)
	{
		i = i*10+(*it-'0');
	}
	return i;
}

bool is_ugly(__int64 n)
{
	return n==0 || n%2==0 || n%3==0 || n%5==0 || n%7==0;
}

int fn(string::iterator first, string::iterator last, __int64 num)
{
	int cnt = is_ugly(num + atoi64(first, last)) ? 1 : 0;

	for (string::iterator it = first+1;it != last;++it)
	{
		__int64 n = atoi64(first, it);

		cnt += fn(it, last, num + n);
		cnt += fn(it, last, num - n);
	}

	return cnt;
}

int main()
{
	int N;
	scanf("%d\n", &N);
	for (int i = 0;i<N;i++)
	{
		char str[64];
		gets(str);
		string d = str;

		int c = fn(d.begin(), d.end(), 0);

		printf("Case #%d: %d\n", i+1, c);
	}

	return 0;
}
