#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
using namespace std;
__int64 n;
int fz,fm,fz2,fm2;
int gcd(int a,int b)
{
	if( b==0 )return a;
	return gcd(b,a%b);
}
int main()
{
	int repeat,pd,pg,ri=1,t,flag;
	freopen("A-large.in","r",stdin);
	freopen("1.out","w",stdout);

	scanf("%d",&repeat);
	while(repeat--)
	{
		flag=0;
		scanf("%I64d%d%d",&n,&pd,&pg);
		fz=pd;
		fm=100;
		t=gcd(fz,fm);
		fm/=t;
		fz/=t;
		if( fm<=n && ((pg!=100 &&pg!=0) || pd==pg)) flag=1;


		printf("Case #%d: %s\n",ri++,flag?"Possible":"Broken");
	}
	return 0;
}