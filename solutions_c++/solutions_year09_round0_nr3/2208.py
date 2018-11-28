#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

#pragma comment(linker, "/STACK:50000000")
string t, s;
int k, n, N;
char c[10000];
int res[600][100];

int f(int l, int r)
{
	if (r >= k)
		return 1;

	if (l >= n)
		return 0;
	
	if (res[l][r] == -1)
	{
		res[l][r] = 0;
		if (s[l] == t[r])
		{
			res[l][r] = ((f(l+1, r+1)%10000) + (f(l+1, r)%10000))%10000;
		}
		else
			res[l][r] = (f(l+1, r))%10000;
	}

	return res[l][r];
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	t = "welcome to code jam";
	k = t.size();

	scanf("%d\n", &N);

	for (int i = 1; i <= N; i++)
	{
		gets(c);
		s = string(c);
		n = s.size();

		memset(res, -1, sizeof res);
		
		int r = f(0, 0);
		cout << "Case #" << i << ": ";
		cout << r/1000;
		r %= 1000;
		cout << r/100;
		r %= 100;
		cout << r/10 << r%10 << endl;
	}

	return 0;
}