#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <string>
#include <bitset>
#include <map>

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>

using namespace std;

int test(int s,int p)
{
	int i,a,b,c,x,y,sur;
	sur = 0;
	for(p=p;p<=10;p++){
		for(i=-2;i<=2;i++)
		{
			p = p;
			x = p + i;
			y = s - p - x;
			//printf("%d - %d %d %d\n",s,p,x,y);
			if( x<0 || y<0 || x>10 || y>10) continue;
			a = abs(p-x);
			b = abs(p-y);
			c = abs(x-y);
			if(a<=1 && b<=1 && c<=1)
			{
				return 1;
			}
			if(a<=2 && b<=2 && c<=2)
			{
				sur = 1;
			}
		}
	}

	if(sur) return 0;
	else return -1;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-out.txt","w",stdout);
	int t,T;
	int i;
	int n,s,p,r,x;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		cin>>n>>s>>p;
		r = 0;
		for(i=0;i<n;i++)
		{
			cin>>x;
			x = test(x,p);
			if(x==1) r++;
			else if(x==0)
			{
				if(s)
				{
					s--;
					r++;
				}
			}
		}
		printf("Case #%d: %d\n",t,r);
	}
	return 0;
}




