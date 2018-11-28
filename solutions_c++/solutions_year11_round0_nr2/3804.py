#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
using namespace std;
typedef unsigned long long LLU;
typedef long long LL;
typedef pair<int,int> pii;
const int INF=99999999;
const double PI=3.1415926535897932384626;
const double EPS=1E-11;
char nchar()
{
	char c;
	while(isspace(c=getchar()));
	return c;
}
char form[256][256];
bool destroy[256][256];
bool check(vector<char>& v)
{
	for(int i=0;i<v.size();i++)
	{
		for(int j=i+1;j<v.size();j++)
			if(destroy[v[i]][v[j]])
				return true;
	}
	return false;
}
int main()
{
	freopen("test.in","r",stdin); freopen("test.out","w",stdout);
	int testn;
	char str[200];
	scanf("%d",&testn);
	for(int tn=1;tn<=testn;tn++)
	{
		memset(form,-1,sizeof(form));
		memset(destroy,0,sizeof(destroy));
		int m,n;
		scanf("%d",&m);
		for(int i=0;i<m;i++)
		{
			int a=nchar();
			int b=nchar();
			int c=nchar();
			form[a][b]=c;
			form[b][a]=c;
			
		}
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			int a=nchar();
			int b=nchar();
			destroy[a][b]=true;
			destroy[b][a]=true;
		}
		int len;
		scanf("%d",&len);
		scanf("%s",str);
		vector<char> elements;
		for(int i=0;i<len;i++)
		{
			elements.push_back(str[i]);
			while(elements.size()>=2)
			{
				int tc=form[elements.back()][elements[elements.size()-2]];
				if(tc!=-1)
				{
					elements.pop_back();
					elements.pop_back();
					elements.push_back((char)tc);
				}
				else
					break;
			}
			if(check(elements))
				elements.clear();
		}
		printf("Case #%d: ",tn);
		if(elements.size()==0)
			printf("[]");
		else
		{
			printf("[%c",elements[0]);
			for(int i=1;i<elements.size();i++)
				printf(", %c",elements[i]);
			printf("]");
		}
		printf("\n");
	}
}
