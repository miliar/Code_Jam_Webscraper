//#include "stdafx.h"
#include <vector>
#include <string>
#include <fstream>
using namespace std;
std::ifstream in ("input");
std::ofstream out("output");
int d,l,n;
bool _in(string str, vector<string> vs)
{
	int i,j;
	for(i=0;i<l;i++)
	{
		for(j=0;j<vs[i].size();j++)
			if(str[i]==vs[i][j]) break;
		if(j==vs[i].size())return false;
	}
	return true;
}
int _tmain(int argc, _TCHAR* argv[])
{
	vector<string> vs; //список слов
	vector<string> sh; //лексема
	string str;
	int i,j,count;
	char c;
	in>>l>>d>>n;
	for(i=0;i<d;i++)
	{
		in>>str;
		vs.push_back(str);
	}
	for(i=0;i<n;i++)
	{
		sh.erase(sh.begin(),sh.end());
		for(j=0;j<l;j++)
		{
			str="";
			in>>c;
			if(c=='(')
			{
				in>>c;
				while(c!=')')
				{
					str+=c;			
					in>>c;
				}
			}else
			{
				str=c;
			}
			sh.push_back(str);
		}
		count=0;
		for(j=0;j<d;j++)
		{
			if(_in(vs[j],sh)) count++;
		}
		out<<"Case #"<<i<<": "<<count<<'\n';
	}
	in.close();
	out.close();
	return 0;
}

