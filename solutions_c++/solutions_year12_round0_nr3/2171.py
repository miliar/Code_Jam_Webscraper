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
#define SIZ 3000000

bool DEBUG = false;

using namespace std;

int t,decs,r;
set<int> mas[SIZ];
int a,b;

int main()
{
freopen("C-large.in", "r",stdin);
freopen("output.txt", "w", stdout);
#ifdef HOME
DEBUG = true;
#endif
decs = 1;
fw(i,1,2000000)
	{
	if(i==decs*10) 
		{
		decs*=10;
		r++;
		}
	int val = i;
	fr(j,r)
		{
		int rest = val%10;
		val = rest*decs+val/10;
		if(val>i) mas[i].insert(val);
		}	
	/*
	cout<<i<<": ";
	fr(j,l[i])
		cout<<mas[i][j]<<" ";
	cout<<endl;
        */
	}
cin>>t;
fw(test,1,t)
	{
	cin>>a>>b;
	int ans = 0;
	fw(i,a,b)
		for(set<int>::iterator it = mas[i].begin(); it!=mas[i].end() ;it++)
			if((*it)<=b) 
				{
//				cout<<i<<" "<<(*it)<<endl;
				ans++;
				}
	cout<<"Case #"<<test<<": "<<ans;
	if(test<t) cout<<endl;
	}
return 0;
}
