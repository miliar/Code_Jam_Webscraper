#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
using namespace std;

#define debug(x) cout << #x << "=" << x << endl

long long t,n,pd,pg;

string f(long long n, long long pd, long long pg)
{
	if (pg==0)
		if (pd==0) return "Possible";
		else return "Broken";
	if (pg==100)
		if (pd==100) return "Possible";
		else return "Broken";
	for (int i=1;i<=n;i++)
		if (i*pd%100==0) return "Possible";
	return "Broken";
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	
	cin >> t;
	for (long long i=1; i<=t; i++)
	{
		cin >> n >> pd >> pg;
		cout << "Case #" << i << ": " << f(n,pd,pg) << endl;
	}
	
	return 0;
}
