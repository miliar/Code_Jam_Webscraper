#include <cstdio>
#include <vector>
using namespace std;

#define INPUT "A-large.in"
#define OUTPUT "A-large.out"
#define NMAX 100

int max(int a, int b)
{
	return a > b ? a : b;
}

int abs(int a)
{
	return a < 0 ? -a : a;
}

int solve()
{
	char C[NMAX];
	int P[NMAX], n;
	vector<int> O, B;

	scanf("%d", &n);
	for(int i = 0; i < n; ++i)
	{
		scanf(" %c%d", C + i, P + i);
		if(C[i] == 'O')
			O.push_back(P[i]);
		else
			B.push_back(P[i]);
	}

	int distO, distB, pO = 0, pB = 0, ans = 0;

	if(O.empty())
		distO = -1;
	else
		distO = O[0] - 1;

	if(B.empty())
		distB = -1;
	else
		distB = B[0] - 1;

	for(int i = 0; i < n; ++i)
		if(C[i] == 'O')
		{
			if(distB != -1)
				distB = max(distB - distO - 1, 0);
			ans += distO + 1;
			if(++pO == O.size())
				distO = -1;
			else
				distO = abs(O[pO] - O[pO - 1]);
		}
		else
		{
			if(distO != -1)
				distO = max(distO - distB - 1, 0);
			ans += distB + 1;
			if(++pB == B.size())
				distB = -1;
			else
				distB = abs(B[pB] - B[pB - 1]);
		}

	return ans;
}

int main()
{
	int nt;

	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);

	scanf("%d", &nt);
	for(int t = 1; t <= nt; ++t)
		printf("Case #%d: %d\n", t, solve());

	return 0;
}
