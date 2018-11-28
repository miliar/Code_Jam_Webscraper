#include <iostream>
#include <string>
#include <set>
using namespace std;

int main()
{
	int		t ;
	
	cin >> t ;
	
	for( int cas = 1 ; cas <= t ; cas++ )
	{
		int		n,m;
		set<string>	allDirectory;
		set<string>	exist;
		string	buff;
		string::size_type index ;
		
		cin >> n >> m ;
		
		for( int i = 0 ; i < n ; i++ )
		{
			cin >> buff ;
			//while( (index=buff.find_last_of( '/')) != string::npos )
			exist.insert( buff ) ;
		}
		
		allDirectory.insert( exist.begin(), exist.end() ) ;
		for( int i = 0 ; i < m ; i++ )
		{
			cin >> buff ;
			
			while( buff.empty()==false )
			{
				allDirectory.insert( buff ) ;
				index=buff.find_last_of( '/');
				buff=buff.substr(0,index) ;
			}
		}
		
		cout << "Case #" << cas << ": " << allDirectory.size() - exist.size() << endl ;
	}
	
	return 0 ;
}
