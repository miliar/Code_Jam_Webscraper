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
#include <cstring>
#include <string>
using namespace std;
#define rep(i,a,b) for(int i=a;i<b;i++)
#define print(n) printf("%d ",n);
#define printl(n) printf("%lld ",n);
#define println(n) printf("%d\n",n);
#define printlln(n) printf("%lld\n",n);
char S[128][128];
int main()
{
	int X;
	scanf("%d",&X);
	int kase=1;
	while(X--)
	{
		int r,c;
		scanf("%d%d",&r,&c);
		rep(i,0,r)scanf("%s",S[i]);
		bool flag=false;
		rep(i,0,r)
		{
			rep(j,0,c)
			{
				if(i==r-1 || j==c-1)
				{
					if(S[i][j]=='#')
					{
						flag=1;
						break;
					}
					continue;
				}
				if(S[i][j]=='#' && S[i+1][j]=='#' && S[i][j+1]=='#' && S[i+1][j+1]=='#')
				{
					S[i][j]='/';S[i+1][j]='\\';S[i][j+1]='\\';S[i+1][j+1]='/';
				}
				else 
				{
					if(S[i][j]=='#')
					{
						flag=1;
					//	print(i);
					//	print(j);
						break;
					}
				}
			}
			if(flag)break;
		}
		printf("Case #%d:\n",kase);
		if(flag)puts("Impossible");
		else
		{
			rep(i,0,r)puts(S[i]);
		}
		kase++;
	}
}

