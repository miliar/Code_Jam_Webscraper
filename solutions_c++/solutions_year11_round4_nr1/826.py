#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <cmath>
#include <string>

#define fr(x,y) for(int x=0; x<(y); ++x)
#define fe(x,y,z) for(int x=(y); x<(z); ++x)
#define fw(x,y,z) for(int x=(y); x<=(z); ++x)
#define df(x,y,z) for(int x=(y); x>=(z); --x)
#define mn(x,y) ((x)<(y) ? (x) : (y))
#define mx(x,y) ((x)>(y) ? (x) : (y))
#define ab(x) ((x)<0 ? (-(x)) : (x))
#define MP make_pair
#define PB push_back
#define BIG 1000000000
#define X first
#define Y second
#define dbg(x) if(DEBUG) {cout<<#x<<": "<<(x)<<endl;}
#define dout(x) if(DEBUG) {cout<<x;}
#define dline(x) if(DEBUG) {cout<<x<<endl;}
#define dbgr(x,l) if(DEBUG) {cout<<#x<<": ";fr(innercounter,l) cout<<x[innercounter]<<" ";cout<<endl;}
#define dbge(x,y,z) if(DEBUG) {cout<<#x<<": ";fe(innercounter,y,z) cout<<x[innercounter]<<" ";cout<<endl;}
#define dbgw(x,y,z) if(DEBUG) {cout<<#x<<": ";fw(innercounter,y,z) cout<<x[innercounter]<<" ";cout<<endl;}
#define dbgee(x,l1,l2) if(DEBUG) {cout<<#x<<": "<<endl;fr(icounter,l1){fr(jcounter,l2) cout<<x[icounter][jcounter]<<" ";cout<<endl;}}

bool DEBUG = false;

using namespace std;

typedef pair<int,int> pii;

int tn,t,x,s,r,n,b,e,cur,w,len;
pii mas[10000];
double ans;

int main()
{
#ifdef HOME
freopen("input.txt", "r",stdin);
freopen("output.txt", "w", stdout);
//DEBUG = true;
#endif
scanf("%d", &tn);
fr(test,tn)	
	{
	scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
	double tim = t;
	r-=s;
	cur = len = 0;
	fr(i,n)
		{
		scanf("%d%d%d", &b, &e, &w);
		if(b>cur) mas[len++] = MP(s,b-cur);
		mas[len++] = MP(w+s,e-b);
		cur = e;
		}
	if(cur<x) mas[len++] = MP(s,x-cur);
	sort(mas,mas+len);
	if(DEBUG)
		{
		fr(i,len)
			cout<<i<<": "<<mas[i].X<<" "<<mas[i].Y<<endl;
		}
	cur = 0;
	ans = 0;
	while(cur<len&&tim>0)
		{
		dbg(cur);
		dbg(ans);
		dbg(tim);
		if((r+mas[cur].X)*tim>mas[cur].Y)
			{
			dline("first");
			double temp=(mas[cur].Y*1.0/(r+mas[cur].X));			
			dbg(temp);
			ans+=temp;
			tim-=temp;
			}
		else 
			{
			dline("second");
			double td = (r+mas[cur].X)*tim;
			dbg(td);
			ans+=tim;
			ans+=(mas[cur].Y-td)/mas[cur].X;
			dbg(ans);
			cur++;
			break;
			}			
		dbg(ans);
		dbg(tim);

		cur++;
		}
	while(cur<len)
		{
		dbg(cur);
		ans+=mas[cur].Y*1.0/mas[cur].X;
		cur++;
		}
	printf("Case #%d: %.8lf", test+1, ans);
	if(test<tn-1) printf("\n"); 
	}
return 0;
}
