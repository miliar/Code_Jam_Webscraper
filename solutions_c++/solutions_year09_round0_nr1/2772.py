#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <cstring>
using namespace std;

int main()
{
	int l,d,n;
	vector<string> str;
	bool token[20][26];
	string t;
	cin>>l>>d>>n;

	for(int i=1;i<=d;i++)
	{
		cin>>t;
		str.push_back(t);
	}

	for(int i=0;i<n;i++)
	{
		memset((void*)token, 0, sizeof(bool)*20*26);
		cin>>t;
		int index=0;
		int para=0;
		int count=0;
		bool ok=false;
		for(int j=0;j<t.length();j++)
		{
			if(t[j]=='(') para=1;
			else if(t[j]==')') para=0, index++;
			else
			{
				token[index][t[j]-'a']=true;
				if(para==0) index++;
			}
		}
		for(vector<string>::iterator it=str.begin();it!=str.end();it++)
		{
			ok=true;
			for(int j=0;j<l;j++)
			{
				if(token[j][(*it)[j]-'a']==false)
				{
					ok=false;
					break;
				}
			}
			if(ok) count++;
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	return 0;
}
