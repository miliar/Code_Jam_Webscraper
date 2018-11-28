#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>

using namespace std;

#define min(a,b) ((a) < (b) ? (a) : (b))
#define max(a,b) ((a) > (b) ? (a) : (b))

#define CLR(a) memset(a,0,sizeof(a))

#define i64 __int64

i64 cases,caseno,n,m,A;
bool flag;

void input()
{
	scanf("%I64d %I64d %I64d",&n,&m,&A);
}

i64 x2,x3,y2,y3,res;

void check()
{
	flag=false;

	printf("Case #%I64d: ",++caseno);

	for(x2=0;x2<=n && !flag;x2++)
	{
		for(y3=0;y3<=m && !flag;y3++)
		{
			for(x3=1;x3<=n && !flag;x3++)
			{
				res=x2*y3-A;
				if(res<0) continue;
				if(res%x3==0)
				{
					y2=res/x3;
					if(y2>=0 && y2<=m)
					{
						if(x2*y3-y2*x3==A) 
						{
							flag=true;
							return;
						}
					}
				}
			}
		}
	}
}

void process()
{
	check();
	if(!flag) puts("IMPOSSIBLE");
	else printf("0 0 %I64d %I64d %I64d %I64d\n",x2,y2,x3,y3);
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b1.ans","w",stdout);
		
	scanf("%I64d",&cases);
	while(cases--)
	{
		input();
		process();
	}
	return 0;
}
