/*
 * =====================================================================================
 *
 *       Filename:  template.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  09/13/2009 12:52:20 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Bharath (IISc), ajeetbharath@gmail.com
 *        Company:  Texas Instruments
 *
 * =====================================================================================
 */
#include<iostream>
#include<fstream>
#include<string>
#include<cmath>

typedef unsigned int UINT;
typedef int INT;

using namespace std;

ifstream fin;
ofstream fout;

static string foundList;
static string opString;

void processCase()
{
	int i,n,base;
	long seconds=0;
	string str;
	fin>>str;

	foundList.clear();
	opString.clear();

	for(i=0;i<str.size();i++)
	{
		n=foundList.find(str[i]);
		if(n!=string::npos)
		{
		//	cout<<"Found at "<<n<<endl;
		}
		else
		{
			n=foundList.size();
			foundList+=str[i];
		}

		if(n==0)
			opString+='1';
		else if(n==1)
			opString+='0';
		else
			opString+='0'+n;
		//if(found(str[i]))
		//{
		//	
		//}
		//else
		//{
		//	addToList(str[i]);
		//}
	}	
	//cout<<opString;
	base=foundList.size();
	if(base<=1)
		base++;
	for(i=0;i<opString.size();i++)
		seconds+=(opString[i]-'0')*pow(base,opString.size()-(i+1));
	fout<<seconds;

}

int main(int argc,char* argv[])
{
	UINT i,T;

	if(argc<3)
	{
		cout<<"Usage: "<<argv[0]<<" "<<"<input file> "<<"<output file>"<<endl;
		return 1;
	}

	fin.open(argv[1]);
	fout.open(argv[2]);
	fin>>T;
	for(i=1;i<=T;i++)
	{
		fout<<"Case #"<<i<<": ";
		cout<<"Case #"<<i<<": ";
		processCase();
		fout<<endl;
		cout<<endl;
	}
	return 0;
}

