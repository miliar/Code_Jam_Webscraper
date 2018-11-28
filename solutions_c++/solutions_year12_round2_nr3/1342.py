#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>

using namespace std;

map< long long, pair< long long, long long > > v;

void printMap( long long a , bool first )
{
	if( v[a].second == -1 )
	{
		if( !first )
			cout << " ";
		cout << v[a].first;
	}
	else
	{
		printMap( v[a].first, first );
		printMap( v[a].second, false );
	}
}

int main(){	
	
	int T;
	cin >> T;
	
	for (int o = 1; o <= T; o++)
	{
		v.erase ( v.begin(), v.end() );
		int n;
		cin >> n;
		
		long long s[n];
		
		for (int i = 0; i <n ; i++)
		{
			cin >> s[i];
		}
		
		set <long long> a;
		bool impos = true;
		
		cout << "Case #" << o << ":" << endl;
		
		for (int i = 0; i < n; i++)
		{
			if( v.find(s[i]) != v.end() )
			{
				cout << s[i] << endl;
				
				printMap( v[s[i]].first, true );
				printMap( v[s[i]].second, false );
				cout << endl;
				impos = false;
				break;

			}
			
			v[s[i]] = pair< long long,long long>( s[i], -1 );
			
			set <long long>::iterator it;
			set <long long> b;
			b = a;
			
			for (it = b.begin(); it != b.end() ; it++)
			{
				long long neww = *it+s[i];
				if( v.find( neww ) != v.end() )
				{
					printMap( *it, true );
					printMap( s[i], false );
					cout << endl;
					
					printMap( neww,true );
					cout << endl;
					impos = false;
					break;
				}
				v[neww] = pair<long long, long long>( *it,s[i] );
				a.insert( neww );
			}
			
			if( !impos ) break;
			
			a.insert( s[i] );
		}
		
		if( impos )
			cout << "Impossible" << endl;
	}
	
	return 0;
}

