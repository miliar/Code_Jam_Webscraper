#include "stdafx.h"
#include <set>
#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<string> a;
int L,D,N;
int ans=0;

int main()
{

	freopen("A-small.in","rt",stdin);
	freopen("A-small.out","wt",stdout);

	
	scanf("%d%d%d\n",&L,&D,&N);
	a.resize(D);
	
	for(int i=0;i<D;i++)
	{
		cin>>a[i];
	}

	
	for(int i=0;i<N;i++)
	{
		vector<int> not(D);
		ans=0;
		string s;
		cin>>s;
		int p=0;		
		for(int j=0;j<s.length();j++)
		{
			vector<char> cur;
			if (s[j]=='(')
			{
				for(;s[j]!=')';j++)
					cur.push_back(s[j]);
			}
			else
				cur.push_back(s[j]);
			for(int k=0;k<D;k++)
			{
				bool good=0;
				for(int r=0;r<cur.size();r++)
					if (a[k][p]==cur[r])
						good=1;
				if (!good)
					not[k]=1;
			}
			p++;
		}
		for(int j=0;j<D;j++)
			if (not[j]==0)
				ans++;
		printf("Case #%d: %d\n",i+1,ans);
	}


	return 0;
}