#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <cctype>
#include <algorithm>
#include <vector>
#include <numeric>
#include <set>
#include <queue>
#include <map>
#include <list>
#include <string>
#include <iostream>
#include <stack>
#include <sstream>
using namespace std; 
#define PB push_back
#define MP make_pair
#define F first
#define S second 
#define BE(a) a.begin(),a.end() 
#define CLS(a,b) memset(a,b,sizeof(a))
#define SZ(a) ((int)a.size())
const long double pi=acos(-1.0);
#define torad(a) ((a)*pi/180.0)
typedef vector<int> vi ; 
typedef vector<string> vs ; 
typedef vector<double> vd ; 
typedef pair<int,int> pii ; 
typedef long long ll ; 
typedef long double ld ; 
typedef double dl ; 
class chick {public:
int x,v,t;
};
//typedef vector<node> vn ; 
int cases,g,n,k,b,t;
chick all[51];
int acc[51];
int main()
{
	freopen("B-large.in","r",stdin);
	
	freopen("B-large.out","w",stdout);
////////////////////////////////////////////
	int i,j;
	ll sol;
	scanf("%d",&cases);
	int x;
	for(g=0;g<cases;g++)
	{
		sol=0;
		CLS(acc,0);
		printf("Case #%d: ",g+1);
		
		scanf("%d%d%d%d",&n,&k,&b,&t);

		for(i=0;i<n;i++)
		{
			scanf("%d",&all[i].x);
		}
		for(i=0;i<n;i++)
		{
			scanf("%d",&all[i].v);
			all[i].t=(b-all[i].x)/all[i].v+bool((b-all[i].x)%all[i].v);
		}
		reverse(all,all+n);
		acc[0]=(all[0].t<=t);
		for(i=1;i<n;i++)
		{
			acc[i]=acc[i-1]+bool(all[i].t<=t);
		}
		int h;
		if(acc[n-1]<k)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			h=0;
			for(i=n-1;i>=0;i--)
			{
				if(i+1==acc[i])
					break;
				if(all[i].t>t)
					if(acc[i]<k)
						sol+=(k-acc[i]);
			}
			printf("%lld\n",sol);
		}
		
	}

	return 0;
}