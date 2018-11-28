#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <cstdlib>
#include <stdlib.h>
#include <stack>
#include <cstdio>
#include <map>
#include <cmath>
#include <time.h>
using namespace std;

#define MAX(a,b) ((a>=b)?a:b)
#define MIN(a,b) ((a<=b)?a:b)
#define ABS(a) ((a<0)?-(a):a)

set<string> S;
vector<string> mas;
int main()
{
	//freopen("in.txt","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("out2.out","w",stdout);
	int T;
	scanf("%d",&T);
	int n,m,count;
	string s;
	for(int t=0;t<T;++t)
	{
		scanf("%d %d",&n,&m);
		S.clear(); mas.clear();
		for(int i=0;i<n;++i){cin >>s; mas.push_back(s);}
		for(int j=0;j<mas.size();++j)
			for(int i=1;i<mas[j].size();++i)
			{
				if(mas[j][i]=='/')
				{
					s=mas[j].substr(0,i);
					if(S.find(s)==S.end())S.insert(s);
				}
				else if(i+1==mas[j].size())
				{
					s=mas[j].substr(0,i+1);
					if(S.find(s)==S.end())S.insert(s);
				}
			}
		mas.clear();
		for(int i=0;i<m;++i){cin >>s; mas.push_back(s);}
		count=0;
		for(int j=0;j<mas.size();++j)
			for(int i=1;i<mas[j].size();++i)
			{
				if(mas[j][i]=='/')
				{
					s=mas[j].substr(0,i);
					if(S.find(s)==S.end()){S.insert(s); ++count;}
				}
				else if(i+1==mas[j].size())
				{
					s=mas[j].substr(0,i+1);
					if(S.find(s)==S.end()){S.insert(s); ++count;}
				}
			}
		printf("Case #%d: ",t+1);
		printf("%d\n",count);
	}
	return 0;
}