#include "stdio.h"
#include "conio.h"
#include <iostream>
#include <string>
#include <list>
#include <fstream>

using namespace std;
std::list<string*>	str_list;
int l,d,n;
int checkgr(string testgr,string s)//return in 0 or 1 in each small group
{
	//cout<<"comp "<<testgr<<" - "<< s<<endl;
	if(testgr.find(s)>testgr.length())//not equal
	{
		//cout<<"ret 0"<<endl;
		return 0;
	}
	else 
	{
		//cout<<"ret 1"<<endl;
		return 1;
	}
}
int checkw(string testin,string s)//return in 0 or 1 in each word
{
	//if(testin.compare("")==0||s.compare("")==0)
	//{
	//	return 0;
	//}
	int start_testing=0;
	//int ei;
	for(int i=0;i<l;i++)//i mean tue in s na~
	{
		if(testin.substr(start_testing,1).compare("(")==0)//found (
		{
			if(checkgr(testin.substr(start_testing+1,testin.find(')',start_testing+1)-start_testing-1),s.substr(i,1))==0)//check group failed
			{
				return 0;
			}
			start_testing=testin.find(')',start_testing+1)+1;
		}
		else//te la tua
		{
			if(testin.substr(start_testing,1).compare(s.substr(i,1))!=0)//not equal so mean failed
			{
				return 0;
			}
			start_testing++;
		}
		//else// check t la tua
	}
	return 1;
}
int checks(string testin)//return in number
{
	int x=0;
	std::list<string*>::iterator itr;
	for (itr = str_list.begin(); itr != str_list.end(); ++itr)//get all in list
	{
		string s=(*itr)->substr(0,(*itr)->length());
		//cout<<"comparing word = "<<s<<endl;
		//(*itr)->copy(s,(*itr)->length(),0);
		if(checkw(testin,s))
		{
			//cout<<" increase x "<<endl;
			x++;
		}
		//cout<<" inc itr"<<endl;
	}
	return x;
}
int main()
{  
	//test field
	//string tss="avbsdf";
	//cout<<tss.find('1',0,tss.length())<<endl<<endl;
	//EO test

	ifstream myfile;
	ofstream outfile;
	outfile.open("out_large.txt");
	myfile.open ("A-large.in");

	l=0;d=0;n=0;//init

	if (myfile.is_open())
	{
		while (! myfile.eof())
		{
			//getline (myfile,line/*, ' '*/);
			//
			myfile>>l;//length
			myfile>>d;//d word
			myfile>>n;//test
			for(int i=0;i<d;i++)//input
			{
				string *s = new string();
				myfile>>*s;
				str_list.push_back(s);
			}

			string inp;
			for(int i=1;i<=n;i++)
			{
				myfile>>inp;
				if(inp.compare("")!=0)
				{
					cout<<"Case #"<<i<<": "<<checks(inp)<<endl;
					outfile<<"Case #"<<i<<": "<<checks(inp)<<endl;
				}
			}
		}
		myfile.close();
	}
	outfile.close();
	getch();
	//cout<<l*d*n<<endl;
	return 0;
}