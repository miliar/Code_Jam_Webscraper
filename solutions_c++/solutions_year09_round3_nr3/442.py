#include <vector>
#include <algorithm>
#include <queue>
#include <string>
#include <stdio.h>

using namespace std;

int go(vector <int> v, int p)
{
	int i,l,r=0, c;
	r = p - 1;
	vector <bool> jest(p+10, true);
	jest[v[0]] = false;

	for (i=1; i<v.size(); i++) // wypuszczamy wiezniow
	{
		c = v[i];
		for (l=c-1; l>=1; l--)
		{
			if (!jest[l]) break;
			r++;
		}
		for (l=c+1; l<=p; l++)
		{
			if (!jest[l]) break;
			r++;
		}
		jest[c] = false;
	}
	return r;
}

int main()
{
	int i,l,k,j;
	int T, P,Q;

	scanf("%d", &T);
	for (k=0; k<T; k++)
	{
		vector <int> q;
		scanf("%d %d", &P, &Q);
		for (i=0; i<Q; i++)
		{
			scanf("%d", &j);
			q.push_back(j);
		}

		int best = 99999999, res;
		
		do
		{
			res = go(q, P);
			if (res < best) best = res;
		} while (next_permutation(q.begin(), q.end()));

		printf("Case #%d: %d\n", k+1, best);
	}
	return 0;
}
