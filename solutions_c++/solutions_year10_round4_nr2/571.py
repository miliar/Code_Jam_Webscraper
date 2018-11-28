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
#include <memory.h>
using namespace std;
#define maxw 2000000000

int f[2048][11];

int main()
{
	//freopen("B.in","r",stdin);
	//freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
	//freopen("B-small-attempt1.in","r",stdin);freopen("B-small-attempt1.out","w",stdout);
	//freopen("B-small-attempt2.in","r",stdin);freopen("B-small-attempt2.out","w",stdout);
	freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);

	int T,C=0,P,i,h,hh,t,j,a;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",++C);
		scanf("%d",&P);
		h=1<<P;
		for(i=0;i<h;i++)
		{
			scanf("%d",&t);
			t=P-t;
			for(j=0;j<t;j++)f[i+h][j]=maxw;
			for(;j<=P;j++)f[i+h][j]=0;
		}
		for(a=P-1;a>=0;a--)
		{
			h=1<<a;
			for(i=0;i<h;i++)
			{
				scanf("%d",&t);
				//for(j=0;j<=P;j++)f[i+h][j]=f[(i+h)*2][j];
				for(j=0;j<=P;j++)
					if(f[(i+h)*2][j]==maxw || f[(i+h)*2+1][j]==maxw)
						f[i+h][j]=maxw;
					else
						f[i+h][j]=f[(i+h)*2][j]+f[(i+h)*2+1][j];
				for(j=0;j<P;j++)if(f[i+h][j]>f[i+h][j+1]+t)f[i+h][j]=f[i+h][j+1]+t;
			}
		}
		printf("%d\n",f[1][0]);
	}
	return 0;
}
