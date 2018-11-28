#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <utility>
#include <complex>
#include <valarray>
#include <deque>
using namespace std;

typedef long long ll;
typedef vector<int> vi;

#define RI( i, o ) for(typeof(o.begin()) i= (o).begin(); i!=(o).end(); ++i)
#define RP3( x, y, z ) RP( i, 0, x ) RP( j, 0, y ) RP( k, 0, z )
#define RP( i, s, e ) for(typeof(s) i=(s); i<(e); ++i)
#define R( i, x ) RP(i,0,(x).size())
#define pB push_back


const ll mod=212275933234147823LL;
ll vv[110];

int gr1[110][110];
int gr1l[110];
ll gr1h[110];

int gr2[110][110];
int gr2l[110];
ll gr2h[110];
int Y;

void cons1(int p, vector<vi > g, int ss)
{
	gr1l[p]=0;
	R(i,g[p]) if(gr1l[g[p][i]]==-1 && (ss&(1<<g[p][i]))){
		cons1(g[p][i],g, ss);
		gr1[p][gr1l[p]]=g[p][i];
		++gr1l[p];
		}
}

void cons2(int p, vector<vi > g)
{
	gr2l[p]=0;
	R(i,g[p]) if(gr2l[g[p][i]]==-1){
		cons2(g[p][i],g);
		gr2[p][gr2l[p]]=g[p][i];
		++gr2l[p];
		}
}

ll chk1(int p)
{
	ll& m=gr1h[p]=1;
	vector<ll> vals;
	
	RP(i,0,gr1l[p]) vals.pB(chk1(gr1[p][i]));
	sort(vals.begin(), vals.end());
	R(i,vals) {m+=vals[i]*vv[i]; m%=mod;}
	return m;
}

ll chk2(int p)
{
	ll& m=gr2h[p]=1;
	vector<ll> vals;
	
	RP(i,0,gr2l[p]) vals.pB(chk2(gr2[p][i]));
	sort(vals.begin(), vals.end());
	R(i,vals) {m+=vals[i]*vv[i]; m%=mod;}
	return m;
}

int mg(int p, int q)
{
	if(gr1h[p] !=gr2h[q]) return 0;
	return 1;
}

//Problem D
int main()
{
	int N;
	cin >> N;
	
	srand(0);
	RP(i,0,110) vv[i]=abs(rand()*217227591473LL+rand()*12673681LL+rand()*31577+rand())%mod;
	
	RP(cs, 1, N+1)
	{
		
		cout << "Case #" << cs << ": ";
		int c, n, m, x, y;
		cin >> n;
		vector<vector<int> > g1(n,vector<int>());
		RP(i,0,n-1)
		{
			cin >> x >> y;
			--x; --y;
			g1[x].push_back(y);
			g1[y].push_back(x);
		}
		cin >> m;
		vector<vector<int> > g2(m,vector<int>());
		RP(i,0,m-1)
		{
			cin >> x >> y;
			--x; --y;
			g2[x].push_back(y);
			g2[y].push_back(x);
		}
		Y=0;
		RP(ss,0,(1<<n))
		RP(s,0,n)
			RP(e,0,m)
			
			if(ss&(1<<s))
			{
				memset(gr1,0,sizeof(gr1));
				memset(gr2,0,sizeof(gr2));
				memset(gr1l,-1,sizeof(gr1l));
				
				memset(gr1h,-1,sizeof(gr1h));
				memset(gr2l,-1,sizeof(gr2l));
				memset(gr2h,-1,sizeof(gr2h));
				
				cons1(s,g1, ss);
				cons2(e,g2);
				
				chk1(s);
				chk2(e);
				
				Y=mg(s,e);
				/*
				RP(u,0,n) cout << gr1h[u] << " "; cout << endl;
				RP(u,0,m) cout << gr2h[u] << " "; cout << endl;
				cout << endl;*/
				
				if(Y==1) goto end;
				
				
			}
		end:;
		if(Y) cout << "YES" << endl; else cout << "NO" << endl;
	}
	return 0;
}
