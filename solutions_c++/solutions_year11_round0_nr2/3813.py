#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<fstream>
#include<string>

using namespace std;

#define MAXN 110

int C,D,N;

string str,list;
string com[MAXN],opp[MAXN];

ifstream fin("B-small-attempt0.in");
ofstream fout("B-small-attempt0.out");

void solve()
{
	int i,j,k,len;
	list="";
	for(i=0;i<N;i++)
	{
		list+=str[i];
		len=list.length();
		j=C;
		if(len>1)
		{
			for(j=0;j<C;j++)
			{
				if((list[len-1]==com[j][0] && list[len-2]==com[j][1]) || 
				(list[len-1]==com[j][1] && list[len-2]==com[j][0]))
				{
					break;
				}
			}
		}
		if(j!=C)
		{
			list.erase(len-2,2);
			list+=com[j][2];
		}
		for(j=0;j<D;j++)
		{
			if(list.find(opp[j][0])!=-1 && list.find(opp[j][1])!=-1)
			{
				break;
			}
		}
		if(j!=D)
		{
			list.erase();
		}
	}
}

int main()
{
	int ct,text;
	fin>>text;
	for(ct=1;ct<=text;ct++)
	{
		int i,j;
		fin>>C;
		for(i=0;i<C;i++) fin>>com[i];
		fin>>D;
		for(j=0;j<D;j++) fin>>opp[j];
		fin>>N>>str;
		solve();
		fout<<"Case #"<<ct<<": [";
		j=list.length();
		if(j!=0) fout<<list[0];
		for(i=1;i<j;i++)
		{
			fout<<", "<<list[i];
		}
		fout<<"]"<<endl;
	}
	return 0;
}
