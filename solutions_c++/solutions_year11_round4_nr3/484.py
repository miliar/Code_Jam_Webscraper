#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
using namespace std;

typedef long long ll;

int plist[1000],pcnt;
bool p[1001];

void work()
{
	memset(p,1,sizeof(p));
	p[0] = p[1] = false;
	for(int i=2;i<=1000;i++)
	{
		if (p[i]==false) continue;
		plist[pcnt++] = i;
		for(int j=i*i;j<=1000;j+=i)
			p[j] = false;
	}
}

int price[1000];

int now[1000];

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);

	work();

	int T;
	cin>>T;
	for(int tt=1;tt<=T;tt++)
	{
		printf("Case #%d: ",tt);
		
		int n;
		cin>>n;
		
		memset(price,0,sizeof(price));
		int maxWaiter = 1;
		for(int i=2;i<=n;i++)
		{
			bool ok = true;
			int k = i,pcounter = 0;
			while(k>1)
			{
				now[pcounter] = 0;
				while (k%plist[pcounter]==0) { k/=plist[pcounter]; now[pcounter]++; }
				if (now[pcounter]>price[pcounter]) ok = false;
				++pcounter;
			}
			if (ok==false)
			{
				for(int j=0;j<pcounter;j++)
					price[j] = max(price[j],now[j]);
			}
		}
		for(int i=0;i<1000;i++)
			maxWaiter+=price[i];

		int minWaiter = 0;
		if (n==1) minWaiter = 1;
		else
		{
			int current = 1;
			for(int i=0;i<1000;i++)
			{
				int num = 1;
				for(int j=0;j<price[i];j++) num*=plist[i];
				if (current*num>n) { ++minWaiter; current = num; }
				else current = current * num;
			}
			++minWaiter;
		}

		printf("%d\n",maxWaiter-minWaiter);
	}
	return 0;
}
