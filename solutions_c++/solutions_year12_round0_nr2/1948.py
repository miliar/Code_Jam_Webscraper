// This works!!
//Data-structures includes
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>


//Other Includes
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
	int i,j,k,v,wild=0,temp=0;
	for (i=0;i<n;i++) scanf ("%d",&t[i]);
	for (v=0;v<n;v++)
	{
		if (t[v]%3==0)
		{
			if ((t[v]/3)>=p)
				temp++;
			else if (t[v] && (t[v]/3)+1>=p && ((t[v]/3)+1)<11)
				wild++;
		}
		else if (t[v]%3==1)
		{
			if (((t[v]/3)+1)>=p && ((t[v]/3)+1)<11)
				temp++;
		}
		else if (t[v]%3==2)
		{
			if (((t[v]/3)+1)>=p && ((t[v]/3)+1)<11)
				temp++;
			else if (((t[v]/3)+2)>=p && ((t[v]/3)+2)<11)
				wild++;
		}
	}
	printf ("Case #%d: %d\n",g++,temp+min(wild,s));
	}
	return 0;
}
