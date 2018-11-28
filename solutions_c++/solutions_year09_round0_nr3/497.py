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

char InputFileNames[4][20] = {"C-sample.in", "C-small.in", "C-large.in", "C-test.in"};
char OutputFileNames[4][20] = {"C-sample.out", "C-small.out", "C-large.out", "C-test.out"};

#define MOD 10000

enum{SAMPLE=0, SMALL, LARGE, TEST};

char s[20] = {"welcome to code jam"};
char buff[1000];

int patternLen, textLen;

int a[1000][20];

int main (void){
	int CUR = LARGE;
	freopen(InputFileNames[CUR], "r", stdin);
	freopen(OutputFileNames[CUR], "w", stdout);
	
	gets(buff);
	int T = atoi(buff);
	patternLen = strlen(s);
	int i, j, k;
	for(int t=1; t<=T; ++t){
		gets(buff);

		textLen = strlen(buff);

		for(i=0; i<textLen; ++i){
			for(j=0; j<patternLen; ++j){
				if(s[j]!=buff[i]){
					a[i][j]=0;
					continue;
				}

				a[i][j] = 0;
				if(j==0){
					a[i][j] = 1;
				}
				else{
					for(k=0; k<i; ++k){
						a[i][j] = (a[i][j] + a[k][j-1])%MOD;
					}
				}
			}
		}

		int res = 0;
		for(int ind = 0; ind<textLen; ++ind){
			res = (res+a[ind][patternLen-1])%MOD;
		}

		printf("Case #%d: %04d\n",t,res);
	}

	return 0;
}
