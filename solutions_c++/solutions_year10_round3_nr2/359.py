#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <deque>
#include <cstdlib>
#define MAX 1000001
#define MAX2 10000001
using namespace std;
int main()
{
	unsigned long long int t,n,m,a,b,c,d,i,j,k,u,v,w,x,y,z,e,f,g,h,l,o,p,r,s;
	scanf("%llu", &t);
	for(z=1;z<=t;z++)
	{
		scanf("%llu %llu %llu", &l,&p,&c);
		j=0;
		i=l;
		while(i*c<p)
		{
			j++;
			i*=c;
		}
		i=0;
		while(j>0)
		{
			j/=2;
			i++;
		}		
		printf("Case #%llu: %llu\n", z, i);
	}	
	return 0;
}
