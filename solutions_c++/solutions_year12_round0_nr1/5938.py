#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>
using namespace std;

char M_convert(char c)
{
	switch(c)
	{
	case 'y' : return 'a';
	case 'n' : return 'b';
	case 'f' : return 'c';
	case 'i' : return 'd';
	case 'c' : return 'e';
	case 'w' : return 'f';
	case 'l' : return 'g';
	case 'b' : return 'h';
	case 'k' : return 'i';
	case 'u' : return 'j';
	case 'o' : return 'k';
	case 'm' : return 'l';
	case 'x' : return 'm';
	case 's' : return 'n';
	case 'e' : return 'o';
	case 'v' : return 'p';
	case 'z' : return 'q';
	case 'p' : return 'r';
	case 'd' : return 's';
	case 'r' : return 't';
	case 'j' : return 'u';
	case 'g' : return 'v';
	case 't' : return 'w';
	case 'h' : return 'x';
	case 'a' : return 'y';
	case 'q' : return 'z';
	case ' ' : return ' ';
	}
}
int main()
{
	int t;
	//ifstream in("C:\\Users\\Vbox\\Desktop\\Input.txt");
	//ofstream out("C:\\Users\\Vbox\\Desktop\\Out.txt");
	cin>>t;
	string temp;
	getline(cin,temp);

	for(int i=0; i<t; i++)
	{
		string str;
		getline(cin,str);
		cout<<"Case #"<<i+1<<": ";
		for(int j =0; j<str.length(); j++)
		{
			//char c = M_convert(str[j]);
			cout<< M_convert(str[j]);
		}
		cout<<endl;
	}
	//system("pause>0");
}