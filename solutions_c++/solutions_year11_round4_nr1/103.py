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

#define FRsmall(x,y) freopen(#x"-small-attempt"#y".in","r",stdin);freopen(#x"-small-attempt"#y".out","w",stdout);
#define FRlarge(x) freopen(#x"-large.in","r",stdin);freopen(#x"-large.out","w",stdout);

int d[110];

int main()
{
	//freopen("A.in","r",stdin);
	//FRsmall(A,0)
	FRlarge(A)

	int T,C=0;
	scanf("%d",&T);
	while(++C<=T)
	{
		printf("Case #%d: ",C);
		
		int S,R,X,t,N;
		int i,s=0;
		int b,e,w;
		double c=0,u,m;
		memset(d,0,sizeof(d));
		scanf("%d %d %d %d %d",&X,&S,&R,&t,&N);
		for(i=0;i<N;i++)
		{
			scanf("%d %d %d",&b,&e,&w);
			d[w]+=e-b;
			s+=e-b;
		}
		d[0]+=X-s;u=t;
		for(i=0;i<=100;i++)
		{
			m=min((double)d[i]/(i+R),u);
			u-=m;
			c+=m;
			c+=(d[i]-m*(i+R))/(i+S);
		}
		printf("%.10f\n",c);
	}
	return 0;
}
