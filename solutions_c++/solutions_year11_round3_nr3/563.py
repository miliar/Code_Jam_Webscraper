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
#define ft(n) for(t=0;t<(n);t++)
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

int main()
{
	freopen("small.in","r",stdin);
	freopen("output.out","w",stdout);
    int i,j,k,t,tt;
    tt=si();
    ft(tt)
    {
    	printf("Case #%d: ",t+1);
    	//write you program:
    	int n,l,h,a[100];
    	n=si();
    	l=si();
    	h=si();
    	fi(n)
    		a[i]=si();
    	fii(l,h)
    	{
    		fj(n)
    			if(i%a[j]&&a[j]%i)
    				break;
    		if(j==n)
    			break;
    	}
    	if(j<n)
    		printf("NO\n");
    	else
    		pi(i);
    }
    return 0;
}