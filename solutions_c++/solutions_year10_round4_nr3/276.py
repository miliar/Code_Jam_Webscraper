#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>
#include <complex>
using namespace std;

#define ME(s) memset((s), 0, sizeof((s)))
#define MM(s,a) memset((s),(a),sizeof((s)))
#define MCP(s,a) memcpy((s), (a), sizeof(s))
#define LL long long
#define LD long double
#define PII pair<int, int>
#define PDD pair<double, double>
#define mkp(a,b) make_pair((a),(b))
#define y first
#define x second
#define sqr(a) ((a)*(a))
#define lowbit(x) ((x)&(-(x)))
#define two(x) (1<<(x))
#define contain(mask,x) (((mask)&two(x))!=0)

#define OFFLINEJUDGE

#ifdef OFFLINEJUDGE
FILE *fin=freopen("C.in","r",stdin);
FILE *fout=freopen("C.out","w",stdout);
#else
FILE *fin=stdin;
FILE *fout=stdout;
#endif
int T,R,a[111][111],ans,g[111][111];

int work(){
	for(int i=1;;i++){
//		cerr << i << endl;
		memset(g,0,sizeof(g));
		for(int x=1;x<=100;x++)
			for(int y=1;y<=100;y++)
				if(!a[x][y-1]&&!a[x-1][y]&&a[x][y])
					g[x][y]=0;
				else if(a[x][y-1]&&a[x-1][y]&&!a[x][y])
					g[x][y]=1;
				else
					g[x][y]=a[x][y];
		memcpy(a,g,sizeof(g));
		int flag=0;
		for(int x=1;x<=100;x++){
			for(int y=1;y<=100;y++){
				flag|=g[x][y];
			//	cerr << g[x][y] ;
			}
//			cerr << endl;
		}
		if(!flag){
			ans=i;
			break;
		}
	}
}

int main(){
	cin >> T;
	for(int c=1;c<=T;c++){
		cin >> R ;
		memset(a,0,sizeof(a));
		for(int i=0;i<R;i++){
			int x,xx,y,yy;
			cin >> x >> y >> xx >> yy;
			for(int i=x;i<=xx;i++)
				for(int j=y;j<=yy;j++)
					a[i][j]=1;//++
		}
		work();
		fprintf(fout,"Case #%d: %d\n",c,ans);
	}
}
