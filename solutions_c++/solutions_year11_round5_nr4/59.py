#include <stdio.h>
#include <math.h>
#define N 110
char s[N];
bool is(long long x)
{
	long long d=sqrt((double)x);
	for(; d*d<x; d++);
	for(; d*d>x; d--);
	return d*d==x;
}
bool rec(int i, long long x)
{
	if(s[i]==0) return is(x);
	else if(s[i]=='1') return rec(i+1, x*2+1);
	else if(s[i]=='0') return rec(i+1, x*2);
	else
	{
		s[i]='0';
		if(rec(i+1, x*2)) return 1;
		s[i]='1';
		if(rec(i+1, x*2+1)) return 1;
		s[i]='?';
		return 0;
	}
}
int main()
{
	int t, ts;
	for(scanf("%d", &ts), t=0; t<ts; scanf("%s", s), rec(0, 0), printf("Case #%d: %s\n", t+1, s), t++);
	return 0;
}