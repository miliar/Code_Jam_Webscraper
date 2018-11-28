#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <string.h>
#include <conio.h>
#include <map>
#include <sstream>

using namespace std;



int main()
{
	int t=0;		//количество
	FILE* in = freopen("input.txt", "r", stdin);
	FILE* out = freopen("output.txt", "w", stdout);
	cin>>t;

	for( int i=0; i<t; i++ )
	{
		int n, s, p;
		cin >> n >> s >> p;

		int ans = 0;
		for( int j=0; j<n; j++ )
		{
			int b=0, c=0;
			cin >> b;
		
			c = b/3;
			if( b%3 != 0 )
				c++;
			if( c>= p )
				ans++;
			else
			{
				if( s>0 && b!=0 )
				{
					if( b%3 == 2 )
						c = b/3+2;
					else
						c = b/3+1;
					if( c>= p )
					{
						ans++;
						s--;
					}
				}
			}
		}
		cout << "Case #" << i+1 << ": " << ans << endl;
	}

    return 0;
}