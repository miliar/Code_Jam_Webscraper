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

#define EPS 1e-7
#define INF 1e10

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

#define CLR(c, v) memset(c, v, sizeof(c))

int getInt(void){
	int d;
	scanf("%d",&d);
	return d;
}

#define INT getInt()

char inFile[3][30]={
	"A-sample.in",
	"A-small.in",
	"A-large.in"
};

char outFile[3][30]={
	"A-sample.out",
	"A-small.out",
	"A-large.out"
};

#define fileInd 2
#define problemId 'A'

#define inf 100000
#define Z 10100 

#define AND 1
#define OR 0

int M;
int memo[Z][2];
int G[Z];
int C[Z];
int I[Z];

#define left(n) (2*n)
#define right(n) (2*n+1)

int go(int node, int target){
	int &ret = memo[node][target];
	if(-1!=ret)return ret;

	if( node > ( (M-1)/2 ) ){ //child node
		//cout<<node<<endl;
		if( I[node] == target ) return ret = 0;
		else return ret = inf;
	}

	ret = inf;
	int temp;

	if( G[node] == AND ){
		if( target == 0 ){
			temp = go( left(node), 0) + go( right(node), 1);
			ret = mmin(ret, temp);

			temp = go( left(node), 1) + go( right(node), 0);
			ret = mmin(ret, temp);

			temp = go( left(node), 0) + go( right(node), 0);
			ret = mmin(ret, temp);
		}
		else{
			temp = go( left(node), 1) + go( right(node), 1);
			ret = mmin(ret, temp);
		}
	}
	else{
		if( target == 1 ){
			temp = go( left(node), 0) + go( right(node), 1);
			ret = mmin(ret, temp);

			temp = go( left(node), 1) + go( right(node), 0);
			ret = mmin(ret, temp);

			temp = go( left(node), 1) + go( right(node), 1);
			ret = mmin(ret, temp);
		}
		else{
			temp = go( left(node), 0) + go( right(node), 0);
			ret = mmin(ret, temp);
		}
	}


	if(C[node]==1){
		if( G[node] == OR ){
			if( target == 0 ){
				temp = go( left(node), 0) + go( right(node), 1) + 1;
				ret = mmin(ret, temp);

				temp = go( left(node), 1) + go( right(node), 0) + 1;
				ret = mmin(ret, temp);

				temp = go( left(node), 0) + go( right(node), 0) + 1;
				ret = mmin(ret, temp);
			}
			else{
				temp = go( left(node), 1) + go( right(node), 1) + 1;
				ret = mmin(ret, temp);
			}
		}
		else{
			if( target == 1 ){
				temp = go( left(node), 0) + go( right(node), 1) + 1;
				ret = mmin(ret, temp);

				temp = go( left(node), 1) + go( right(node), 0) + 1;
				ret = mmin(ret, temp);

				temp = go( left(node), 1) + go( right(node), 1) + 1;
				ret = mmin(ret, temp);
			}
			else{
				temp = go( left(node), 0) + go( right(node), 0) + 1;
				ret = mmin(ret, temp);
			}
		}

	}

	return ret;
}

int main (void){
	int i, j, k;
	int T, t; // test case number

	inFile[fileInd][0] = problemId;
	outFile[fileInd][0] = problemId;
	freopen(inFile[fileInd], "r", stdin);
	freopen(outFile[fileInd], "w", stdout);


	// start code here 
	T = INT;
	rep(t, T){
		M = INT;
		int tar = INT;

		for(i = 1; i<=M; ++i){
			if( i<= ((M-1)/2) ){
				G[i] = INT;
				C[i] = INT;
			}
			else{
				I[i] = INT;
			}
		}

		CLR(memo, -1);

		int res = go(1, tar);

		printf("Case #%d: ",t+1);
		if( res > M ){
			printf("IMPOSSIBLE\n");
		}
		else{
			printf("%d\n",res);
		}
	}

	return 0;
}
