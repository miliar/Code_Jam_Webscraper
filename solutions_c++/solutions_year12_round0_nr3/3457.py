#include <stdio.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <map>
using namespace std;

int getdigit(int x)
{
	int ans;
	for (ans = 0; x; x /= 10)
		ans++;
	return ans;
}

int arrange(int x)
{
	int i, div, mul;
	int digit, re[10];
	digit = getdigit(x);
	for (i = 0, mul = 1; i < digit; i++)
		mul *= 10;
	for (i = 0, div = 1; i < digit; i++)
	{
		re[i] = x % div * mul + x / div;
		div *= 10;
		mul /= 10;
	}
	sort(re, re + digit);
	for (i = 0; i < digit; i++)
		if (getdigit(re[i]) == digit)
			break ;
	return re[i];
}

int main()
{
	//freopen("C-small-attempt0.in","r+",stdin);
	//freopen("C-small-attempt0.out","w+",stdout);
	int ans;
	int t, ctr, A, B;
	map<int, int> M;
	map<int,int>::iterator it;
	for (scanf("%d", &t), ctr = 1; ctr <= t; ctr++)
	{
		ans = 0;
		M.clear();
		for (scanf("%d%d", &A, &B); A <= B; A++)
			M[arrange(A)]++;
		for (it = M.begin(); it != M.end(); it++)
		{
			ans += (it->second) * (it->second - 1) / 2;
		}
		printf("Case #%d: %d\n", ctr, ans);
	}
}