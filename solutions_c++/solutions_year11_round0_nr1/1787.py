
#include <iostream>

#include <vector>
#include <string>

#include <ctype.h>

using namespace std;

int n;


int main()
{
	cin >> n;

	for( int i=0; i<n; ++i )
	{
		int ret = 0;
		int m;
		int o = 0, b = 0;
		int ook = 0, bok = 0;
		cin >> m;
		for( int j=0; j<m; ++j )
		{
			string ob, num;
			cin >> ob >> num;
			int next = atoi( num.c_str() )-1;
			//cout << next << endl;
			if ( ob == "O" )
			{
				if ( abs( next-o ) > ook )
				{
					ret += abs( next-o )-ook;
					bok += abs( next-o )-ook;
				}
				ret++;
				bok++;
				ook = 0;
				o = next;
			}
			else
			{
				if ( abs( next-b ) > bok )
				{
					ret += abs( next-b )-bok;
					ook += abs( next-b )-bok;
				}
				ret++;
				ook++;
				bok = 0;
				b = next;
			}
		}
		
		cout << "Case #" << (i+1) << ": " << ret << endl;
	}

	return 0;
}

