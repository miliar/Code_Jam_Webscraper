#define mset(a) memset(a,0,sizeof(a))

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;
int hx[2000],hy[2000];
int r[2000];
int main()
{
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		int n,w,l;
		cin>>n>>w>>l;
		for(int i=0;i<n;i++)
			cin>>r[i];
		int prex=0,prey=0;
		for(int i=0;i<n;i++)
		{
			for(int x=prex;x<=w;x+=r[i])
				for(int y=0;y<=l;y+=r[i])
				{
					if(x==prex){y=prey+(i==0)?0:(r[i]+r[i-1])-1;x++;continue;}
					for(int j=0;j<i;j++)
					{
						if((long long)(x-hx[j])*(x-hx[j])+(long long)(y-hy[j])*(y-hy[j])<(long long)(r[i]+r[j])*(r[i]+r[j]))
							goto l1;
					}
					hx[i]=x;
					hy[i]=y;
					prex=x;
					prey=y;
					goto l2;
l1:;
				}
l2:;

		}
		printf("Case #%d:",tt);
		for(int i=0;i<n;i++)
			printf(" %d.0 %d.0",hx[i],hy[i]);
		printf("\n");
	}
	return 0;
}
