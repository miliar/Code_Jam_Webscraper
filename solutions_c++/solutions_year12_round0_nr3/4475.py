
#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <cmath>
#include <cstdio>
#include <algorithm>

#define pb push_back
#define mp make_pair
#define FOR(i,a,b) for (int i = (a); (i) <= (b); (i)++)
using namespace std;

int test;
int used1[11], used2[11];

bool good(int a, int b)
{
	FOR(i,0,9)
	used1[i] = used2[i] = 0;
	char bufer[5];
	sprintf(bufer,"%d",a);
	string s1(bufer);
	sprintf(bufer,"%d",b);
	string s2(bufer);
	int n = s1.size();
	int m = s2.size();
	if (n != m) return false;
	for(int i =0; i<n; i++)
	{
		used1[int(s1[i])-48]++;
		used2[int(s2[i])-48]++;
	}
	FOR(i,0,9)
	if (used1[i] != used2[i]) return false;
	FOR(i,1,n)
	{
		s1 = s1[n-1] + s1.substr(0,n-1);
		if (s1 == s2) return true;
	}
	return false;
}




int main()

{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d\n",&test);
	FOR(t,1,test)
	{
		int n,m;
		cin >> n >> m;
		int ans = 0;
		FOR(i,n,m)
		for(int j = i+1; j <= m; j++)
		if (good(i,j))
		{
			ans++;
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
