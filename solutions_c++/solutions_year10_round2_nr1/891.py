#include <string>
#include <iostream>
#include <vector>

using namespace std;

int push( string &a , vector<string> &list )
{
//cout << "--" << a << "-" << list.size() << endl;

	if( a.length() == 0 )
		return 0;
	
	for( int i = 0 ; i < list.size() ; i++ )
	{
		if( list[i] == a )
			return 0;
	}
	
	string b;
	int k;
	for( k = a.length()-1 ; a[k] != '/' && k >=0 ; k-- )
	{
		;
	}
	b = a.substr( 0 , k );
	
//	cout << k << "-->" << b << "---" << endl;
	int retVal = 1 + push( b , list );
	list.push_back( a );
	return retVal;
}


int main()
{

	int T;
	cin >> T;

	for( int i = 1 ; i <= T ; i++ )
	{
		int count = 0;
		vector < string > existing;
		string temp;
		int N , M;
		
		cin >> N >> M;
	
		for( int j = 0 ; j < N ; j++ )
		{
			cin >> temp;
			existing.push_back( temp );
		}
		
		for( int j = 1 ; j <= M ; j++ )
		{
			cin >> temp;
			count += push( temp , existing );
		}
	
		cout << "Case #"<< i << ": " << count << endl;
	}









	return 0;
}
