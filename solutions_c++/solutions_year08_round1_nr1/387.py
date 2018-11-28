#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int K;
	cin >> K;
	for(int k = 1; k <= K; k++)
	{
		int n;
		cin >> n;
		vector<long long> x(n), y(n);
		for(int i = 0; i < n; i++)
			cin >> x[i];
		for(int i = 0; i < n; i++)
			cin >> y[i];
			
		sort( x.begin(), x.end() );
		sort( y.begin(), y.end() );
		reverse( y.begin(), y.end() );
		
		long long res = 0;
		for(int i = 0; i < n; i++)
			res += x[i] * y[i];

		cout << "Case #" << k << ": " << res << endl;
	}
}