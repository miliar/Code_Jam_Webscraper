#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <memory.h>
#include <queue>
#include <math.h>
#include <string>
#include <sstream>

using namespace std;

#define MS(a,b) memset(a,b,sizeof(a));

bool vis[300];
int val[300];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	for (int t=1;t<=T;t++)
	{
		string s;
		cin>>s;
		MS(vis,0);
		MS(val,-1);
		int cc=0;
		for (int i=0;i<s.size();i++)
		{
			vis[s[i]]=true;
			if (val[s[i]]==-1)
			{
				if (cc==0)
				{
					val[s[i]]=1;
					cc++;
				}
				else if (cc==1)
				{
					val[s[i]]=0;
					cc++;
				}
				else
					val[s[i]]=cc++;
			}
		}
		if (cc==1)
			cc++;
		long long res=0;
		for (int i=s.size()-1,base=1;i>=0;i--,base*=cc)
		{
			res+=val[s[i]]*base;
		}
		cout<<"Case #"<<t<<": "<<res<<endl;
	}
	return 0;
}