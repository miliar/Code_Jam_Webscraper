//Grzegorz Prusak
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;

#define REP(i,n)    for(register int i=0; i<(n); ++i)
#define FOR(i,p,k)  for(register int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(register int i=(p); i>=(k); --i)

void get(int n, vector<string> &v)
{
	REP(i,n)
	{
		char buffer[200];
		scanf(" %s",buffer);
		v.push_back(buffer);
		char *p = buffer+strlen(buffer);
		while(--p!=buffer) if(*p=='/'){ *p = 0; v.push_back(buffer); }
	}
}

int main()
{
	int t; scanf("%d",&t); REP(x,t)
	{
		int n,m; scanf("%d%d",&n,&m);
		vector<string> v1,v2;
		get(n,v1); get(m,v2);
		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end());
		int res = 0;
		int j=0; REP(i,v2.size())
		{
			if(i<v2.size()-1 && v2[i]==v2[i+1]) continue;
			while(j<v1.size() && v1[j]<v2[i]) j++;
			if(j==v1.size() || v1[j]!=v2[i]) res++;
		}
		printf("Case #%d: %d\n",x+1,res);
	}

	return 0;
}

