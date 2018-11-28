#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;
map<string,int>Count;
vector<string> engineername;
int i,j,k,Case,s,q,Result,t;
char str1[101];
string str;
void setzero()
{
	for(j=0;j<engineername.size();j++)
	{
		Count[engineername[j]]=0;
	}
}
void input()
{
	for(i=0;i<s;i++)
	{
		gets(str1);
		str=str1;
		Count[str]=0;
		engineername.push_back(str); 
	}
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);	
	scanf("%d",&Case);
	gets(str1);
    for(k=0;k<Case;k++)
	{
		Count.clear();
		engineername.clear();
		scanf("%d",&s);
		gets(str1);
		input();
		Result=0;
		t=0;
		scanf("%d",&q);
		gets(str1);
		for(i=0;i<q;i++)
		{
			gets(str1); 
			str=str1;
			if(Count[str]==0)
			{
				t++;
				if(t==s)
				{
					setzero();
					t=1;
					Result++;
				}	
				Count[str]=1;
			}
		}	
		printf("Case #%d: %d\n",k+1,Result);	
	}
	return 0; 
}