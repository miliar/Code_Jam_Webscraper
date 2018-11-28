#include <iostream>
#include <string>
#include <vector>
#include <cstdio>

using namespace std;

char c[27];

string r = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
	int n;
	cin>>n;
	string t;
	getline(cin,t);
	int index = 1;
	while(n--)
	{
		cout<<"Case #"<<index++<<": ";
		getline(cin,t);
		for(int j = 0;j<t.length();j++)
		{
			if(t[j]!=' ')t[j]=r[t[j]-'a'];
			cout<<t[j];
		}
		cout<<endl;
	}


	return 0;
}