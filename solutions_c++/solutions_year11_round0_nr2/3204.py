/**************************************************
#		Author Xue Nan
#		Email: xuenan199@gmail.com
#
#		Last modified: 2011-05-07 22:07
#
#		Filename: B.cpp
#		Description: 
**************************************************/
#include <iostream>
#include <vector>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <queue>
#include <cmath>
#include <algorithm>
using namespace std;

int C,D;
string s;
char comp['Z'+1]['Z'+1];
bool op['Z'+1]['Z'+1];
int main(int argc,char *argv[])
{
	int Tcase,Case=0;
	cin>>Tcase;
	while(Tcase--)
	{
		Case++;
		cin>>C;
		memset(comp,0,sizeof(comp));
		memset(op,0,sizeof(op));
		for(int i=0;i<C;i++)
		{
			char x,y,z;
			cin>>x>>y>>z;
			comp[x][y]=comp[y][x]=z;
		}
		cin>>D;
		for(int i=0;i<D;i++)
		{
			char x,y;
			cin>>x>>y;
			op[x][y]=op[y][x]=1;
		}
		cin>>D;
		cin>>s;
		string t="";
		for(int i=0;i<s.size();i++)
		{
			t+=s[i];
			if(t.size()<2) continue;
			while(comp[t[t.size()-1]][t[t.size()-2]])
			{
				char tmp=comp[t[t.size()-1]][t[t.size()-2]];
				t=t.substr(0,t.size()-1);
				t[t.size()-1]=tmp;
			}
			bool flag=true;
			for(int j=0;j<t.size();j++)
			{
				for(int k=0;k<t.size();k++)
				{
					if(j==k) continue;
					if(op[t[j]][t[k]])
					{
						t.clear();
						flag=false;
						break;
					}
				}
				if(!flag) break;
			}
		}
		printf("Case #%d: ",Case);
		if(t.size()==0)
		{
			cout<<"[]"<<endl;
			continue;
		}
		cout<<'['<<t[0];
		for(int i=1;i<t.size();i++)
			cout<<", "<<t[i];
		cout<<']'<<endl;
	}
	return 0;
}
