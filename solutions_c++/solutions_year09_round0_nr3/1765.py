#include "utils.h"
#include <stdio.h>
#include <string>

using namespace std;

int subseq(string str,string s)
{
	if(str.length()<s.length())
		return 0;
	if(str==s)
		return 1;
	if(s.length()==1)
	{
		int cnt=0;
		for(int i=0;i<str.length();i++)
			if(str.at(i)==s.at(0))
				cnt++;
		return cnt%10000;
	}
	
	int ret=0;
	for(int i=0;i<str.length()-s.length()+1;i++)
	{
		if(str.at(i)==s.at(0))
		{
			ret += subseq(str.substr(i+1),s.substr(1));
			ret %= 10000;
		}
	}
	return ret;
}


int main(int argc, char **argv)
{
	if(argc!=2)
	{
		printf("Usage: <prog> <input_file>\n");
		return 1;
	}

	argument arg(argv[1]);
	argLine a = arg.getLine(0);
	int numTC = a.getInt();
	string search("welcome to code jam");

	for(int i=1;i<=numTC;i++)
	{
		printf("Case #%d: %04d\n",i,subseq(arg.getLine(i).getFullStr(),search));
	}
	
	return 0;
}