#include <cstdio>
#include <memory>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <complex>
#include <string>
#include <cstring>
#include <cmath>
#include <ctime>
#include <iostream>
#include <fstream>
#include <functional>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef short int si;
typedef long double ld;
typedef pair<int,int> pii;
#define rep(x,y,z) for(int x=(y),e##x=(z);x<e##x;x++)

const double PI=acos(-1.0);

template<class T> inline T SQR(T a){return a*a;}

#define __small
//#define __large

void test(int T)
{
	ll l,t,n,c;
	cin>>l>>t>>n>>c;
	
	if (c>1000 || n>1000 || (l!=0 && l!=1 && l!=2))
		int as=1;
	n++;
	ll A[3000];
	rep(i,1,c+1)
		scanf("%lld",A+i);
	A[0]=0;
	for (int i=c+1;i<n;i+=c)
		rep(j,0,c)
			A[i+j]=A[j+1];
	ll sum=0;
	rep(i,0,n)
		sum+=A[i];
	ll ans=sum*2;
	if (T==50)
		int as=1;
	if (l==1)
	{
		ll curr=A[0];
	    ll win=0;
		rep(i,1,n)
		{
			curr+=2*A[i];
			if (curr>t) win=max(win,min(curr-t,2*A[i]));
		}
		ans=2*sum-win/2;
	}
	ll win=0;
	if (l==2)
	{
		ll curri=A[0];
		ll wini=0;
		rep(i,1,n)
		{
			curri+=2*A[i];
			if (curri>t) wini=max(wini,min(curri-t,2*A[i]));
			ll currj=curri-wini/2;
			ll winj=0;
			rep(j,i+1,n)
			{
				currj+=2*A[j];
				if (currj>t) winj=max(winj,min(currj-t,2*A[j]));
				win=max(win,wini+winj);
			}
		}
		ans=2*sum-win/2;
	}
	printf("Case #%d: %lld\n",T,ans);

}

int main()
{
#ifdef __small
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-out.txt","w",stdout);
#endif
#ifdef __large
	freopen("B-large.in","r",stdin);
	freopen("B-large-out.txt","w",stdout);
#endif
	int t;
	cin>>t;
	cerr<<t;
	rep(i,0,t)
		test(i+1);
	return 0;	
}
/*
3
2 20 8 2 3 5
1 4 2 2 10 4
1 0 8 2 1 2
*/