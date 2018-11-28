#include <iostream>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

set<string> exists;

string getp( string p )
{
	size_t i = -1;
	for( size_t j=0; j<p.size(); ++j )
	{
		if(p[j] == '/')
			i = j;
	}

	return p.substr(0, i);
}

int main()
{
	int C;
	cin >> C;	

	int cn = 1;
	while(C--)
	{
		exists.clear();
		exists.insert(string(""));

		int N, M;
		cin >> N >> M;
		
		for( int i=0; i<N; ++i )
		{
			string s;
			cin >> s;

			while( s != "" )
			{
				exists.insert(s);
				s = getp( s );
			}
		}

		unsigned long t = 0;
		for( int i=0; i<M; ++i )
		{
			string s;
			cin >> s;

			while( exists.find(s) == exists.end() )
			{
				++t;
				exists.insert(s);

				s = getp( s );
			}
		}

		
		cout << "Case #"  << cn << ": " << t << endl;

		++cn;
	}
	return 0;
}