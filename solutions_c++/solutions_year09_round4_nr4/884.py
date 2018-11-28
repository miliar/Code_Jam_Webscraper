#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
#include <map>

#define mn(a,b) ((a<b) ? (a) : (b))        		
#define mx(a,b) ((a<b) ? (b) : (a))			
#define ab(a) ((a<0) ? (-(a)) : (a))			
#define fr(a,b) for(int a=0; a<b; ++a)			
#define fe(a,b,c) for(int a=b; a<c; ++a)		
#define fw(a,b,c) for(int a=b; a<=c; ++a)		
#define df(a,b,c) for(int a=b; a>=c; --a)		
#define BIG 1000000000					
#define MAX_STRING 10000				

using namespace std;

int c,n,x[40],y[40],r[40];
double eps= 1e-6;
	
int main()
{
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
scanf("%d\n", &c);
fr(t,c)
	{
	scanf("%d\n", &n);
	fr(i,n)
		scanf("%d%d%d\n", &x[i], &y[i], &r[i]);
	if(n==1) printf("Case #%d: %.6lf\n", t+1, r[0]*1.0);
	else if(n==2) printf("Case #%d: %.6lf\n", t+1, mx(r[0],r[1])*1.0);
	else 
		{
		double r1 = sqrt((x[1]-x[0])*(x[1]-x[0])+(y[1]-y[0])*(y[1]-y[0]))+r[0]+r[1];
		r1/=2;
		r1 = mx(r1,r[2]);
		double r2 = sqrt((x[2]-x[0])*(x[2]-x[0])+(y[2]-y[0])*(y[2]-y[0]))+r[0]+r[2];
		r2/=2;
		r2 = mx(r2,r[1]);		
		double r3 = sqrt((x[2]-x[1])*(x[2]-x[1])+(y[2]-y[1])*(y[2]-y[1]))+r[2]+r[1];
		r3/=2;
		r3 = mx(r3,r[0]);				
		printf("Case #%d: %.6lf\n", t+1, mn(mn(r1,r2),r3));
		}
	
/*
	double l,r,m;
	l = 0;
	r = 1000;
	while(r-l>eps)
		{
		m = (l+r)/2;
			
		}
*/
	}
return 0;
}
