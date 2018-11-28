//#pragma comment(linker, "/STACK:10000000")
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <iostream>
#include <stack>
#include <queue>
#include <cmath>
using namespace std;
typedef long long lint;

int P[10];
char S[1111];
int K;
char X[1111];

void EIter(int x)
{
	for(int k = 0; k < K; ++k)
	{
		X[x + k] = S[x + P[k]];
	}
}
void Enc()
{
	for(int i = 0; S[i]; i += K)
		EIter(i);
}
int CalcGroups()
{
	int ret = 1;
	for(int i = 1; S[i]; ++i)
		if(X[i] != X[i - 1])
			ret++;
	return ret;
}

bool Solve(int test)
{
	scanf("%d %s", &K, S);
	int ans = 1 << 20;
	for(int i = 0; i < K; ++i)
		P[i] = i;
	do
	{
		Enc();
		ans = min(ans, CalcGroups());
	}
	while(next_permutation(P, P + K));
	printf("Case #%d: %d\n", test, ans);
	return true;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("inputD.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t = 0;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i)
		Solve(i);
	//while(Solve(++t));
	return 0;
}