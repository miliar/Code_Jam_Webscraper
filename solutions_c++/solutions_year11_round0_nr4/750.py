#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

int main ()
{
	freopen("D-large.in","rt",stdin);
	freopen("D-large.out","wt",stdout);
	int t;
	cin >> t;

	for ( int tt = 1 ; tt <= t ; tt++)
	{
		int n;
		cin >> n;

		int cnt = 0;
		for ( int i = 0 ; i < n ; i ++ )
		{
			int x;
			cin >> x;
			cnt += x!=i+1;
		}
		cout << "Case #"<<tt<<": "<< cnt << endl;
	}
	return 0;
}
