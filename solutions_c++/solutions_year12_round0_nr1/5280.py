#include<iostream>
using namespace std;

char changemap(char a)
{
	switch (a)
	{
	case 'a':
		return 'y';
	case 'b':
		return 'h';
	case 'c':
		return 'e';
	case 'd':
		return 's';
	case 'e':
		return 'o';
	case 'f':
		return 'c';
	case 'g':
		return 'v';
	case 'h':
		return 'x';
	case'i':
		return 'd';
	case 'j':
		return 'u';
	case 'k':
		return 'i';
	case 'l':
		return 'g';
	case'm':
		return 'l';
	case 'n':
		return 'b';
	case  'o':
		return 'k';
	case 'p':
		return 'r';
	case 'q':
		return 'z';
	case 'r':
		return 't';
	case 's':
		return 'n';
	case't':
		return 'w';
	case'u':
		return 'j';
	case 'v':
		return 'p';
	case 'w':
		return 'f';
	case 'x':
		return 'm';
	case 'y':
		return 'a';
	case 'z':
		return 'q';
	case ' ':
		return ' ';
	}
}


int main()
{
	//string a;
	int T,k=0;
	cin>>T;
	char s[2];
		cin.getline(s,2);
	while(T--)
	{
		
		string a;
		//a[0]='\0';
		getline(cin,a,'\n');
		cout<<"Case #"<<++k<<": ";
		for(int i=0;i<a.length();i++)
		{
			cout<<changemap(a[i]);
		}
		cout<<endl;
	}
	return 0;
}
