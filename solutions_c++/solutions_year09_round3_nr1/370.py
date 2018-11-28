#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>

using namespace std;
typedef __int64 ll;
char s[10000];
int was[1000];
const int ml=100,base=10000,nd=4;
struct bign
{ 
	int len,s[ml]; //数组从下标1开始按nd位倒着存：1234567：4567 123
};
void init(bign &bi)
{
	bi.len=1; 
	memset(bi.s,0,sizeof(bi.s)); 
}
void fixlen(bign &bi)
{
	while(bi.len>1 && !bi.s[bi.len])
		bi.len--; 
}
void print(bign &bi){
	printf("%d",bi.s[bi.len]);
	for(int i=bi.len-1;i;i--)printf("%04d",bi.s[i]);
}
void init(bign &bi,char *str)
{
	int i,j=strlen(str)-1; 
	init(bi); bi.len=j/nd+1;
	for(i=0;i<=j;i++)
	{ 
		int k=(j-i)/nd+1;
		bi.s[k]=bi.s[k]*10+str[i]-'0'; 
	}
}
int cmp(bign &a,bign &b){
	if( a.len != b.len ) return a.len-b.len;
	for(int i=a.len;i;i--)
		if(a.s[i] != b.s[i]) return a.s[i]-b.s[i];
	return 0;
}
bign operator+(bign &a,bign &b)
{
	bign c; int i; init(c);
	for(i=1;i<=a.len || i<=b.len || c.s[i];i++)
	{
		c.s[i]+=a.s[i]+b.s[i];
		c.s[i+1]=c.s[i]/base; 
		c.s[i]%=base;
	}
	if(i>1)c.len=i-1;
	else c.len=1;
	return c;
}
bign operator*(bign &a,bign &b){
	bign c; init(c); c.len=a.len+b.len;
	__int64 g=0;
	for(int k=1;k<=c.len;k++)
	{
		__int64 tmp=g; 
		int i=k+1-b.len; 
		if(i<1) i=1;
		for(;i<=k && i<=a.len;i++)
			tmp+=a.s[i]*b.s[k+1-i];
		g=tmp/base;
		c.s[k]=tmp%base;
	}
	fixlen(c);
	return c;
}
int main()
{
	int i,j,k,ca,kk=1;
	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	scanf("%d",&ca);
	while(ca--) 
	{
		scanf("%s",s);
		memset(was,-1,sizeof(was));
		int len=strlen(s);
		int cnt=0;
		for(i=0;i<len;i++) if(was[s[i]]==-1) 
		{
			cnt++;
			if(i==0) was[s[i]]=1;
			else 
			{
				if(cnt==2) was[s[i]]=0;
				else was[s[i]]=cnt-1;
			}
		}
		if(cnt==1) cnt++;
		ll ans=0;
		for(i=0;i<len;i++) 
		{
			ans=ans*cnt+was[s[i]];
		}
		printf("Case #%d: %I64d\n",kk++,ans);
	}
	return 0;
}