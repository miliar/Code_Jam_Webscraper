#include <iostream>
#include <vector>

using namespace std;

int step( int k, int N, vector<int> &g, int &front )
{
	int m=0;
	int i;
	for ( i=0; i<N && m+g[i]<=k; i++ )
		m += g[i];

	vector<int> tmp = g;
	g.clear();
	g.insert( g.end(), tmp.begin()+i, tmp.end() );
	g.insert( g.end(), tmp.begin(), tmp.begin()+i );

	front = ( front + i ) % N;

	return m;
}

int main()
{
	int T;  cin >> T;

	for ( int t=1; t<=T; t++ )
	{
		int R, k, N;
		cin >> R >> k >> N;

		vector<int> g( N );
		for ( int i=0; i<N; i++ )
			cin >> g[i];

		int front = 0;

		long long money = 0;

		if ( R <= 4*N )
		{
			for ( int i=0; i<R; i++ )
				money += step( k, N, g, front );
		}
		else
		{
			vector<bool> f( N );

			int c = 0;
			for ( int i=0; i<3*N; i++ )
			{
				if ( f[front] )
					break;

				f[front] = true;

				money += step( k, N, g, front );
				c++;
			}

			int org = front;
			long long m = 0;
			int period = 0;

			for ( int i=0; i<N; i++ )
			{
				m += step( k, N, g, front );
				period++;

				if ( front == org )
					break;
			}

			money += m * ( (R-c)/period );
			c += ( (R-c)/period*period );

			for ( ; c<R; c++ )
				money += step( k, N, g, front );
		}

		
		cout << "Case #" << t << ": " << money << endl;
	}

	return 0;
}




