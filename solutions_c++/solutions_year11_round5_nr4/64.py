#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#include <set>

#define ll long long

using namespace std;

ll Sqrt(ll num)
{
	ll l=0,r=1518500249;
	while(r-l>1)
	{
		ll m=(l+r)>>1;
		if (m*m<=num) l=m;
		else r=m;
	}
	for(ll i=l-2;i<=l+2;i++)
		if (i*i==num) return i;
	return -1;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	char str[64]={0};
	ll step2[64]={0};
	step2[0]=1;
	for(int i=1;i<64;i++)
		step2[i]=step2[i-1]*2;
	for(int TT=1;TT<=T;++TT)
	{
		printf("Case #%d: ",TT);
		cin >> str;
		vector <ll> what;
		int l=strlen(str);
		ll num=0;
		for(int i=0;i<l;i++)
			if (str[i]=='?')
			{
				what.push_back(step2[l-i-1]);
			}
			else
			{
				num+=(str[i]-'0')*step2[l-i-1];
			}
		ll ret=-1;
		for(int mask=0;mask<(1<<what.size());++mask)
		{
			ll cur=num;
			for(int i=0;i<what.size();i++)
				cur+=((mask&(1<<i))>0)*what[i];
			if (Sqrt(cur)!=-1)
			{
				if (ret==-1||ret>cur) ret=cur;
				break;
			}
		}
		if (what.size()==0) ret=num;
		vector <int> r;
		while(ret>0)
		{
			r.push_back(ret%2);
			ret>>=1;
		}
		for(int i=r.size()-1;i>=0;i--)
			printf("%d",r[i]);
		printf("\n");
	}
	return 0;
}
