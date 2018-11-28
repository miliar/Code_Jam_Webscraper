#include <iostream>
using std::cin;
using std::cout;

int main()
{
	int t,T;
	
	cin >> T;
	
	for ( t = 0; t < T; t++ )
	{
		int n,N;
		int x;
		int ans = 0;
		
		cin >> N;

		for ( n = 0; n < N; n++ )
		{
			cin >> x;
			if ( x != n + 1 ) ans++;
		}
		
		cout << "Case #" << t + 1 << ": " << ans << "\n";
	}
	
	return 0;
}
