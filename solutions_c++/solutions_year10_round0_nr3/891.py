#include <stdio.h>
#include <vector>

using namespace std;

typedef long long LL;

typedef vector<LL> vint;

vint V;

LL R, N, K;

LL next(LL & x)
{
	LL s = 0;
	LL p = 0;
	while (1)
	{
		if (s + V[x] > K || p == N)
		{
			return s;
		}
		s += V[x];
		++x;
		++p;
		x %= N;
	}
}

LL f()
{
	vint U(N, -1);
	vint Res;
	LL x = 0;
	LL p = 0;
	LL t = 0;
	U[0] = t++;
	while (1)
	{
		LL temp = next(x);
		x %= N;
		if (U[x] != -1) 
		{
			Res.push_back(temp);
			break;
		}
		else	
		{
			Res.push_back(temp);
			U[x] = t++;
		}
	}
	LL temp = 0;
	LL cycle = 0;
	if (R <= Res.size())
	{
		for(int i = 0; i < R; ++i) temp += Res[i];
		return temp;
	}
	for(int i = 0; i < U[x]; ++i) temp += Res[i];
	for(int i = U[x]; i < Res.size(); ++i) cycle += Res[i];
	LL z = (R - U[x]) % (Res.size() - U[x]);
	for(int i = U[x]; i < U[x] + z; ++i) temp += Res[i];
	return temp + (R - U[x]) / (Res.size() - U[x]) * cycle; 

}

int main()
{
	
	freopen("C.in", "r", stdin);
	freopen("1.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; ++i)
	{
		scanf("%I64d%I64d%I64d", &R, &K, &N);
		V.assign(N, 0);
		for(int j = 0; j < N; ++j)
		{
			scanf("%d", &V[j]);
		}
		printf("Case #%d: %I64d\n", i + 1, f());
	}
	return 0;
}