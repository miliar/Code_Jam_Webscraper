#include <iostream>
#include <stdio.h>
#include <fstream>
using namespace std;
ofstream fout ("numtri.out");
ifstream fin ("A-large.in");
bool mat[20][30];
char str[5100][20];
int main()
{
	int L,D,N,i,j,k,ct;
	char t;
	fin>>L>>D>>N;
	for(i=0;i<D;++i)
		fin>>str[i];
	for(i=0;i<N;++i)
	{
		memset(mat,0,sizeof(mat));
		for(j=0;j<L;++j)
		{
			fin>>t;
			if(t=='(')
			{
				while(fin>>t)
				{
					if(t==')')
						break;
					else 
						mat[j][t-'a']=1;
				}
			}
			else
			{
				mat[j][t-'a']=1;
			}
		}
		ct=0;
		for(j=0;j<D;++j)
		{
			for(k=0;k<L;++k)
			{
				if(!mat[k][str[j][k]-'a'])
					break;
			}
			if(k==L)
			{
				ct++;
			}
		}
		fout<<"Case #"<<i+1<<": "<<ct<<endl;
	}
	return 0;	
}