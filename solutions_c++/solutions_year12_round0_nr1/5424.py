#include<iostream>
#include<cstring>

using namespace std;

char replace (char x);

int main()
{
	int i,j,num_cases;
	cin>>num_cases;
	string str;
	getline(cin,str);
	for (i=0;i<=num_cases;i++)
	{
		string rep;
		//cout<<i<<" "<<str<<endl;
		int len = str.length();
		for (j=0;j<len;j++)
		{
			rep = rep+replace(str[j]);
		}
		if(i>0)
			cout<<"Case #"<<i<<": "<<rep<<endl;
		getline(cin,str);
	}		
	return 0;
}

char replace (char x)
{
	char ch;
	if (x=='a')
		ch = 'y';
	else if (x=='b')
		ch = 'h';
	else if (x=='c')
		ch = 'e';
	else if (x=='d')
		ch = 's';
	else if (x=='e')
		ch = 'o';
	else if (x=='f')
		ch = 'c';
	else if (x=='g')
		ch = 'v';
	else if (x=='h')
		ch = 'x';
	else if (x=='i')
		ch = 'd';
	else if (x=='j')
		ch = 'u';
	else if (x=='k')
		ch = 'i';
	else if (x=='l')
		ch = 'g';
	else if (x=='m')
		ch = 'l';
	else if (x=='n')
		ch = 'b';
	else if (x=='o')
		ch = 'k';
	else if (x=='p')
		ch = 'r';
	else if (x=='q')
		ch = 'z';
	else if (x=='r')
		ch = 't';
	else if (x=='s')
		ch = 'n';
	else if (x=='t')
		ch = 'w';
	else if (x=='u')
		ch = 'j';
	else if (x=='v')
		ch = 'p';
	else if (x=='w')
		ch = 'f';
	else if (x=='x')
		ch = 'm';
	else if (x=='y')
		ch = 'a';
	else if (x=='z')
		ch = 'q';
	else if (x==' ')
		ch = ' ';
	return ch;
}	
