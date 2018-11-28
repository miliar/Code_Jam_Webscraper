#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <memory.h>
using namespace std;
long long gcd(long long a,long long b)
{
	while (b)
	{
		a%=b;
		swap(a,b);
	}
	return a;
}

int main()
{
	freopen("A-large.in","r",stdin);
		freopen("out.txt","w",stdout);

	int test;
	cin>>test;
	for (int curt=1;curt<=test;curt++)
	{
		long long pd,pg,n;
		cin>>n>>pd>>pg;
		string s;
		if (pg==0&&pd!=0)
		{
			s="Broken";
		}
		else
		{
			if (pg==100&&pd!=100)
				s="Broken";
			else
			{
				long long temp=gcd(100,pd);
				temp=100/temp;
				if (temp>n)
					s="Broken";
				else
					s="Possible";
			}
		}
		cout<<"Case #"<< curt<<": "<<s<<endl;
	}

	return 0;
}