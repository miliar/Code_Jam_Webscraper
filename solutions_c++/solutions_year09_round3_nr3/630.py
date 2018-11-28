#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int findCost(int C, int P, bool Pr[10005])
{
	int Ans = 0;
	for (int i=C-1; i>=1; i--)
	{
		if (Pr[i])
			Ans++;
		else
			break;
	}
	for (int i=C+1; i<=P; i++)
	{
		if (Pr[i])
			Ans++;
		else
			break;
	}
	return Ans;
}

int main()
{
	int T;
	scanf("%d", &T);
	freopen("csmall.out","w",stdout);
	
	for (int test=1; test<=T; test++)
	{
		int P, Q, i, j, k;
		bool Prison[10005];
		int MinAns = 1000099, Ans;
		vector<int> Rel;
		
		scanf("%d %d", &P, &Q);
		
		for (i=0; i<Q; i++)
		{
			int x; 
			scanf("%d", &x);
			Rel.push_back(x);
		}
		
		do
		{
			Ans = 0;
			for (i=1; i<=P; i++)
				Prison[i] = true;
			
			int MTemp;
			for (i=0; i<Q; i++)
			{
				MTemp = findCost(Rel[i], P, Prison);
			
				Prison[Rel[i]] = false;
				Ans += MTemp;
			}
			MinAns = min(Ans,MinAns);
		} while (next_permutation(Rel.begin(), Rel.end()));
		printf("Case #%d: %d\n", test, MinAns);
	}
	return 0;
}

		