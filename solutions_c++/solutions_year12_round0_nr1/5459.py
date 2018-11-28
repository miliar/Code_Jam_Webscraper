#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

int main()
{
	vector <char> mapping(26,0);
	for( int i = 0; i < 26; i++ )
	{
		int temp;
		cin >> temp;
		mapping[i] = temp + 'a';
	}
	int t;
	cin >> t;
	char s[120];
	cin.getline(s,120,'\n');	
	for( int j = 0; j < t; j++ )
	{
		cin.getline(s,120,'\n');
		cout<<"Case #" << j+1 <<": ";
		for( int i = 0; i < 120; i++ )
		{
			if( s[i] == ' ' )
				cout << " " ;
			else if( s[i] >= 'a' && s[i] <= 'z' )
				cout << mapping[ s[i] - 'a' ];
			else
				break;
		}
		cout << endl;
	}
	return 0;
}
		



	
