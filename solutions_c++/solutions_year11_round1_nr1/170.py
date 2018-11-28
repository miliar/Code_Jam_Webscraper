#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <ctime>
#include <cmath>
#include <set>
#include <map>
#pragma comment(linker, "/STACK:1760777216")

#define ll long long

using namespace std;

ll gcd(ll a,ll b) {return b==0 ? a : gcd(b,a%b);}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin >> T;
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		bool poss=true;
		ll n,pd,pg;
		cin >> n >> pd >> pg;
		if (pd!=100&&pg==100) poss=false;
		if (pd>0&&pg==0) poss=false;
		ll b=100/gcd(pd,100);
		if (b>n) poss=false;
		if (poss) printf("Possible\n");
		else printf("Broken\n");
	}
	return 0;
}
