#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

string big = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
	int T;
	ofstream outfile("C://Users//fog//Desktop//1.txt");
	if(!outfile)
		cout<<"dslf"<<endl;
	ifstream infile("C://Users//fog//Desktop//2.in");
	if(!infile)
		cout<<"df"<<endl;
	string mygod;
	getline(infile,mygod);
	
	

	char ch;
	//infile>>ch;
	int i;

	int daijia = 0;
	for(i=0;i<mygod.size();i++)
	{
		daijia = 10*daijia+mygod[i]-'0';
	}

	T = daijia;
	for(i=0;i<T;i++)
	{
		outfile<<"Case #"<<i+1<<": ";
		string str;
		getline (infile,str);
		for(int hahah = 0;hahah<str.size();hahah++)
		{
			if(str[hahah] == '\n')
				break;
			if(str[hahah] == ' ' )
				outfile<<" ";
			else
			{
				outfile<<big[str[hahah] - 'a'];
			}
		}
		outfile<<endl;
	}

	return 0;
}