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
class node {public:
};
typedef vector<node> vn ; 
int cases,g;
ll dist[1000009];
ll n,c,l;
ll t;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
////////////////////////////////////////////
	int i,j,k;
	scanf("%d",&cases);
	for(g=0;g<cases;g++)
	{
		printf("Case #%d: ",g+1);
		scanf("%lld%lld%lld%lld",&l,&t,&n,&c);
		for(i=0;i<c;i++)
		{
			int x;
			scanf("%d",&x);
			for(j=i;j<n;j+=c)
				dist[j]=2*x;
		}
		ll curt=0,curp=0;
		while(curp < n && t>=dist[curp])
		{
			t-=dist[curp];
			curt+=dist[curp];
			++curp;
		}
		if(curp < n)
		{
			if(t)
			{
				dist[curp]-=t;
				curt+=t;
			}
			sort(dist+curp,dist+n);
			for(i=curp;i<n-l;i++)
				curt+=dist[i];
			for(i=n-1;i>=n-l && i>=curp;--i)
				curt+=dist[i]/2;
		}
		printf("%lld\n",curt);
	}

	return 0;
}