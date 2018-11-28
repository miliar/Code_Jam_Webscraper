#pragma warning( disable : 4786 )
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <queue>
using namespace std;

#ifdef _MSC_VER
	typedef __int64 i64; 
	typedef unsigned __int64 u64;
	#define I64 "%I64d"
	#define U64 "%I64u"
#else
	typedef long long i64; 
	typedef unsigned long long u64;
	#define I64 "%lld"
	#define U64 "%llu"
#endif

#define mabs(x) ((x)<0?(-(x)):(x))
#define mmin(a,b) ((a)>(b)?(b):(a))
#define mmax(a,b) ((a)<(b)?(b):(a))
#define sq(x) ((x)*(x))
#define idig(x) ((x)>='0' && (x)<='9')

#define eq(a,b) (a - b < EPS && b - a < EPS) 
#define les(a, b) (b - a > EPS) 

#define VV vector
typedef vector<int> VI; 
typedef vector<string> VS; 
typedef vector<double> VD; 
typedef vector<i64> VL;
typedef vector<VI> VVI; 
typedef vector<VS> VVS; 
typedef pair<int,int> PII;

#define PB push_back
#define SZ size()
#define CS c_str()
#define CL clear()
#define MP(a,b) make_pair((a),(b))

#define rab(i,l,h) for((i)=l;(i)<=h;++(i))
#define rba(i,h,l) for((i)=h;(i)>=l;--(i))
#define rep(i,n) for((i)=0;(i)<(n);++(i))
#define repi(i,n) for((i)=(n-1);(i)>=(0);--(i))

#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),c) != (c).end()) 

// tostring
string itos (int i){ stringstream s; s << i; return s.str(); }
string i64tos (i64 i){ char s[51];sprintf(s,I64,i);string ss=s;return ss; }

template <class T>
void SWAP(T &x, T &y){T z=x; x=y; y=z;}

#define EPS 1e-7
#define INF 1e10

#define Z 1001
bool p[Z];
vector<int> primes;
bool adj[Z][Z];
bool vis[Z];


void dfs(int u, int a, int b){
	if(vis[u]==true)return;
	
	vis[u]=true;

	int i;
	for(i=a;i<=b;++i)if(adj[u][i]==true)dfs(i,a,b);
}

int main (void){
	int i, j, k;

	//freopen("B-sample.in","r",stdin);
	//freopen("B-sample.out","w",stdout);

	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small.out","w",stdout);

	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);

	primes.clear();
	rep(i,Z)p[i]=true;
	p[0]=false;
	p[1]=false;
	for(i=2;i*i<Z;++i){
		if(p[i]==true){
			for(j=i+i;j<Z;j+=i)p[j]=false;
		}
	}

	rep(i,Z)if(p[i])primes.push_back(i);
	
	//cout<<primes.size()<<endl;
	int T;
	scanf("%d",&T);
	int t;

	rep(t,T){
		int A, B, P;
		scanf("%d%d%d",&A,&B,&P);
		
		memset(adj,0,sizeof(adj));

		for(i=A;i<=B;++i){
			for(j=i+1;j<=B;++j){
				if(adj[i][j]==true)continue;

				for(k=0;k<primes.size();++k){
					if(primes[k]<P)continue;
					
					if( i%primes[k]==0 && j%primes[k]==0){
						adj[i][j]=adj[j][i]=true;
						break;
					}
				}
			}
		}

		int res = 0;
		memset(vis, 0, sizeof(vis));

		for(i=A;i<=B;++i){
			if(vis[i]==false){
				dfs(i, A, B);
				res++;
			}
		}

		printf("Case #%d: %d\n",t+1,res);
	}

	
	return 0;
}