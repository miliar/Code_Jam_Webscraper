#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;

char s[99999];
char idx[30]="yhesocvxduiglbkrztnwjpfmaq";
int T,t;

int main()
{
	cin>>T;
	gets(s);
	while(T--)
	{
		gets(s);
		cout<<"Case #";
		cout<<++t<<": ";
		for(int i=0;i<strlen(s);i++)
			if(isalpha(s[i])) putchar(idx[s[i]-'a']);
			else putchar(s[i]);
		cout<<endl;
	}
	return 0;
}
