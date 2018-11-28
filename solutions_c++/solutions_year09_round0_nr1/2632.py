#include<iostream>
#include<vector>
#include<set>
#include<string>
using namespace std;

int main()
{
	int L, D, N;
	vector<string> v;
	cin >> L >> D >> N;
	for( int i = 0; i < D; i++ )
	{
		string s;
		cin >> s;
		v.push_back( s );
	}
	vector< vector< set<char> > > n;
	for( int i = 0; i < N; i++ )
	{
		string s;
		cin >> s;
		vector< set<char> > m;
		for( int j = 0; j < s.size(); j++ )
		{
			set<char> t;
			if( s[j] == '(' )
			{
				j++;
				for( ; j < s.size() && s[j] != ')'; j++ )
				{
					t.insert(s[j]);
				}
			}
			else
			{
				t.insert( s[j] );
			}
			m.push_back( t );
		}
		n.push_back( m );
	}


	for( int k = 0; k < N; k++ )
	{
		int ans = 0;
		for( int i = 0; i < D; i++ )
		{
			int j = 0;
			for( j = 0; j < L; j++ )
			{
				if( n[k][j].find( v[i][j] ) == n[k][j].end() )
				{
					break;
				}
			}
			if( j == L )
			{
				ans++;
			}
		}
		cout << "Case #" << (k+1) << ": " << ans << endl;
	}
}


