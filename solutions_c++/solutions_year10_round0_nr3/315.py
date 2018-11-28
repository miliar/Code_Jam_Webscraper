#include <iostream>

using namespace std;


int n, r, k;
long long g[1111];

void Load()
{
	cin >> r >> k >> n;
	for (int i = 0; i < n; i++)
		cin >> g[i];
}



long long next[1111][30];
long long cost[1111][30];

long long Solve()
{
	long long total = 0;
	int i, j, t;
	for (i = 0; i < n; i++)
		total += g[i];
	if (total < k)
		return r * total;
	j = 0;
	total = g[0];
	for (i = 0; i < n; i++)
	{
		while (total <= k) 
		{
			j = (j+1) % n;
			total += g[j];			
		}
		next[i][0] = j;
		cost[i][0] = total-g[j];
		total -= g[i];
	}

/*	cerr << "k = " << k << "\n";
	for (i = 0; i < n; i++) cerr << g[i] << ' ';
	cerr << "\n";
	for (i = 0; i < n; i++)
	{
		cerr << i << " -> " << next[i][0] << " cost = " << cost[i][0] << "\n";
		for (j = i; j != next[i][0]; j = (j+1)%n)
			cerr << g[j] <<  ' ';
		cerr << "\n";
	}
*/

	long long ans = 0;
	int cur = 0;

	for (j = 1; j < 45; j++)
	{
		if ((((long long)1) << j) > r) break;
		for (i = 0; i < n; i++)
		{
			t = next[i][j-1];
			next[i][j] = next[t][j-1];
			cost[i][j] = cost[i][j-1] + cost[t][j-1];	
		}
		if (r & (((long long)1) << j))
		{
			ans += cost[cur][j];
			cur = next[cur][j];
		}
	}
	if (r % 2) ans += cost[cur][0];

/*	long long ans2 = 0;
	cur = 0;
	for (i = 0; i < r; i++)
	{
		ans2 += cost[cur][0];
		cur = next[cur][0];
	}

	cerr << "ans2 = " << ans2 << "\n";
*/

	return ans;

	
}



int main(){
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ": " << Solve() << "\n";
	}
	return 0;
}
