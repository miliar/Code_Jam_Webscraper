#define _CRT_SECURE_NO_WARNINGS
#include <map> 
#include <set> 
#include <queue> 
#include <bitset> 
#include <valarray> 
#include <complex> 
#include <iostream> 
#include <sstream> 
#include <cmath> 
#include <algorithm> 
#include <string> 
#include <cassert>
#include <ctime>

#ifdef _MSC_VER
#pragma comment(linker,"/STACK:20000000")
#endif

using namespace std;

// prewritten code

#define Size(x) (int)(x).size()
#define For(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define Ford(i,a,b) for(int i=(int)(a);i>=(int)(b);--i) 
#define RepV(i,v) for (int i=0;i<Size(v);++i)
#define All(c) (c).begin(),(c).end()
#define Fill(a,b) memset(&a,b,sizeof(a))
#define Min(a,b) ((a)<(b)?(a):(b))
#define Max(a,b) ((a)>(b)?(a):(b))
#define Abs(a) ((a)<0?-(a):(a))
#define VVI vector<vector<int> >
#define VI vector<int>
#define VVS vector<vector<string> >
#define VS vector<string>
#define ForEach(it,a) for (typeof((a).begin()) it=(a).begin(); it!=(a).end(); ++it)
#define DBG(x) cout << #x <<" = "<< x << endl;
#define DBGA(x) {cout << #x <<": "; for (int i=0; i<(int)sizeof(x)/(int)sizeof(x[0]); ++i) cout<<x[i]<<' '; cout<<endl;}
#define DBGV(x) {cout << #x <<": "; for (int i=0; i<(int)Size(x); ++i) cout<<x[i]<<' '; cout<<endl;}
#define PB push_back
#define MP make_pair

const string problem_name = "1";

const int dx[] = {0,1,0,-1};
const int dy[] = {1,0,-1,0};

char good[6005][60005];
int minY[6005], maxY[6005], minX[6005], maxX[6005];

VI X, Y;

inline bool g(int x, int y){
	return (minX[x+3000]<=y && maxX[x+3000]>=y) || (minY[y+3000]<=x && maxY[y+3000]>=x);
}

void solve_case(){
	Fill(good,0);
	int l;
	scanf("%d",&l);
	string path="";
	For(i,1,l) {
		string s;
		int t;
		cin >> s;
		cin >> t;

		For(j,1,t) path+=s;
	}
	X.clear(); Y.clear();

	For(i,-3000,3000) minX[i+3000]=1000000000, minY[i+3000]=1000000000, maxX[i+3000]=-1000000000, maxY[i+3000]=-1000000000;

	int dir = 0, x=0, y=0;
	RepV(i,path) {
		good[x+3000][y+3000]=1;
		
		minX[x+3000]=Min(minX[x+3000],y);
		maxX[x+3000]=Max(maxX[x+3000],y);
		minY[y+3000]=Min(minY[y+3000],x);
		maxY[y+3000]=Max(maxY[y+3000],x);

		X.push_back(x); Y.push_back(y);
		if (path[i] == 'F'){
			x += dx[dir];
			y += dy[dir];
		} else if (path[i]=='L'){
			dir = (dir+3)%4;
		} else {
			dir = (dir+1)%4;
		}
	}
	long long sq = 0;
	For(i,-3000,3000) For(j,-3000,3000) {
		if (g(i,j) && g(i+1,j) && g(i+1,j+1) && g(i,j+1)) {
			sq += 1;
		}
	}
	X.push_back(0); Y.push_back(0);

	long long sq2=0;
	For(i,0,Size(X)-2) sq2 += X[i]*Y[i+1]-X[i+1]*Y[i];

	//DBGV(X); DBGV(Y);
	sq -= Abs(sq2)/2;

	cout << sq << endl;
}

int main(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
	
	int _t;
	scanf("%d\n",&_t);
	
	For(_z,1,_t){
		printf("Case #%d: ",_z);
		
		solve_case();
		
		fflush(stdout);
	}
	
	return 0;
}
