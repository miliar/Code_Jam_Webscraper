#include<cstdio>
#include<string>
#include<vector>
#include<iostream>
using namespace std;
vector<string> ValidWords(5000);
int L,D,N;
int solve(string a)
{
	vector<string>Current(20);
	int res=0;
	int c=0;
	bool brace=false;
	for(int i=0;i<a.length();++i)
	{
		if(a[i]=='(')
		{
			brace=true;
			continue;
		}
		else if(a[i]==')')
		{
			brace=false;
			c++;
		}
		else if(a[i]<='z' && a[i]>='a')
		{
			Current[c]+=a[i];
			if(!brace)
				c++;
		}
	}
	for(int i=0;i<D;++i)
	{
		bool ok=true;
		for(int j=0;j<ValidWords[i].length();++j)
		{
			if(Current[j].find(ValidWords[i][j],0)==-1)
				ok=false;
		}
		if(ok)
			res++;
	}
	return res;
}

int main()
{
	freopen("a.in","r",stdin) ;
	freopen("out.txt","w",stdout) ;
	scanf("%d %d %d",&L,&D,&N);
	for(int i=0;i<D;++i)
		cin>>ValidWords[i];
	string temp="";
	int res=0;
	for(int i=0;i<N;++i)
	{
		cin>>temp;
		res=solve(temp);
		printf("Case #%d: %d\n",i+1,res);
	}
	return 0;
}