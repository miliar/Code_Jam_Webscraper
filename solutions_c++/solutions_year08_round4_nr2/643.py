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
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define PI 3.14159265358979323846264338327950288
#define MOD 1000
typedef __int64 int64;

int64 a;
bool check(int64 y1,int64 x2,int64 x3,int64 y3)
{
	int64 t=x2*y3+x3*y1-x2*y1;
	if(t==a||t==-a)return true;
	return false;
}

int main()
{
	//freopen("B-small-attempt2.in","r",stdin);
	//freopen("B-small-attempt2.out","w",stdout);
	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);
	int cas,ca;
	int64 x,y;
	for(scanf("%d",&cas),ca=1;ca<=cas;ca++)
	{
		printf("Case #%d: ",ca);
		scanf("%I64d%I64d%I64d",&x,&y,&a);
		for(int64 y1=0;y1<=x;y1++)for(int64 x2=0;x2<=y;x2++)
			for(int64 xx=0;xx<=x;xx++)for(int64 yy=0;yy<=y;yy++)
				if(check(y1,x2,xx,yy))
				{
					int64 x1=0,y2=0;
					printf("%I64d %I64d %I64d %I64d %I64d %I64d\n",x1,y1,x2,y2,xx,yy);
					//int x1=0,y2=0,x3=xx,y3=yy;
					//printf("%d\n",x1*y2-x2*y1+x2*y3-x3*y2+x3*y1-x1*y3);
					goto loop;
				}
		printf("IMPOSSIBLE\n");
		loop:;
	}
}

