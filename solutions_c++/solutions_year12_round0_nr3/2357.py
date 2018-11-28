#include <iostream>
#include <cstdio>
#include <cstring>
#include <windows.h>
#define Max 2000000
#define Limit 10000000
using namespace std;

int T, A, B;
int Next[Limit];

int Rec(int n)
{
	int dec = 1;
	while (dec <= n) dec *= 10;
	dec /= 10;
	do
	{
		n = dec * (n % 10) + n / 10;
	}
	while(n < dec);
	return n;
}

void Init()
{
	for (int i = 0; i <= Limit; i++) Next[i] = -1;
	for (int n = 0; n <= Max; n++)
	{
		int t = n;
		while (Next[t] == -1)
		{
			Next[t] = Rec(t);
			t = Next[t];
		}
	}
}

bool u[Max + 1];

long long Solve()
{
	long long r = 0;
	memset(u, 0, sizeof(u));
	
	for (int i = A; i <= B; i++)
	if (!u[i])
	{
		int t = i, tt = t, n = 0;
		do
		{
			if (A <= t && t <= B)
			{
				n++;
				u[t] = true;
			}
			t = Next[t];
		}
		while(t != tt);
		
		r += (long long)n * (n - 1) / 2;
	}
	
	return r;
}

int main()
{
	//freopen("c-small.txt", "r", stdin);
	
	Init();
	
	cin >> T;
	for (int test = 0; test < T; test++)
	{
		cin >> A >> B;
		printf("Case #%d: %I64d\n", test + 1, Solve());
	}
	
	return 0;
}
