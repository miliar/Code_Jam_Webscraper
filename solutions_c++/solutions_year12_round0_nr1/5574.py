#include<iostream>
#include<fstream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<stack>
#include<queue>
#include<algorithm>
#include<string>
#include<map>
#include<limits.h>

using namespace std;

map <char,char> mapping;

void buildMapping()
{
	string a="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv",
	amap="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	mapping['z']='q';
	mapping['q']='z';
	mapping['o']='e';
	mapping['a']='y';
	
	for ( int i = 0; i < a.length(); i++ )
	{
		mapping[a[i]]=amap[i];
	}
	
}

int main (int argc, char const* argv[])
{
	int n=0,i=1;
	string ip;
	char str[256],c;
	
	ifstream cin("A-small-attempt0.in");
	ofstream file("output.txt");
	
	cin>>n;
	buildMapping();
	
	while(c!='EOF' && i<=n+1)
	{
		c=cin.get();
		if (c==' ')	file<<c;
		else if(c=='\n')	
		{
			if(i>1)	file<<endl;
			if(i<=n)	file<<"Case #"<<i++<<": ";
			else break;
		}
		else	file<<mapping[c];
		
	}
	
	return 0;
}
