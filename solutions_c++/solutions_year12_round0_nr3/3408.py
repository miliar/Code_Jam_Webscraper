#include<iostream>
#include <string.h>
#include <map>
#include <algorithm>
#include <vector>
#include <stdio.h>

using namespace std;

int len;
int ac;
void getlen(int a)
{
	if(a < 10) len = 1,ac = 1;
	else if(a < 100) len = 10,ac = 2;
	else if(a < 1000) len = 100,ac = 3;
	else if(a < 10000) len = 1000,ac = 4;
	else if(a < 100000) len = 10000,ac = 5;
	else if(a < 1000000) len = 100000,ac = 6;
	else if(a < 10000000) len = 1000000,ac = 7;
	else if(a < 100000000) len = 10000000,ac = 8;
	
}
bool ok(int a,int b)
{
	int t = ac ;
	if(ac == 1) return false;

	while(t --)
	{
		a = a%len * 10 + a / len;
		if(a == b)
			return true;
	}
	return false;
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("c.out","w",stdout);
	int t;
	int cas = 1;
	int a,b;
	cin>>t;
	while(t--)
	{
		int ans = 0;
		cin>>a>>b;
		getlen(a);
		for(int i = a; i <= b; i ++)
		{
			for(int j = i+1; j <= b; j ++)
			{
				if(ok(i,j))
				{
					//printf("ok :  %d %d\n",i,j);
					ans ++;
				}
			}
		}
		printf("Case #%d: %d\n",cas ++, ans);
	}
	return 0;
}