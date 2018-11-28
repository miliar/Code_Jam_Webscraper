#include<stdio.h>
#include<algorithm>
#include<map>
#include<vector>
using namespace std;
void process()
{
	int in,im,io,n;
	map<pair<char,char> ,char > mp,dis;
	vector<int>::iterator it,it2;
	vector<int> dq;
	scanf("%d",&in);
	char str[2000];
	for(n=0;n<in;n++)
	{
		scanf("%s",str);
		mp[make_pair(str[0],str[1])]=str[2];
		mp[make_pair(str[1],str[0])]=str[2];
	}
	scanf("%d",&im);
	for(n=0;n<im;n++)
	{
		scanf("%s",str);
		dis[make_pair(str[0],str[1])]=1;
		dis[make_pair(str[1],str[0])]=1;
	}
	scanf("%d",&io);
	scanf("%s",str);
	for(n=0;n<io;n++)
	{
		if((!dq.empty())&&mp[make_pair(str[n],dq.back())]!=0)
		{
			char t=dq.back();
			dq.pop_back();
			dq.push_back(mp[make_pair(str[n],t)]);
		}
		else
		{
			it2=dq.end();
			for(it=dq.begin();it!=dq.end();it++)
			{
				if(dis[make_pair(*it,str[n])])
				{
					it2=it;
				}
			}
			if(it2!=dq.end())
			{
				dq.clear();
			}
			else
			{
				dq.push_back(str[n]);
			}
		}
	}
	printf("[");
	for(it=dq.begin();it!=dq.end();it++)
	{
		if(it!=dq.begin())
			printf(", ");
		printf("%c",*it);
	}
	printf("]\n");
}
int main()
{
	int ix,n;
	scanf("%d",&ix);
	for(n=0;n<ix;n++)
	{
		printf("Case #%d: ",n+1);
		process();
	}
}
