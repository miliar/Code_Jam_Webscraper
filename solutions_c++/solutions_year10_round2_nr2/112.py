#include <iostream>
using namespace std;

const int MAXN = 50 + 10, INF = 1000*1000*1000;

int b, t;
int xs[MAXN], vs[MAXN];

int swp(int n, int k)
{
//	cout << "@ " << n << " " << k << endl;
	if(k == 0)
		return 0;
	if(k > n)
		return -INF;
	if(xs[n]+vs[n]*t >= b)
		return swp(n-1, k-1);
	else
		return swp(n-1, k) + k;
}

int main()
{
	int c;
	cin >> c;
	for(int ts=1; ts<=c; ts++)
	{
		int n, k; 
		cin >> n >> k >> b >> t;
		for(int i=1; i<=n; i++)
			cin >> xs[i];
		for(int i=1; i<=n; i++)
			cin >> vs[i];
		int out = swp(n, k);
		cout << "Case #" << ts << ": ";
		if(out < 0)
			cout << "IMPOSSIBLE";
		else
			cout << out;
		cout << endl;
	}
	return 0;
}
