// joy A
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<map>
#include<string>
#include<cmath>
#include<set>
using namespace std;
typedef __int64 LL;

LL N,PD,PG;
LL gcd(LL a,LL b)
{
	while(b) b^=a^=b^=a%=b;
	return a;
}
bool okay()
{
	LL g=gcd(PD,100);
	if(N<100/g) return 0;
	return 1;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;scanf("%d",&T);
	int CN=0;
	
	while(T--)
	{
		scanf("%I64d%I64d%I64d",&N,&PD,&PG);
		printf("Case #%d: ",++CN);
		if((PD!=100&&PG==100)||(PD>0&&PG==0)||!okay()) puts("Broken");
		else puts("Possible");
	}
	
	
	return 0;
}
