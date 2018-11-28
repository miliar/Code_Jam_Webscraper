#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <iterator>
#include <iostream>
#include <functional>
#include <sstream>
#include <numeric>

#define CLR( x , y ) ( memset( (x) , (y) , sizeof( (x) ) ) )
#define EPS 1e-9

using namespace std;

FILE *in=fopen("B.in","r");
FILE *outt=fopen("B.out","w");

int n,m;

long long a;

int area(int x1,int y1,int x2,int y2)
{
	return x1*y2+y1*x2;
}
long long gcd(long long a,long long b)
{
	if(!b)return a;
	return gcd(b,a%b);
}
int main()
{
	int i,j,k,test,tests;
	int n;
	long long x1,y1,x2,y2;
	fscanf(in,"%d",&tests);
	for(test=1;test<=tests;test++){
		int D=0;
		fscanf(in,"%d%d%lld",&n,&m,&a);
		a*=a;
		for(x1=0;x1<=n;x1++){
			for(y1=0;y1<=m;y1++){
				for(x2=0;x2<=n;x2++){
					for(y2=0;y2<=m;y2++){
						if(x1==0 && y1==0)continue;
						if(x2==0 && y2==0)continue;
						if(x1==x2 && y1==y2)continue;
						if(x1*y2-x2*y1==0)continue;
						int G1=x1*y2-x2*y1;
						if(G1*G1==a){
							D=1;
							break;
						}
					}
					if(D)break;
				}
				if(D)break;
			}
			if(D)break;
		}
		if(!D)fprintf(outt,"Case #%d: IMPOSSIBLE\n",test);
		else fprintf(outt,"Case #%d: %d %d %lld %lld %lld %lld\n",test,0,0,x1,y1,x2,y2);
	}
	return 0;
}
