#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
#include<iostream>

using namespace std;


typedef long long ll;
int n;
char s[1000];

bool isUgly(ll num)
{
	return num == 0 || num%2 == 0 || num%3==0 || num%7 ==0 || num%5==0; 
}

int dfsCount(int ind, ll sofar, ll cur, bool sign)
{
	if(ind == n)
		return isUgly(sofar+cur*(sign?1:-1));
	// +
	return dfsCount(ind+1, sofar+cur*(sign?1:-1), s[ind]-'0', 1)
	// -
	+ dfsCount(ind+1, sofar+cur*(sign?1:-1), s[ind]-'0', 0)
	// empty
	+ dfsCount(ind+1, sofar, cur*10+s[ind]-'0', sign);
}

int main(void)
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int numCase;
	scanf("%d", &numCase);
	for(int c=1; c<=numCase; c++)
	{
		scanf("%s", s);
		n=(int)strlen(s);
		int ret=dfsCount(1,0,s[0]-'0',1);
		printf("Case #%d: %d\n", c, ret);
	}
	return 0;
}