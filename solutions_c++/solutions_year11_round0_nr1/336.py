#include<cstdio>
#include<string>
#include<iostream>
#include<cmath>
using namespace std;
int mod(int p)
{
	if(p<0) return -p;
	else p;
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++)
	{
		int o,b;
		o=b=1;
		int to,tb;
		to=tb=0;
		int time=0,n,p;
		string st;
		scanf("%d",&n);
		while(n--)
		{
			cin>>st>>p;
			if(st=="O")
			{
				time=max(time,to+mod(p-o))+1;
				to=time;
				o=p;
			}
			else
			{
				time=max(time,tb+mod(p-b))+1;
				tb=time;
				b=p;
			}
		}
		printf("Case #%d: %d\n",tc,time);
	}
	return 0;
}
