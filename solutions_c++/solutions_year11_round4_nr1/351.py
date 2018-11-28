#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
using namespace std;

#define MP make_pair
#define PB push_back
#define two(X) (1<<(X))
#define SIZE(A) ((int)(A.size()))
#define LENGTH(A) ((int)A.length())
#define random(x) (rand()%x)
#define randomize() (srand((int)time(0)))

typedef long long int64;
typedef vector<int> VI;
typedef vector<string> VS;

const int INF=0x7FFFFFFF;
const double eps=1e-8;
const double pi=acos(-1.0);
const int maxn=100000;

struct data
{
	int x,y,s;
};

bool cmp1(const data &a, const data &b)
{
	return a.x<b.x;
}

bool cmp2(const data &a, const data &b)
{
	return a.s<b.s;
}

data a[maxn];
int L,S,R,T,N,n,ca;

void init()
{
	cin>>L>>S>>R>>T>>N;
	for (int i=0; i<N; i++)
		cin>>a[i].x>>a[i].y>>a[i].s;
	sort(a,a+N,cmp1);
	int now=0; n=N;
	for (int i=0; i<N; i++)
		if (a[i].x!=now)
		{
			a[n].x=now;
			a[n].y=a[i].x;
			a[n].s=0;
			now=a[i].y;
			n++;
		} else now=a[i].y;
	if (now!=L)
	{
         a[n].x=a[N-1].y;
         a[n].y=L;
         a[n].s=0;
         ++n;
    }
	sort(a,a+n,cmp2);
}

void solve()
{
	//for (int i=0; i<n; i++) cout<<a[i].x<<" "<<a[i].y<<" "<<a[i].s<<endl;
	double ans=0,t=T;
	for (int i=0; i<n; i++)
	{
		if (abs(t)<eps)
		{
			ans+=(a[i].y-a[i].x)*1.0/(S+a[i].s);
			continue;
		}

		if (t>=(a[i].y-a[i].x)*1.0/(R+a[i].s))
		{
			ans+=(a[i].y-a[i].x)*1.0/(R+a[i].s);
			t-=(a[i].y-a[i].x)*1.0/(R+a[i].s);
		} else
		{
			ans+=t;
			double L=(a[i].y-a[i].x)-(R+a[i].s)*t;
			ans+=L/(a[i].s+S);
			t=0;
		}
	}
	printf("%.10f\n",ans);
}

int main()
{
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
	cin>>ca;
	for (int i=1; i<=ca; i++)
	{
		cout<<"Case #"<<i<<": ";
		init();
		solve();
	}
	return 0;
}


