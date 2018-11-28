#include <iostream>
#include <sstream>

using namespace std;

int main()
{
	freopen( "C-small-attempt0.in", "rt", stdin );
	freopen( "test-output.txt", "wt", stdout );

	int T = 0;
	cin >> T;

	for( int i = 0; i < T; i++ )
	{
		long long A = 0;
		cin >> A;

		long long B = 0;
		cin >> B;

		int count = 0;

		for( long long n = A; n < B; n++ ) // j <= B not needed as impossible to have recycled > B..
		{
			stringstream ss;
			ss << n;
			string s = ss.str();

			long long mArr[10] = {0};
			int d = 0;
			for( int j = s.length()-1; j >= 0; j-- )
			{
				string ns = "\0";
				ns.append( s, j, s.length() - j );
				ns.append( s, 0, j );

				long long m = 0;
				m = atoi(ns.c_str());

				for( int k = 0; k < d; k++ )
				{
					if( mArr[k] == m )
						goto here;
				}
				mArr[d] = m;
				d++;

				if( m <= A || m > B || n >= m )
					continue;

				for( long long k = n+1; k <= B; k++ )
				{
					if( k == m )
					{
						count++;
					}
				}
here:

;			}
		}

		cout << "Case #" << i+1 << ": " << count << endl;
	}

	return 0;
}