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
#include <float.h>
#include <string>
#include <cstring>

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

const string problem_name = "2";

int rows, cols, a[200][200];
char res[200][200];

const int dr[]={-1,0,0,1};
const int dc[]={0,-1,1,0};

int basins=0;

char go(int r, int c){
	if (res[r][c]!=0) return res[r][c];
	int best = 1<<30, bestd=-1;
	For(i,0,3) {
		int nr=r+dr[i], nc=c+dc[i];
		if (nr>=0&&nr<rows&&nc>=0&&nc<cols&&a[nr][nc] < best){
			best=a[nr][nc];
			bestd=i;
		}
	}
	if (bestd==-1 || best >= a[r][c]) return res[r][c] = ++basins;
	return res[r][c] = go(r+dr[bestd],c+dc[bestd]);
}

void solve_case(){
	basins=0;
	printf("\n");
	scanf("%d%d",&rows,&cols);
	For(i,0,rows-1) For(j,0,cols-1) scanf("%d",&a[i][j]);
	Fill(res,0);
	For(i,0,rows-1) For(j,0,cols-1) if (res[i][j]==0) go(i,j);

	int b=0;
	char mp[100];
	Fill(mp,0);
	For(i,0,rows-1) For(j,0,cols-1) if (res[i][j]<'a') {
		int cur=res[i][j];
		if (mp[cur] == 0){
			mp[cur] = ++b;
		}
		res[i][j] = mp[cur]-1+'a';
	}
	For(i,0,rows-1){
		For(j,0,cols-1) printf("%c ",res[i][j]);
		printf("\n");
	}
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
