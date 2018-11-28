#include<iostream>
#include<cstdio>
#include<stack>
#include<queue>
#include<cctype>
#include<string>
#include<vector>
#include<cmath>
#include<algorithm>
#include<fstream>
#include<map>

using namespace std;

int main()
{
	freopen("input.txt.txt","r",stdin);
	freopen("ans.txt","w",stdout);
	int t;
	cin>>t;
	map < char, int > m;
	//m.resize(62);
	cin.get();
	int ct=1;
	while(t--)
	{
		string s;
		getline(cin,s);
		int counter=1,check=0;
		//for(int i=0;i<m.size();i++) cout<<m[i]<<" ";
		for(char i='a';i<='z';i++) m[i]=-1;
		for(char i='0';i<='9';i++) m[i]=-1;
		for(int i=0;i<s.size();i++)
		{
			if(m[s[i]]==-1&&counter==2&&check==0)
			{
				m[s[i]]=0;
				check=1;
				//cout<<check<<endl;
			}	 
			else if(m[s[i]]==-1)
			{
				m[s[i]]=counter;
				counter++;
			}
		}
		long long ans=0;
		int x=s.size()-1;
		if(counter<2) counter=2;
	//	  cout<<counter<<endl;
		for(int i=0;i<s.size();i++)
		{
			 //cout<<m[s[i]]<<" ";
			 ans=ans+m[s[i]]*(int)(pow((double) counter,(double)(x-i))+0.01);
			 //cout<<ans<<endl;
		}
		//cout<<s<<endl;	 
		cout<<"Case #"<<ct<<": "<<ans<<endl; 
		m.clear();
		ct++;	 	 
	}	 	    
	
	return 0;
}

