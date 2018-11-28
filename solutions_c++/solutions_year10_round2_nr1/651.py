#define PATH "/home/tushar/Desktop/"
#define INPUTFILE PATH "A-large.in" 
#define OUTPUTFILE PATH "A-large.out"

#include <vector>
#include <cassert>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>

using namespace std;
map<string,bool> Val;
int main()
{
	assert (freopen (INPUTFILE, "r", stdin));
	assert (freopen (OUTPUTFILE, "w", stdout));
	
	int T,N,M;
	string inp,word;
	cin>>T;
	for(int k=1;k<=T;++k)
	{
		cin>>N>>M;
		Val["/"] = true;
		for(int i=0;i<N;++i)
		{
			cin>>inp;
			inp += "/";
			Val[inp] = true;
			word = "";
			for(int j=0;j<inp.size();++j)
			{
				word += inp[j];
				if(inp[j] == '/' && !Val[word])Val[word]=true;
				}
			}
		int count=0;
		for(int i=0;i<M;++i)
		{
			cin>>inp;
			inp += "/";
			if(!Val[inp])
			{
				Val[inp] = true,count++;
				word = "";
				for(int j=0;j<inp.size();++j)
				{
					word += inp[j];
					if(inp[j] == '/' && !Val[word])Val[word]=true,count++;
					}
				}
			}
		cout<<"Case #"<<k<<": "<<count<<endl;
		Val.clear();
		}
	return 0;
	}
