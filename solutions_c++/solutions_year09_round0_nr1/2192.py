#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
using namespace std;
int L,D,N;


int parse(string s,vector<string> dict)
{
	vector<string> V;
	int length=s.length();
	int index=0,count=0;
	vector<bool> flag(D,true);
	for(int i=0;i<length;i++)
	{
		if(s[i]=='(')
		{
			vector<bool> present(26,false);
			i++;
			present[s[i]-97]=true;
			while(s[i]!=')')
			{
				present[s[i]-97]=true;
				i++;
			}
			for(int j=0;j<D;j++)
			{
				if(!present[dict[j][index]-97])
					flag[j]=false;	
			}
		}
		else
		{
			for(int j=0;j<D;j++)
			{
				if(dict[j][index]!=s[i])
					flag[j]=false;	
			}

		}
		index++;
	}

	for(int i=0;i<D;i++)
	{
		if(flag[i])
			count++;	
	}
	return count;
}



int main()
{
	cin>>L>>D>>N;
	string s;
	vector<string> V;
	vector<string> dict;
	for(int i=0;i<D;i++)
	{
		cin>>s;
		dict.push_back(s);
	}
	for(int i=0;i<N;i++)
	{
		cin>>s;
		cout<<"Case #"<<i+1<<": "<< parse(s,dict)<<'\n';
	}
	return(0);
}
