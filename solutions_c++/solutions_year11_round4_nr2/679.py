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

int tn,r,c,d,w;
char mas[1000][1000];

int main()
{
#ifdef HOME
freopen("input.txt", "r",stdin);
freopen("output.txt", "w", stdout);
//DEBUG = true;
#endif
scanf("%d\n", &tn);
fw(test,1,tn)
	{
	scanf("%d%d%d\n", &r, &c, &d);
	fr(i,r)
		gets(mas[i]);
	fr(i,r)
	fr(j,c)
		mas[i][j]-='0';
	bool solved = false;
	int minim = mn(r,c);
	dbg(minim);
	df(l,minim,3)
		{
		if(DEBUG) cout<<"Length: "<<l<<endl;
		fw(i,0,r-l)
		fw(j,0,c-l)
			{
			int sx = 0, sy = 0;
			int cx = 2*i+l-1;
			int cy = 2*j+l-1;
			fe(x,i,i+l)
			fe(y,j,j+l)
				{
				bool s1,s2;
				s1 = s2 = false;
				if(x==i||x==i+l-1) s1 = true;
				if(y==j||y==j+l-1) s2 = true;
				if(s1&&s2) continue;
				sx+=mas[x][y]*(2*x-cx);
				sy+=mas[x][y]*(2*y-cy);
				if(DEBUG) cout<<"Eval: "<<sx<<" "<<sy<<endl;
				}
			if(DEBUG) cout<<"Sum("<<i<<","<<j<<"): "<<sx<<" "<<sy<<endl;
			if(sx==0&&sy==0)
				{
				if(DEBUG) cout<<"Ans: "<<i<<" "<<j<<endl;
				printf("Case #%d: %d",test, l);
				if(test<tn) puts("");
				solved = true;
				goto A;
				}
			}
		}
	A:
	if(!solved) 
		{
		printf("Case #%d: IMPOSSIBLE",test);
		if(test<tn) puts("");
		}
	}
return 0;
}
