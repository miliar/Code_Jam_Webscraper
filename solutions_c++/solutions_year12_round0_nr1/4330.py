#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<cstdlib>
#include<string>
#include<conio.h>
using namespace std;
void main ()
{
	ifstream in("in.txt");
	ifstream in1("in1.txt");
	char c;
	string str;
	string str1;
	c=in.get();
	while(!in.eof())
	{
		str+=c;
		c=in.get();
	}
	c=in1.get();
	while(!in1.eof())
	{
		str1+=c;
		c=in1.get();
	}
	in.close();
	in.close();
	
	ifstream in3("A-small-attempt1.in");
	ofstream out("out.txt");
	int N;
	string str2;
	in3>>N;
	in3.ignore();
	for(int i=0 ; i<N; i++)
	{
		c=in3.get();
		while(!in3.eof() && c!='\n')
		{
			if(c!=' ')
			{
				if(c=='q')
				{
					c='z';
					str2+=c ;

				}
				else if(c=='z')
				{
					str2+="q";
				}
				else
				{
					str2+=str1[str.find(c)];
				}
				
			}
			else
			{
				str2+=c;
			}
			c=in3.get();
		}
		out<<"Case #"<<i+1<<": "<<str2;
		if(i+1<N)
		{
			out<<endl;
		}
		str2=""; 
	}
	in3.close();
		out.close();
	
	

}