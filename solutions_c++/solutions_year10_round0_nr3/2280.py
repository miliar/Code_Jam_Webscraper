#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int solve(int r, int k, queue<int> &q)
{
	int e;
	int total = 0;
	for( int i = 0; i < r; i++)
	{
		e = 0;
		int n = q.size();
		while( n > 0 && (e + q.front()) <= k )
		{
			e += q.front();
			q.push(q.front());
			q.pop();
			n--;
		}

		total += e;
	}
	return total;
}
int main()
{
	freopen("C-small.in","r",stdin);
	freopen("c.out","w",stdout);
	int count;
	cin >> count;
	for(int i = 0; i < count; i++)
	{
		int r,n,k;
		int t;
		queue<int> q; 
		cin >> r;
		cin >> k;
		cin >> n;
		for(int j = 0; j < n; j++)
		{	
			cin >> t;
			q.push(t);
		}
		cout << "Case #" << i+1 << ": " << solve(r,k,q) << endl;
	}
}