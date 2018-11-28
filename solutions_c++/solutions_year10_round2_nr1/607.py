#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <map>
using namespace std;
int main()
{
	freopen("g1.in","r",stdin);
	freopen("g1.out","w",stdout);
	int t;
	scanf("%d",&t);
	int i,j,k;
	char sent[150];
	string sen;
	string temp;
	int n,m;
	int cnt;
	for (i = 1;i <= t;i++)
	{
		cnt = 0;
		map<string,int> mymap;
		scanf("%d%d",&n,&m);
		for (j= 1;j <= n;j++)
		{
			scanf("%s",sent);
			int len = strlen(sent);
			for (k = 1;k < len;k++)
			{
				if (sent[k] == '/')
				{
					sent[k] = '\0';
					temp = sent;
					if (mymap.count(temp) == 0)
					{
						mymap[temp] = 1;
					}
					sent[k] = '/';
				}
			}
			temp = sent;
			if (mymap.count(temp) == 0)
			{
				mymap[temp] = 1;
			}
		}
		for (j = 1;j <= m;j++)
		{
			scanf("%s",sent);
			int len1 = strlen(sent);
			for (k = 1;k < len1;k++)
			{
				if (sent[k] == '/')
				{
					sent[k] = '\0';
					temp = sent;
					if (mymap.count(temp) == 0)
					{
						mymap[temp] = 1;
						cnt ++;
					}
					sent[k] = '/';
				}
			}
			temp = sent;
			if (mymap.count(temp) == 0)
			{
				mymap[temp] = 1;
				cnt ++;
			}
		}
		printf("Case #%d: %d\n",i,cnt);
		mymap.clear();
	}
}