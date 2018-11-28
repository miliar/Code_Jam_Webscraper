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
#include<string>

using namespace std;

#define s(n)					scanf("%d",&n)
#define sl(n) 					scanf("%lld",&n)
#define sf(n) 					scanf("%lf",&n)
#define ss(n) 					scanf("%s",n)
#define INF						(int)1e9
#define LINF					(long long)1e18
#define EPS						1e-9
#define maX(a,b)				((a)>(b)?(a):(b))
#define miN(a,b)				((a)<(b)?(a):(b))
#define abS(x)					((x)<0?-(x):(x))
#define FOR(i,a,b)				for(int i=a;i<b;i++)
#define REP(i,n)				FOR(i,0,n)
#define foreach(v,c)            for( typeof((c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define mp						make_pair
#define FF						first
#define SS						second
#define tri(a,b,c)				mp(a,mp(b,c))
#define XX						first
#define YY						second.first
#define ZZ						second.second
#define pb						push_back
#define fill(a,v) 				memset(a,v,sizeof a)
#define all(x)					x.begin(),x.end()
#define SZ(v)					((int)(v.size()))
#define DREP(a)					sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)			(lower_bound(all(arr),ind)-arr.begin())
#define debug(args...)			{dbg,args; cerr<<endl;}
#define dline					cerr<<endl	

void sc(char &c){
	char temp[4];	ss(temp);	
	c=temp[0];
}

struct debugger
{
	template<typename T> debugger& operator , (const T& v)
	{	
		cerr<<v<<" ";	
		return *this;	
	}
} dbg;

void debugarr(int * arr,int n)
{
	cout<<"[";
	for(int i=0;i<n;i++)
		cout<<arr[i]<<" ";
	cout<<"]"<<endl;
}





typedef long long LL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef pair<int,PII> TRI;

typedef vector<int> VI;
typedef vector<LL> VL;
typedef vector<PII> VII;
typedef vector<PLL> VLL;
typedef vector<TRI> VT;

typedef vector<VI> VVI;
typedef vector<VL> VVL;
typedef vector<VII> VVII;
typedef vector<VLL> VVLL;
typedef vector<VT> VVT;


/*Main code begins now */

int testnum;
int N,R,C;
int r[1005];
int px[1005];
int py[1005];
set<int> candx;
set<int> candy;

VII z;

void solve()
{
	fill(px,-1);
	fill(py,-1);
	candx.clear();
	candy.clear();
	candx.insert(-INF);
	candy.insert(-INF);
	for(int ind=N-1;ind>=0;ind--)
	{
		int i = z[ind].SS;
		
		bool found = false;
		
		
		for(set<int>::iterator itx = candx.begin(); itx!=candx.end(); itx++)
		{
			for(set<int>::iterator ity = candy.begin(); ity!=candy.end(); ity++)
			{
				//debug(*itx,*ity);
				int cx = (*itx)+r[i];
				int cy = (*ity)+r[i];
				if(cx<0) cx=0;
				if(cy<0) cy=0;
				if(cx>R) cx=R;
				if(cy>C) cy=C;
				
				
				
				bool ok=true;
				for(int l=0;l<N;l++)
				{
					if(px[l]<0) continue;
					int dx = abs(px[l]-cx);
					int dy = abs(py[l]-cy);
					if(dx<r[i]+r[l] && dy<r[i]+r[l])
					{
						ok=false;
						continue;
					}
				}
				
				if(ok)
				{
					px[i] = cx;
					py[i] = cy;
					candx.insert(cx-r[i]);
					candy.insert(cy-r[i]);
					candx.insert(cx+r[i]);
					candy.insert(cy+r[i]);
					found=true;
					//debug("placed",i);
					break;
				}
				if(found) break;
			}
			//debug("found",found);
			if(found) break;
		}
		
		assert(found);
	}
	
	printf("Case #%d:",testnum);
	for(int i=0;i<N;i++)
		printf(" %d %d",px[i],py[i]);
	printf("\n");
		
		
}

bool input()
{
	s(N); s(R); s(C);
	z.clear();
	for(int i=0;i<N;i++)
	{
		s(r[i]);
		z.pb(mp(r[i],i));
	}
	sort(all(z));
	return true;
}


int main()
{
	int T; s(T);
	for(testnum=1;testnum<=T;testnum++)
	{
		if(!input()) break;
		solve();
	}
}
