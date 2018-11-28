#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <string>
#include <cstring>
#include <queue>

#define fr(i,a,n) for((i)=(a);(i)<(n);(i)=(i)+1)
#define fre(i,a,n) for((i)=(a);(i)<=(n); (i)=(i)+1)
#define frre(i,j,n) for((i)=(j);(i)>=(n);(i)--)

#define pb(X) push_back((X))
#define vs vector <string>
#define vi vector <int>
#define vvi vector < vi >

#define _bc(i) __builtin_popcount(i)
#define INF 0x3f3f3f3f //1061109567
typedef long long lint;
typedef unsigned long long ull;

using namespace std;


int main()
{
	int t,n,i;
	char r[105],ch;
	int p[105];
	scanf("%d",&t);
	for(int tt=1; tt<=t; tt++)
	{
		scanf("%d",&n);
		for(i=0; i<n; i++)
		{
			scanf("%c%c%d",&ch,&r[i],&p[i]);
		}
		int x=1,y=1,prev1=0,prev2=0,pp,cnt=0;
		for(i=0; i<n; i++)
		{
			if(r[i]=='O')
			{
				
				if(y==p[i])
				{
					cnt++;
					prev1+=1;
				}
				else
				{
					if(prev2 >= abs(p[i]-y))
						pp=0;
					else
						pp=abs(p[i]-y)-prev2;
						
					cnt+=pp+1;
					prev1+=pp+1;
					y=p[i];
				}
				prev2=0;
			}
			else
			{			
				if(x==p[i])
				{
					cnt++;
					prev2+=1;
				}
				else
				{
					if(prev1 >= abs(p[i]-x))
						pp=0;
					else
						pp=abs(p[i]-x)-prev1;
						
					cnt+=pp+1;
					prev2+=pp+1;
					x=p[i];
				}
				prev1=0;
			}
		}
		printf("Case #%d: %d\n",tt,cnt);
	}
	return 0;
}
