#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>

using namespace std;

#define pb		push_back
#define mp	 	make_pair
#define fill(a,v) 	memset(a, v, sizeof(a))
#define sz		size()
#define all(x)		x.begin(), x.end()
#define INDEX(arr,ind)	(lower_bound(all(arr),ind)-arr.begin())
#define FF		first
#define SS		second
#define T(t)            int t;scanf ("%d",&t);while (t--)

typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef long long int LL;
typedef vector<long long> VLL;
typedef pair<int,int> PII;
typedef vector<pair<int,int> > VPII;
typedef pair<double,double> pdd;

int main()
{
	int g=1;
	T(t){
	int n,s,p;
	scanf ("%d%d%d",&n,&s,&p);
	int t[n];
	int i,j,k,v,w=0,cnt=0;
	for (i=0;i<n;i++) scanf ("%d",&t[i]);
	for (i=0;i<n;i++)
	{
		if (t[i]%3==0)
		{
			if ((t[i]/3)>=p)
				cnt++;
			else if (t[i] && (t[i]/3)+1>=p && ((t[i]/3)+1)<11)
				w++;
		}
		else if (t[i]%3==1)
		{
			if (((t[i]/3)+1)>=p && ((t[i]/3)+1)<11)
				cnt++;
		}
		else if (t[i]%3==2)
		{
			if (((t[i]/3)+1)>=p && ((t[i]/3)+1)<11)
				cnt++;
			else if (((t[i]/3)+2)>=p && ((t[i]/3)+2)<11)
				w++;
		}
	}
	printf ("Case #%d: %d\n",g++,cnt+min(w,s));
	}
	return 0;
}
