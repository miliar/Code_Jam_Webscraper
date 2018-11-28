#include <iostream>
#include <string>
using namespace std;

char conv[27] = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
	//freopen("A.in","r",stdin);
	//freopen("A.txt","w",stdout);
	int T;
	cin >> T;
	cin.ignore();
	string s;
	for( int i = 1; i <= T; i++ )
	{
		cout << "Case #" << i << ": ";
		getline(cin,s);
		for( int j = 0; j < s.size(); j++ )
			if( s[j] >= 'a' && s[j] <= 'z' )
				cout << conv[(s[j]-'a')];
			else if( s[j] >= 'A' && s[j] <= 'Z' )
				cout << (char)(conv[(s[j]-'A')]-'a'+'A');
			else
				cout << s[j];
		cout << endl;
	}
	return 0;
}