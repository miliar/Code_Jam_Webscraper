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

char InputFileNames[4][20] = {"B-sample.in", "B-small.in", "B-large.in", "B-test.in"};
char OutputFileNames[4][20] = {"B-sample.out", "B-small.out", "B-large.out", "B-test.out"};

enum{SAMPLE=0, SMALL, LARGE, TEST};


#define SIZE 105
int a[SIZE][SIZE];
int b[SIZE][SIZE];
bool done[SIZE];
char mapping[SIZE];

int dr[4] = {-1, 0, 0, 1};
int dc[4] = {0, -1, 1, 0}; 

int R, C;

bool in(int x, int y){
	if(x>=0 && x<R && y>=0 && y<C)return true;
	else return false;
}

int dfs(int x, int y){
	if(b[x][y]!=0){
		return b[x][y];
	}

	int val = 1000000;
	int xx = 0;
	int yy = 0;
	int i;
	rep(i, 4){
		int u = x + dr[i];
		int v = y + dc[i];

		if(in(u, v)==true){
			if(a[u][v] < val){
				val = a[u][v];
				xx = u;
				yy = v;
			}
		}
	}
	b[x][y] = dfs(xx, yy);
	return b[x][y];
}

int main (void){
	int CUR = LARGE;
	freopen(InputFileNames[CUR], "r", stdin);
	freopen(OutputFileNames[CUR], "w", stdout);

	int T = INT;
	int i, j, k;

	for(int t=1; t<=T; ++t){
		
		R = INT;
		C = INT;
		
		rep(i, R)rep(j, C)a[i][j] = INT;

		memset(b, 0, sizeof(b));

		int cur = 1;

		rep(i, R)rep(j, C){
			int c = 0;
			rep(k, 4){
				int x = i + dr[k];
				int y = j + dc[k];

				if(in(x, y) && a[x][y]<a[i][j])c++;
			}
			if(c==0){
				b[i][j] = cur++;
			}
		}

		rep(i, R)rep(j, C){
			if(b[i][j]==0){
				dfs(i, j);
			}
		}

		for(i=1; i<cur; ++i){
			mapping[i] = '#';
		}
		
		char ch = 'a';
		rep(i, R)rep(j, C){
			if(mapping[b[i][j]]=='#'){
				mapping[b[i][j]] = ch;
				ch = ch + 1;
			}
		}
		
		
		printf("Case #%d:\n",t);
		rep(i, R){
			rep(j, C){
				if(j)putchar(' ');
				printf("%c",mapping[b[i][j]]);
			}
			printf("\n");
		}
	}

	return 0;
}
