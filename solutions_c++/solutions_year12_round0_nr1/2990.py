#include<cstdio>
#include<iostream>
#include<cmath>
#include<fstream>
#include<string>
using namespace std;

int main()
{
	int t,w,k;
	string inputstring,outputstring;
	char input[101],output[101];
	char g[27]="abcdefghijklmnopqrstuvwxyz";
	char s[27]="yhesocvxduiglbkrztnwjpfmaq";
	//bool ;
	ifstream infile ("test small.txt");
	ofstream outfile;
	outfile.open("output test.txt");
	infile>>t;
	//cin>>t;
	for (int i=0;i<t+1;i++)
	{
		outputstring="";
		getline (infile,inputstring);
		//outfile<<inputstring<<endl;
		for(int j=0;j<inputstring.size();j++)
		{
			if(inputstring[j]==' ')
			{
				outputstring+=' ';
			}
			else
			{
				for(int x=0;x<27;x++)
				{
					if(inputstring[j]==g[x])
					{
						k=x;
						break;
					}
				}
				outputstring+=s[k];
			}
		}
		outfile<<"Case #"<<i<<": "<<outputstring<<endl;
	}
	return 0;
}