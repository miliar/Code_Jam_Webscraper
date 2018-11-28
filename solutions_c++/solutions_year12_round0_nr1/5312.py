#include <iostream>
#include <string>
using namespace std;

int main()
{
	int T;
	cin>>T;
	string str = "";
	getline (cin,str);
	for( int i = 0; i < T; i++ )
	{
		cout<<"Case #"<<i+1<<": ";
		getline (cin,str);
		for(int j = 0; str[j] != '\0'; j++)
		{
			if( str[j] == 'a' )
				cout<<'y';
			else if( str[j] == 'b' )
				cout<<'h';
			else if( str[j] == 'c' )
				cout<<'e';
			else if( str[j] == 'd' )
				cout<<'s';
			else if( str[j] == 'e' )
				cout<<'o';
			else if( str[j] == 'f' )
				cout<<'c';
			else if( str[j] == 'g' )
				cout<<'v';
			else if( str[j] == 'h' )
				cout<<'x';
			else if( str[j] == 'i' )
				cout<<'d';
			else if( str[j] == 'j' )
				cout<<'u';
			else if( str[j] == 'k' )
				cout<<'i';
			else if( str[j] == 'l' )
				cout<<'g';
			else if( str[j] == 'm' )
				cout<<'l';
			else if( str[j] == 'n' )
				cout<<'b';
			else if( str[j] == 'o' )
				cout<<'k';
			else if( str[j] == 'p' )
				cout<<'r';
			else if( str[j] == 'q' )
				cout<<'z';
			else if( str[j] == 'r' )
				cout<<'t';
			else if( str[j] == 's' )
				cout<<'n';
			else if( str[j] == 't' )
				cout<<'w';
			else if( str[j] == 'u' )
				cout<<'j';
			else if( str[j] == 'v' )
				cout<<'p';
			else if( str[j] == 'w' )
				cout<<'f';
			else if( str[j] == 'x' )
				cout<<'m';
			else if( str[j] == 'y' )
				cout<<'a';
			else if( str[j] == 'z' )
				cout<<'q';
			else cout<<' ';
		}
		cout<<endl;
	}
	return 0;
}
