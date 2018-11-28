#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <functional>
#include <cmath>
#include <iostream>
using namespace std;

string line[100];
int last[100];

void sw(int & a, int &b)
{
	int c;
	c=a;
	a=b;
	b=c;
}


int main()
{
	char tmp[100];
	int cases, i,j,n;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>cases;
	for(int t=1;t<=cases;t++)
	{
		cin>>n;
		for(i=0;i<n;i++)
		{
			cin>>line[i];
			int aa = -1;
			for(j=0;j<n;j++)
			{
				if(line[i][j] == '1')
					aa=j;
			}
			last[i]=aa;
		}
		int ans=0;
		for(i=0;i<n;i++)
		{
			for(j=i;j<n;j++)
			{
				if(last[j]<=i)
					break;
			}
			for(int cc=j;cc>i;cc--)
			{
				ans++;
				swap(last[cc],last[cc-1]);
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}