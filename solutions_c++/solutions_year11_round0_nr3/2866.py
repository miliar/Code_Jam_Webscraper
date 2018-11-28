#include <iostream>
using namespace std;
int n, it, T;

int main()
{
	cin >> T;
	for ( it = 1; it <= T; ++it )
	{
		cin >> n;
		int min = 10000000;
		int ans = 0, sum = 0,x ;
		for ( int i = 0; i < n; ++i )
		{
			cin >> x;
			ans ^= x;;
			sum += x;
			if ( x < min) min = x;
		}
		cout << "Case #"<< it << ": ";
		if ( ans == 0 )
			cout << sum - min<<"\n";
		else cout << "NO\n";
	}
}
		
