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

struct Walkway
{
	double l;
	double w;
	friend bool operator <(Walkway a,Walkway b)
	{
		return a.w==b.w?a.l>b.l:a.w<b.w;
	}
}walkway[1111];
int main()
{
	int cas,m=1,N;
	double X,S,R,t;
	int i,j,k;
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>cas;
	while(cas--)
	{
		scanf("%lf%lf%lf%lf%d",&X,&S,&R,&t,&N);
		double s,e;
		double sum=0;
		for(i=0;i<N;i++)
		{
			scanf("%lf%lf%lf",&s,&e,&walkway[i].w);
			walkway[i].l=e-s;
			sum+=e-s;
		}
		walkway[N].w=0,walkway[N].l=X-sum;
		double remain=t,ans=0;
		sort(walkway,walkway+N+1);
		for(i=0;i<=N;i++)
		{
			if(remain>0)
			{
				if(remain>=walkway[i].l/(walkway[i].w+R))
					remain-=walkway[i].l/(walkway[i].w+R),ans+=walkway[i].l/(walkway[i].w+R);
				else
				{
					double l=(walkway[i].w+R)*remain;
					ans+=remain+(walkway[i].l-l)/(walkway[i].w+S);
					remain=0;
				}
			}
			else ans+=walkway[i].l/(walkway[i].w+S);
		}
		printf("Case #%d: %.6lf\n",m++,ans);
	}
}