#include <iostream>
#include <string>
using namespace std;

char convertedchar(char ch)
{
	if(ch=='a')  return 'y';
	if(ch=='b')  return 'h';
	if(ch=='c')  return 'e';
	if(ch=='d')  return 's';
	if(ch=='e')  return 'o';
	if(ch=='f')  return 'c';
	if(ch=='g')  return 'v';
	if(ch=='h')  return 'x';
	if(ch=='i')  return 'd';
	if(ch=='j')  return 'u';
	if(ch=='k')  return 'i';
	if(ch=='l')  return 'g';
	if(ch=='m')  return 'l';
	if(ch=='n')  return 'b';
	if(ch=='o')  return 'k';
	if(ch=='p')  return 'r';
	if(ch=='q')  return 'z';
	if(ch=='r')  return 't';
	if(ch=='s')  return 'n';
	if(ch=='t')  return 'w';
	if(ch=='u')  return 'j';
	if(ch=='v')  return 'p';
	if(ch=='w')  return 'f';
	if(ch=='x')  return 'm';
	if(ch=='y')  return 'a';
	if(ch=='z')  return 'q';
}

int main()
{
	int T,i;
	cin>>T;
	for(i=1;i<=T;i++)
	{
	char ch;
		if(i==1) 
		{
			cin>>ch;
		}
		string str;
		getline(cin,str);
		char output[str.length()];
		int j;
		for(j=0;j<str.length();j++)
		{
			if(str.at(j)==' ')  output[j]=' ';
			else  output[j]=convertedchar(str.at(j));
		}
		cout<<"Case #"<<i<<": ";
		if(i==1) cout<<convertedchar(ch);
		for(j=0;j<str.length();j++)
		cout<<output[j];
		cout<<endl;
	}
}