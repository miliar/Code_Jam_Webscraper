#include<iostream>
#include<fstream>
#include<string>
#include <sstream>
using namespace std;
string get_string(int nbr)
{
	ostringstream oss;
	oss << nbr;
	return oss.str();
}

bool check(int a, int b)
{
	string str1=get_string(a);
	string str2=get_string(b);
	char tmp;

	for(int i=0;i<str1.length();i++)
	{
		tmp=str1[str1.length()-1];
		for(int j=str1.length()-1;j>0;j--)
			str1[j]=str1[j-1];
		str1[0]=tmp;
		if(str1==str2)
			return true;
	}
	return false;
}

int main()
{
	ifstream file("C-small-attempt0.in",ios::in);
	ofstream fichier("C-small-attempt0.out", ios::out | ios::trunc);
	string line;
	int t,a,b,nbr;
	bool match;

	getline(file,line);
	istringstream iss (line,istringstream::in);
	iss>>t;
	for(int n=0;n<t;n++)
	{
		nbr=0;
		getline(file,line);
		istringstream iss (line,istringstream::in);
		iss>>a;
		iss>>b;
		for(int i=b;i>a;i--)
			for(int j=a;j<i;j++)
				if(check(j,i))
					nbr++;
		fichier<<"Case #"<<n+1<<": "<<nbr<<endl;
	}
	return 0;
}
