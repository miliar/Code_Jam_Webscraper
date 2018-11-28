#include "utils.h"
#include <iostream>
#include <string>

using namespace std;

enum _V
{
	Start,
	P_Open,
	P_Open_Matched,
	Matched
};

bool isValid(string word,string pattern)
{
	int state=Start;
	for(int i=0,j=0;i<word.length() && j<pattern.length();)
	{
		char a=word.at(i);
		char b=pattern.at(j);
		switch(state)
		{
		case Start:
			if(b=='(')
			{
				state=P_Open;
				j++;				
			} else if(a==b)
			{
				i++;
				j++;				
			} else
				return false;
			break;
		case P_Open:
			if(a==b)
			{
				state=P_Open_Matched;
				i++;
				j++;
			} else if(b==')')
			{
				return false;
			} else
				j++;
			break;
		case P_Open_Matched:
			if(b==')')
			{
				state = Start;
			}
			j++;
			break;
		case Matched:
			break;
		default:
			return false;
		}
	}
	return true;
}

int main(int argc, char **argv)
{
	if(argc!=2)
	{
		cout<<"Usage: <prog> <input_file>"<<endl;
		return 1;
	}

	argument arg(argv[1]);
	argLine a = arg.getLine(0);
	int L=a.getInt();
	int D=a.getInt();
	int N=a.getInt();

	vector<string> w,p;
	int i=1,j;
	for(;i<=D;i++)
		w.push_back(arg.getLine(i).getStr());
	for(;i<=D+N;i++)
		p.push_back(arg.getLine(i).getStr());
	for(j=0;j<p.size();j++)
	{
		int count=0;
		for(i=0;i<w.size();i++)
			if(isValid(w[i],p[j]))
				count++;
		cout<<"Case #"<<j+1<<": "<<count<<endl;
	}
	return 0;
}