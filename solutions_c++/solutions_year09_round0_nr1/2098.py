#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

int L,D,N;
string dict[5005],token;

bool haschar(string str,char c)
{
	for(int i=0;i<str.length();i++)
		if(str[i]==c) return true;
	return false;
}

int solve()
{
	int i,j=0,ans=0;
	string query[20];
	
	for(i=0;i<token.length();i++)
	{
		if(token[i]=='(')
		{
			i++;
			string temp="";
			while(token[i]!=')') temp+=token[i++];
			query[j++]=temp;
		}
		else
		{
			string temp="";
			temp+=token[i];
			query[j++]=temp;
		}
	}
	for(i=0;i<D;i++)
	{
		int len=dict[i].length();
		if(len==L)
		{
			bool ok=true;
			for(j=0;j<len;j++)
			{
				if(haschar(query[j],dict[i][j])==false){ok=false;break;}
			}
			if(ok) ans++;
		}
	}
	return ans;	
}
			
int main()
{
	int i;
	cin>>L>>D>>N;
	char garbage=getchar();

	for(i=0;i<D;i++) getline(cin,dict[i]);
	
	for(i=1;i<=N;i++)
	{
		getline(cin,token);
		printf("Case #%d: %d\n",i,solve());
	}
	return 0;
}
