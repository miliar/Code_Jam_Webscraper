#include <iostream>
#include <fstream>
#include <string>
using namespace std;

char convert(char a)
{
	if(a=='a')
		return 'y';
	else if(a=='b')
		return 'h';
	else if(a=='c')
		return 'e';
	else if(a=='d')
		return 's';
	else if(a=='e')
		return 'o';
	else if(a=='f')
		return 'c';
	else if(a=='g')
		return 'v';
	else if(a=='h')
		return 'x';
	else if(a=='i')
		return 'd';
	else if(a=='j')
		return 'u';
	else if(a=='k')
		return 'i';
	else if(a=='l')
		return 'g';
	else if(a=='m')
		return 'l';
	else if(a=='n')
		return 'b';
	else if(a=='o')
		return 'k';
	else if(a=='p')
		return 'r';
	else if(a=='q')
		return 'z';
	else if(a=='r')
		return 't';
	else if(a=='s')
		return 'n';
	else if(a=='t')
		return 'w';
	else if(a=='u')
		return 'j';
	else if(a=='v')
		return 'p';
	else if(a=='w')
		return 'f';
	else if(a=='x')
		return 'm';
	else if(a=='y')
		return 'a';
	else if(a=='z')
		return 'q';
	else
		return a;
}
int main()
{
	int t,cnt=0,i;
	ifstream file;
	ofstream file1;
	char g[150],s[150];
	file.open("A-small-attempt1.in");
	file1.open("test.out");
    //freopen("test.out", "w", stdout);
	file>>t;
	file.getline(g,150);
	while(t--)
	{
		file.getline(g,150);
		i=0;
		while(g[i]!=NULL)
		{
			s[i]=convert(g[i]);
			i++;
		}
		s[i]='\0';
		/*cout<<g<<"\n"<<s<<"\n";
		getchar();*/
		file1<<"Case #"<<++cnt<<": "<<s<<"\n";
	}
	return 0;
}

