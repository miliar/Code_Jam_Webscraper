#include <iostream>
using namespace std;
#include <fstream>
#include <string>


void googletrans(string fpath)
{
	ifstream fin(fpath);
	ofstream fout("out.txt");
	string g_tb = "yhesocvxduiglbkrztnwjpfmaq";

	if(!fin)
	{
		cout<<"Fail to read file"<<endl;
		system("PAUSE");
		exit(1);
	}
	
	string temp;
	int num;
	getline(fin,temp);
	num = atoi(temp.c_str());
	
	for(int i=0; i<num;i++)
	{
		getline(fin,temp);
		fout<<"Case #"<<i+1<<": ";
		for(int j=0; j<temp.size(); j++)
		{
			if(temp[j] == ' ')
				fout<<' ';
			else
			{
				fout<<g_tb[(int)temp[j]-97];
			}
		}
		fout<<endl;
	}
	fin.close();
	fout.close();
}

void main()
{
	string fpath = "A-small-attempt0.in";
	googletrans(fpath);
}