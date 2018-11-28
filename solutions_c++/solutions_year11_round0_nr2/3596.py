#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<list>
#include<queue>
#include<cctype>
#include<stack>
#include<map>
#include<set>
using namespace std;


bool combine(string & s, vector<string> & combine)
{
	if(s.size()<2)
		return false;
	for(int i=0;i<combine.size();i++)
	{
		if(combine[i][0]==s[s.size()-2] && combine[i][1]==s[s.size()-1] ||combine[i][0]==s[s.size()-1] && combine[i][1]==s[s.size()-2])
		{
			s=s.substr(0,s.size()-2);
			s+=combine[i][2];
			return true;
		}	
	}
	return false;
}

void cleanup(string & s,vector<string> & oppose)
{
	if(s.size()<2)
		return;
	for(int i=0;i<oppose.size();i++)
	{
		if(oppose[i][0]==s[s.size()-1])
		{
			for(int j=0;j<s.size()-1;j++)
			{
				if(s[j]==oppose[i][1])
				{
					s="";
					return;
				}
			}
		}
		else if(oppose[i][1]==s[s.size()-1])
		{
			for(int j=0;j<s.size()-1;j++)
			{
				if(s[j]==oppose[i][0])
				{
					s="";
					return;
				}
			}
		}
	}

}





int main()
{
	int t;	
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		int c,d,n;
		cin>>c;

		vector<string> combineString(c);
		for(int i=0;i<c;i++)
		{
			cin>>combineString[i];
		}
		cin>>d;

		vector<string> opposedString(d);
		for(int i=0;i<d;i++)
		{
			cin>>opposedString[i];
		}
		cin>>n;
		string s="";
		for(int i=0;i<n;i++)
		{
			//cout<<"Here\n";
			char ch;
			cin>>ch;
			s+=ch;	
			while(combine(s,combineString));
			cleanup(s,opposedString);


		}
		//cout<<s<<endl;		

		string out="[";
		for(int i=0;i<s.size();i++)
		{
			if(i==0)
				out+=s[0];
			else
			{
				out+=", ";
				out+=s[i];
			}
		}
		out+=']';
		printf("Case #%d: %s\n",k,out.c_str());
	}

return 0;
}	
