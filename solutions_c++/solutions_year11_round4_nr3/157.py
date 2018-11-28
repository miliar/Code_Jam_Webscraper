#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <vector>
#include <math.h>

using namespace std;


vector <int> pr;


bool IsPrime(int s)
{
	if (s == 1)  return false;
	if (s == 2)  return true;
	for (int i = 0; i < pr.size(); i ++)
	{
		if (s % pr[i] == 0)  return false;
		if (pr[i] * pr[i] > s)  break;
	}
	return true;
}


int MakePrimeList(int lim)
{
	pr.clear();
	if (lim >= 2)  pr.push_back(2);
	if (lim >= 3)  pr.push_back(3);
	for (int x = 1; x < lim; )
	{
		x += 4;  if (x > lim)  break;
		if (IsPrime(x))  pr.push_back(x);
		x += 2;  if (x > lim)  break;
		if (IsPrime(x))  pr.push_back(x);
	}
	return pr.size();
}

long long work()
{
	long long N, ans;
	cin >> N;    ans = 1;
	if (N == 1)  return 0;
	for (int i = 0; i < pr.size() && (long long)(pr[i]) * pr[i] <= N; i ++)
	{
		ans --;
		for (long long z = pr[i]; z <= N; z *= pr[i])
			ans ++;
	}
	return ans;
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	MakePrimeList(1000000);
	int T;
	cin >> T;
	for (int k = 1; k <= T; k ++)
		printf("Case #%d: %I64d\n", k, work());
	return 0;
}