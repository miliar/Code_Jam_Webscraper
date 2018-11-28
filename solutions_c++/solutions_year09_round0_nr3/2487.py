#include<iostream>
#include<string>
using namespace std;

int main()
{
	int n;
	cin >> n;
	string s;
	getline( cin, s );
	string h = "welcome to code jam";
	for( int i = 0; i < n; i++ )
	{
		string s;
		getline( cin, s );
		unsigned long long t[s.size()+1][22];
		for( int j = 0; j < s.size()+1; j++ )
		{
			for( int k = 0; k < 22; k++ )
			{
				t[j][k] = 0;
			}
		}
		t[0][0] = 1;

		for( int j = 0; j < s.size(); j++ )
		{
			for( int k = 0; k < 19; k++ )
			{
				if( s[j] == h[k] )
				{
					for( int l = j; l >= 0; l-- )
					{
						t[j+1][k+1] += t[l][k];
					}
					//cout << j << " " << k << " " << s[j] << " " << t[j+1][k+1] << endl;
				}
			}
		}

		unsigned long long ans = 0;
		for( int j = 0; j < s.size()+1; j++ )
		{
			ans += t[j][19];
			//cout << j << " " << t[j][19] << endl;
		}
		printf( "Case #%d: %04d\n", i+1, (int)ans );
	}
}

