/*You choise is C++ IDE*/

#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <stdlib.h>
#include <math.h>
#include <memory.h>
#include <iomanip>
#include <string>
#include <cstring>

#define fi(n) for(i=0;i<(n);i++)
#define fj(n) for(j=0;j<(n);j++)
#define fk(n) for(k=0;k<(n);k++)
#define ft(n) for(T=0;T<(n);T++)
#define fii(a,b) for(i=a;i<=b;i++)
#define fjj(a,b) for(j=a;j<=b;j++)
#define fkk(a,b) for(k=a;k<=b;k++)
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ZERO(x) ((x)>(1e-8)?(x):0)

using namespace std;

int si(){int m;scanf("%d",&m);return m;}
char sc(){char m;scanf("%c",&m);return m;}
double sd(){double m;scanf("%lf",&m);return m;}
__int64 sll(){__int64 m;scanf("%I64d",&m);return m;}
char xuebin[100001];string ss(){gets(xuebin);return xuebin;}

void pi(int x){printf("%d\n",x);}
void pc(char x){printf("%c\n",x);}
void pd(double x){printf("%lf\n",x);}
void pll(__int64 x){printf("%I64d\n",x);}
void ps(char *x){puts(x);}
int a[1000000];

int main()
{
	freopen("small.in","r",stdin);
	freopen("output.txt","w",stdout);
    int i,j,k,T,tt;
    tt=si();
    ft(tt)
    {
    	printf("Case #%d: ",T+1);
    	//write you program:
    	int l,t,n,c,min=0,max=0;
    	scanf("%d%d%d%d",&l,&t,&n,&c);
    	fi(c)
    	{
    		a[i]=si();
    	}
    	for(j=c;j<n;j++)
    	{
    		a[j]=a[j-c];
    	}
    	for(i=0;i<n;i++)
    	{
    		max+=a[i]*2;
    		if(max>=t)
    			break;
    		a[i]=0;
    	}
    	if(i==n)
    	{
    		min+=max;
    		pi(min);
    		continue;
    	}
    	min+=t;
    	a[i]=(max-t)/2;
    	sort(a,a+n);
    	for(j=n-1;j>=0;)
    	{
    		if(!l)
    			break;
    		min+=a[j];
    		l--;
    		j--;
    	}
    	for(;j>=0;j--)
    	min+=2*a[j];
    	pi(min);
    }
    return 0;
}