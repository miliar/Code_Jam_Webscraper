#include<iostream>
#include<string>
#include<cstring>
#include<cctype>
using namespace std;
string mp = "yhesocvxduiglbkrztnwjpfmaq";
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc, cs = 1;
	cin >> tc;
	getchar();
	while( tc -- )
	{		
		char s[1000];
		gets(s);
		int i;
		cout <<"Case #"<< cs++<<": "; 
		for(i = 0; i < strlen( s ); i ++ ){
			if( isalpha( s[ i ] ))
				cout << mp[ s[ i ] -'a' ];
			else cout << s[ i ];
		}
		cout << endl;
	}
	return 0;

}