#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<cctype>
#include<cstdio>
#include<vector>
#include<fstream>

using namespace std;

vector <string> s;

int main()
{
	fstream fin("input.in");
	fstream fout("ans.in");
	int L,D,N;
	fin>>L;
	fin>>D;
	fin>>N;
	s.resize(D);
	for(int i=0;i<D;i++) 
	{
		fin>>s[i];
	}
	int ct=0;
	while(N--)
	{
		int ans=0;
		vector < vector <char> > a;
		a.resize(L);
		string temp="";
		fin>>temp;
		int pos=0,found=0;
		for(int i=0;i<temp.size();i++)
		{
			if(temp[i]=='(') found=1;
			else if(temp[i]==')')
			{ 
				pos++;
				found=0;
			}
			else
			{
				a[pos].push_back(temp[i]);
				if(found==0) pos++;
			}
		}		
		for(int i=0;i<s.size();i++)
		{
			int counter=0,flag=0;
			for(int j=0;j<s[i].size()&&flag==0;j++)
			{
				int check=0;
				for(int k=0;k<a[j].size()&&check==0;k++)
				{
					if(s[i][j]==a[j][k])
					{
						counter++;
						check=1;
					}
				}
				if(check=0) flag=1;
			}
			if(counter==L&&flag==0) ans++;
		}
		ct++;
		//cout<<"Case #"<<ct<<": "<<ans<<endl;			
		fout<<"Case #"<<ct<<": "<<ans<<endl;
	
	}						
return 0;
}	
