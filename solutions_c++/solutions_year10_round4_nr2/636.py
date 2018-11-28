#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for ( int t=0; t<T; t++ )
	{
		int P;
		cin >> P;
		vector<int> M(1<<P);

		for ( int i=0; i<(1<<P); i++ )
			cin >> M[i];

		vector<vector<int> > price;

		for ( int p=0; p<P; p++ )
		{
			vector<int> temp( 1<<(P-p-1) );
			for ( int i=0; i<(1<<(P-p-1)); i++ )
				cin >> temp[i];
			price.push_back( temp );
		}

		vector<vector<bool> > bought;
		for ( int p=0; p<P; p++ )
			bought.push_back( vector<bool>( 1<<(P-p-1), false ) );

		for ( int i=0; i<(1<<P); i++ )
		{
			for ( int j=0; j<(P-M[i]); j++ )
				bought[P-j-1][i>>(P-j)] = true;
		}

		int ans = 0;

		for ( int p=0; p<P; p++ )
			for ( int i=0; i<(1<<(P-p-1)); i++ )
				if ( bought[p][i] )
					ans++;

		cout << "Case #" << (t+1) << ": " << ans << endl;
	}
}