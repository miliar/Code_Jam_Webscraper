#include<iostream>

using namespace std;

int main()
{
	freopen( "input.txt","rt", stdin );
	freopen( "output.txt","wt", stdout );
	int tests;
	cin >> tests;
	for( int t = 1; t <= tests; t++ )
		{
			int n;
			int res = 0;
			cin >> n;
			for( int i = 1; i <= n; i++ )
				{
					int x;
					cin >> x;
					if( x != i )
						res++;
				}
			cout << "Case #" << t << ": " << res << endl;

		}
}