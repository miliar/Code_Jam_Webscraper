#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int n;
	cin >> n ;
	char alpha[27] = "yhesocvxduiglbkrztnwjpfmaq";
	int ii=1;	
	cin >> ws ;
	while(n--)
	{
		string s;
		getline(cin,s);
		int len = s.length();
		cout << "Case #"<<ii<<": ";		
		for(int i=0;i<len;i++)
		{	
			if(s[i] != ' ')
			cout << (char) alpha [ s[i] -'a'] ;
			else cout << " " ;	
		}
		cout << endl;
		ii++;	
	}
}
