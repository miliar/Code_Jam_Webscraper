#include <cstdio>
#include <algorithm>
using namespace std;

char S[40];

void Solve(int test)
{
	scanf("%s", S);
	int n = 0;
	while(S[n])
		n++;
	printf("Case #%d: ", test);
	if(next_permutation(S, S + n))
		puts(S);
	else
	{
		S[n] = '0';
		n++;
		S[n] = 0;
		for(int i = 0; i < n; ++i)
			if(S[i] == '0')
				continue;
			else if(S[i] < S[0] || S[0] == '0')
				swap(S[i], S[0]);
		sort(S + 1, S + n);
		puts(S);
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i)
		Solve(i);
	return 0;
}