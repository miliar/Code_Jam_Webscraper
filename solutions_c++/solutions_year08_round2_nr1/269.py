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

int x[100001], y[100001];
int xy[3][3];

int px[9];
int py[9];

int main (void){
	int i, j, k, l, m, n;

	//freopen("A-sample.in","r",stdin);
	//freopen("A-sample.out","w",stdout);

	//freopen("A-small.in","r",stdin);
	//freopen("A-small-1.out","w",stdout);

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	//cout<<T<<endl;
	int t;
	rep(t, T){
		//cout<<t<<endl;
		int n, A, B, C, D, X, Y, M;
		scanf("%d%d%d%d%d%d%d%d",&n,&A,&B,&C,&D,&X,&Y,&M);
		x[0]=X;
		y[0]=Y;
		for(i=1;i<n;++i){
			x[i]=((i64)A*x[i-1]+B)%M;
			y[i]=((i64)C*y[i-1]+D)%M;
		//	cout<<i<<" "<<x[i]<<" "<<y[i]<<endl;
		}

		//cout<<"Ah"<<endl;
		rep(i, 3)rep(j, 3)xy[i][j]=0;

		rep(i, n){
			xy[ x[i]%3 ][ y[i]%3 ]++ ;
		}


		i64 res = 0;
		/*rep(i, 3)rep(j, 3){
			int v = xy[i][j];
			if(xy[i][j] >= 3)
				res = res + ((i64)v*(v-1)*(v-2))/6;
		}*/

		k = 0;
		rep(i, 3)rep(j, 3){
			px[k]=i;
			py[k]=j;
			k++;
		}

		
		i64 v, w, z;
		rep(i, 9)for(j=i;j<9;++j)for(k=j;k<9;++k){
		
			if(i==j && j==k){
				v = xy[px[i]][py[i]];
				if(v>=3)res = res + (v*(v-1)*(v-2))/6;
			}
			else if(i==j){
				if( ( px[i]+px[i]+px[k])%3 == 0  && ( py[i]+py[i]+py[k])%3 == 0 ){
					v = xy[ px[i] ][ py[i] ];
					w = xy[ px[k] ][ py[k] ];

					if( v >=2 ) res  = res + ( (v*(v-1))/2 )*w;
				}
			}
			else if(j==k){
				if( ( px[i]+px[j]+px[j])%3 == 0  && ( py[i]+py[j]+py[j])%3 == 0 ){
					v = xy[ px[j] ][ py[j] ];
					w = xy[ px[i] ][ py[i] ];

					if( v >=2 ) res  = res + ( (v*(v-1))/2 )*w;
				}
			}
			else{
				if( ( px[i]+px[j]+px[k])%3 == 0  && ( py[i]+py[j]+py[k])%3 == 0 ){
					v = xy[ px[i] ][ py[i] ];
					w = xy[ px[j] ][ py[j] ];
					z = xy[ px[k] ][ py[k] ];

					res = res + v*w*z;
				}
			}
		}
		
		//rep(i,n)cout<<x[i]<<" "<<y[i]<<endl;

		/*int x1, x2, x3, y1, y2, y3, res=0;
		for(i=0;i<n;++i){
			x1 = x[i]%3;
			y1 = y[i]%3;
			for(j=i+1;j<n;++j){
				x2 = x[j]%3;
				y2 = y[j]%3;
				for(k=j+1;k<n;++k){
					x3 = x[k]%3;
					y3 = y[k]%3;

					if( (x1+x2+x3)%3 ==0 && (y1+y2+y3)%3==0 )res++;
				}
			}
		}*/
		printf("Case #%d: "I64"\n",t+1,res);
	}
	return 0;
}