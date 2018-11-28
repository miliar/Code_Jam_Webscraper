#include "stdafx.h"
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <iostream>
#define PI 3.14159265358979323846264338327950288
#define _clr(a,b) memset(a,b,sizeof(a))
template<class T> T _abs(T a)
{ if(a<0) return -a;return a;}
template<class T> void get_min(T& a,T b)
{ if(a>b) a=b;}
template<class T> void get_max(T& a,T b)
{ if(a<b) a=b;}
using namespace std;
int count(__int64 a,__int64 b,__int64 c)
{
	int ans=0;
	__int64 p=c;
	for(int i=0;;i++)
	{
		if(a*c>=b) return ans;
		a=a*p;
		p=p*p;
		ans++;
	}
	/*else
	{
		double k=double(b)/double(a);
		k=pow(k,1/(double)c);
		int _a=b/k;
		int _b=k*a;
		MEM[a][b]=max(count(_a,b,c),count(a,_b,c))+1;
		return MEM[a][b];
	}*/
}
int main()
{
	//freopen("e:\\1.in","r",stdin);
	freopen("e:\\1.out","w",stdout);
	//freopen("e:\\B-small-attempt2.in","r",stdin);
	freopen("e:\\B-large.in","r",stdin);
	int a,b,c;
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		scanf("%d%d%d",&a,&b,&c);
		printf("%d%\n",count((__int64)a,(__int64)b,(__int64)c));
	}
	return 0;
}
