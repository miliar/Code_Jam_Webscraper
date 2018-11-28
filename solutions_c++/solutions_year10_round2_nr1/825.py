#include <map>
#include <cmath>
#include <vector>
#include <string>
#include <cstdio>
#include <cstring>
#include <utility>
#include <iostream>
#include <algorithm>
#define CASEID printf("Case #%d: ",iD++)
#define CASES  for(scanf("%d",&cases);cases--;)
using namespace std;

int N,M;
string exist,create;
map<string,bool>ok;

int main()
{
	int cases,iD=1;
	
	CASES
	{
		cin>>N>>M;
		ok.clear();
		ok["/"]=true;

		for(int i=0;i<N;i++)
		{
			cin>>exist;
			exist+="/";
			string tmp="";
			for(int j=0;j<exist.length();j++)
			{
				tmp+=exist[j];
				if(exist[j]=='/')
					ok[tmp]=true;
			}
		}
		int cnt=0;
		for(int i=0;i<M;i++)
		{
			cin>>create;
			create+="/";
			string tmp="";
			for(int j=0;j<create.length();j++)
			{
				tmp+=create[j];
				if(create[j]=='/')
				{
//					cout<<tmp<<endl;
					if(!ok[tmp])
					{
						cnt++;
						ok[tmp]++;
					}
				}
			}
		}
		CASEID;
		printf("%d\n",cnt);
	}
	return 0;
}

