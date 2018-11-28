#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <deque>
#include <math.h>

using namespace std;

long long int divis(long long int s)
{
	if (s <= 2)
	{
		return s;
	}
	--s;
	if (s % 2 == 0)
	{
		s /= 2;
	}
	else
	{
		s /= 2;
		++s;
	}
	return divis(s) + 1;
}

long long int LoadTests(long long int P, long long int L, long long int C)
{
	long long int s = 0;
	while (P * C < L)
	{
		P *= C;
		++s;
	}
	return divis(s);
}

int main()
{
	freopen("B.in", "rt", stdin);
	freopen("B.out", "wt", stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		long long int P, L, C;
		cin >> P >> L >> C;
		cout << "Case #" << i + 1 << ": " << LoadTests(P, L, C) << endl;
	}
	return 0;
}
	
	
	
