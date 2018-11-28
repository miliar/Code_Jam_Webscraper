#include <iostream>
#include <cctype>
#include <cstring>
#include <string>

using namespace std;

char str[]="yhesocvxduiglbkrztnwjpfmaq";

int main()
{
	int i;
	cin>>i;
	string ch;
	getline(cin,ch);
	for(int x=1;x<=i;x++){
		getline(cin,ch);
		for(int j=0;j<ch.length();j++){
			if(isalpha(ch[j])) ch[j]=str[ch[j]-'a'];
		}
		cout<<"Case #"<<x<<": "<<ch<<endl;
	}
}