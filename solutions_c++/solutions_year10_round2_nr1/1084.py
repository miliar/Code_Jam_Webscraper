#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <map>

using namespace std;

int main()
{

	FILE *fin = freopen("input.txt", "r", stdin);
	FILE *fout = fopen("out.txt", "w");

	set < string > exist;
	set < string > all;

	int t, n, m;
	cin >> t;

	for( int i= 1; i <= t; ++i )
	{
		exist.clear();
		all.clear();

		string instr;
		int cnt;

		cin >> n >> m;

		exist.insert("/");

		for( cnt = 0; cnt < n; ++cnt )
		{
			cin >> instr;

			instr += "/";

			if( exist.find(instr) == exist.end() )
			{
				for( int a = 1; ; ++a )
				{
					int found = instr.find("/", a );
					if( found == instr.npos )
						break;
					string temp = instr.substr(0, found );

					if( exist.find(temp) == exist.end() )
						exist.insert(temp);

					a = found;
				}
			}
		}

		for( cnt = 0; cnt < m; ++cnt )
		{
			cin >> instr;

			instr += "/";

			if( all.find(instr) == all.end() )
			{
				for( int a = 1; ; ++a )
				{
					int found = instr.find("/", a );
					if( found == instr.npos )
						break;
					string temp = instr.substr(0, found );

					if( all.find(temp) == all.end() )
						all.insert(temp);

					a = found;
				}
			}
		}

		int count = 0;
		for( set <string> ::iterator it = exist.begin(); it != exist.end(); ++it )
		{
			if( all.find(*it) != all.end() )
				++count;
		}

		cout << "Case #" << i << ": " << all.size() - count << endl;
		fprintf(fout, "Case #%d: %d\n", i, all.size() - count);
	}
	return 0;
}