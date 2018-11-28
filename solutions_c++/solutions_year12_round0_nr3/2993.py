#include <sstream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
vector<string> dp;
void generate(int size,int pos=0,string str="")
{
	if(size==pos)
	{
		dp.push_back(str);
		return;
	}
	if(str.size()<size)
		str+=' ';
	if(pos==0&&size<7)
	{
		for(char i='1';i<='9';i++)
		{		
			str[pos]=i;
			generate(size,pos+1,str);
		}
	}
	else if(pos==0&&size==7)
	{
		for(char i='1';i<='2';i++)
		{		
			str[pos]=i;
			generate(size,pos+1,str);
		}
	}
	else
	{
		for(char i='0';i<='9';i++)
		{		
			str[pos]=i;
			generate(size,pos+1,str);
		}
	}
}

void main()
{
	
	for(int i=1;i<=7;i++)
	{
		generate(i);
		stringstream strm;
		strm<<i<<".in";
		ofstream cout(strm.str().c_str());
		for(int j=0;j<dp.size();j++)
		{
			cout<<dp[j]<<' ';
		}
		dp.clear();
	}
}