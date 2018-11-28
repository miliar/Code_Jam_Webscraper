#line 5 "code.cpp"
#include <string>
#include <vector>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<m;i++)
#define sqr(x) (x)*(x)
#define For(i,n,m) for(int i=n;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef vector<vector<pair<int,int> > > adjL;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int cases;
	cin>>cases;
	for(int a=1;a<=cases;a++)
	{
		int x,s,r,t,n;
		cin>>x>>s>>r>>t>>n;
		double intervals[120];
		mem(intervals,0);
		int end=0;
		rep(i,n)
		{
			int si,ei,ti;
			cin>>si>>ei>>ti;
			if(si!=end)
				intervals[0]+=si-end;
			intervals[ti]+=ei-si;
			end=ei;
		}
		intervals[0]+=x-end;
		double time=0;
		double cur=t;
		for(int index=0;index<=110;index++)
		{
			if(intervals[index]==0)
				continue;
			double speed=index;
			if(cur>0)
			{
				speed+=r;
				double need=intervals[index]/speed;
				if(need>cur)
				{
					time+=cur;
					intervals[index]-=cur*speed;
					index--;
					cur=0;
				}
				else
				{
					time+=need;
					cur-=need;
					intervals[index]=0;
				}
			}
			else
			{
				speed+=s;
				time+=intervals[index]/speed;
				intervals[index]=0;
			}
		}
		printf("Case #%d: %.6f\n",a,time);
	}
	return 0;
}
// Powered by FileEdit
// Powered by TZTester 1.01 [25-Feb-2003]
// Powered by CodeProcessor
