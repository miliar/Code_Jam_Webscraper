// Alien_Language.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <set>
#include <vector>
using namespace std;

int L,D,N;
int main()
{
	int result;
	int i,j,k,m,n;
	char ch;
	int pos,len;
	string str;
	vector<string> example,test;
	fstream in,out;
	in.open("A-large.in",ios::in);
	out.open("A-large.out",ios::out);
	in>>L>>D>>N;
	bool **flag = new bool*[D];
	for(i=0;i<D;i++)
		flag[i] = new bool[L];

	string * pstr = new string[L];
	for(i=0;i<D;i++)
	{
		in>>str;
		example.push_back(str);
	}
	for(i=0;i<N;i++)
	{
		in>>str;
		for(k=0;k<D;k++)
			for(j=0;j<L;j++)
				flag[k][j]=false;
		k=0;
		pos=0;len=0;
		for(j=0;j<str.size();j++)
		{
			if(str[j]=='(')
			{
				len=0;
				pos=j++;
				while(str[j]!=')')
				{
					j++;
					len++;
				}
				pstr[k++]=str.substr(pos+1,len);
			}
			else
				pstr[k++]=str[j];
		}
//				for(j=0;j<L;j++)
//					out<<pstr[j]<<endl;

		for(j=0;j<L;j++)
		{
			if(j==0)
			{
				for(k=0;k<pstr[j].size();k++)
				{
					for(m=0;m<example.size();m++)
					{
						if(example[m][j]==pstr[j][k])
							flag[m][j]=true;
					}
				}
			}
			else
			{
				for(k=0;k<pstr[j].size();k++)
				{
					for(m=0;m<example.size();m++)
					{
						if(flag[m][j-1] && example[m][j]==pstr[j][k])
							flag[m][j]=true;
					}
				}
			}
		}	
		result=0;
		for(j=0;j<example.size();j++)
			if(flag[j][L-1]==true)
				result++;
		out<<"Case #"<<i+1<<": "<<result<<endl;
	}

	out.close();
	in.close();
	return 0;
}

