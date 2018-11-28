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
int size[1000];
ll sum[1000];
int rounds[1000];
int ptr;
int r,k,n;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
////////////////////////////////////////////
	int i,j,cnt;
	ll total=0;
	bool flag;
	scanf("%d",&cases);
	for(g=0;g<cases;g++)
	{
		total=0;
		flag=0;
		scanf("%d%d%d",&r,&k,&n);
		for(i=0;i<n;i++)
			scanf("%d",&size[i]);
		cnt=0;
		CLS(sum,0);
		CLS(rounds,-1);
		ptr=0;
		while(r)
		{
			if(flag==0)
			{
				if(rounds[ptr]!=-1)
				{
					total+=(r/(cnt-rounds[ptr]))*(total-sum[ptr]);
					r%=(cnt-rounds[ptr]);
					flag=1;
				}
				else
				{
					rounds[ptr]=cnt;
					sum[ptr]=total;
				}
			}

			if(r==0)
				break;
			int cap;

			cap =k;
			for(i=0;i<n;i++)
			{
				if(size[ptr]<=cap)
				{
					total+=size[ptr];
					cap-=size[ptr];
					ptr=(ptr+1)%n;
				}
				else
					break;
			}
			r--;
			cnt++;
		}
		printf("Case #%d: ",g+1);
		printf("%lld\n",total);
	}

	return 0;
}