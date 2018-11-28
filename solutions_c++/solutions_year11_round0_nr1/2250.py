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

pair<char,int> mas[100];
int t,n,cur,maxim,poso,posb,curo,curb;
bool mark[1000000];

int main()
{
#ifdef HOME
freopen("input.txt", "r",stdin);
freopen("output.txt", "w", stdout);
DEBUG = true;
#endif
cin>>t;
fr(test,t)
	{
	cin>>n;
	fr(i,n)
		cin>>mas[i].X>>mas[i].Y;
	maxim = 0;
	curo = curb = 0;
	poso = posb = 1;
	fr(i,n)
		{
		if(mas[i].X=='O')
			{
			while(poso!=mas[i].Y)
				{
				if(poso>mas[i].Y) poso--;
				else poso++;
				curo++;
				}
			while(curo<curb) curo++;
			curo++;
			}
		else 
			{
			while(posb!=mas[i].Y)
				{
				if(posb>mas[i].Y) posb--;
				else posb++;
				curb++;
				}
			while(curb<curo) curb++;
			curb++;
			}
		}
	maxim = mx(curo,curb);
	printf("Case #%d: %d", test+1, maxim);
	if(test!=t-1) printf("\n");
	}
return 0;
}
