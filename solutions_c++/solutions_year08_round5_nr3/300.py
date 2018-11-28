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

#define eq(a,b) (a - b < EPS && b - a < EPS) 
#define les(a, b) (b - a > EPS) 

#define VV vector
typedef vector<int> VI; 
typedef vector<string> VS; 
typedef vector<double> VD; 
typedef vector<i64> VL;
typedef vector< VL > VVL;
typedef vector< VI > VVI; 
typedef vector<VS> VVS; 

typedef pair<int,int> PII;
typedef pair<string, string> PSS;
typedef pair<string, int> PSI;
typedef pair<int, string> PIS;

typedef vector< PII > VPII;

typedef map<string, int> MSI;
typedef map<int, string> MIS;

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

#define FOR(v, it) for(it = v.begin(); it!=v.end(); ++it)
#define foreach(vtype, v, it) for(vtype::iterator it = v.begin(); it!=v.end(); ++it)

// tostring
string itos (int i){ stringstream s; s << i; return s.str(); }
string i64tos (i64 i){ char s[51];sprintf(s,I64,i);string ss=s;return ss; }

template <class T>
void SWAP(T &x, T &y){T z=x; x=y; y=z;}

#define dbg(x) cout << #x << " -> " << (x) << "\t";
#define dbge(x) cout << #x << " -> " << (x) << endl;

#define CLR(c, v) memset(c, v, sizeof(c))

int getInt(void){
	int d;
	scanf("%d",&d);
	return d;
}
#define INT getInt()

//clockwise
int move[4][2]={
	-1, 0, 
	0, -1, 
	1, 0, 
	0, 1
};

//clockwise
int kmove[8][2]={
	-2, -1, 
	-1, -2,
	1, -2,
	2, -1,
	2, 1,
	1, 2,
	-1, 2,
	-2, 1
};

////////////////////////////////////////////////////////////
//               INPUT FROM FILE                          //
////////////////////////////////////////////////////////////
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
////////////////////////////////////////////////////////////

#define Z 100
char g[Z][Z];
int R, C;

i64 memo[Z][1<<10];

bool valid(int s1, int s2, int r){
	int i;
	rep(i, C-1){
		if( s2&(1<<i) && s2&(1<<(i+1)) )return false;
	}

	//cout<<r<<endl;

	//rep(i, C)cout<<g[r][i]<<" ";cout<<endl;
	//printf("%s\n",g[r]);
	rep(i, C){
		//dbg(r); dbg(i); printf("?%c?\n",g[r][i]);
		if( (s2&(1<<i) ) && g[r][i] == 'x' ) {
			
			return false;
		}
	}

	rep(i, C){
		if( s2&(1<<i) ){
			if( i > 0 ){
				if( s1&(1<<(i-1)) )return false; 
			}
			if( i < C-1 ){
				if( s1&(1<<(i+1)) )return false;
			}
		}
	}
	return true;
}

int bitCount(int s){
	if(s == 0)return 0;
	else return (s%2) + bitCount(s/2);
}

i64 go(int r, int state){
	i64 &ret = memo[r][state];
	if(-1!=ret)return ret;
	if( r == R ) return ret = 0;
	//cout<< r << " "<<state<<endl;

	int high = 1<<C;
	
	int i;
	ret = 0;
	i64 temp;
	rep(i, high){
		
		//if( valid(state, high, r)==false) cout<<"ouch"<<endl;
		if( valid(state, i, r) ){
			//cout<<state<<" "<<i<<" "<<r<<endl;
			temp = go(r+1, i) + bitCount(i);
			ret = mmax( ret, temp );
		}
	}

	return ret;
}

int main (void){
	int fileInd = 1;
	char problemId = 'C';
	inFile[fileInd][0] = problemId;
	outFile[fileInd][0] = problemId;
	freopen(inFile[fileInd], "r", stdin);
	freopen(outFile[fileInd], "w", stdout);

	int i, j, k;
	VI::iterator it;

	int t, T;
	T = INT;
	

	rep(t, T){
		R = INT;
		C = INT;

		rep(i, R)scanf("%s",&g[i]);
		CLR(memo, -1);

		i64 res = go(0, 0);


		printf("Case #%d: "I64,t+1,res);
		
		printf("\n");
	}

	return 0;
}
