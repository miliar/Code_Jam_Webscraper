#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <vector>
#include <string>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <iostream>
#include <sstream>
using namespace std;

#define size(x) int((x).size())
#define foreach(i,c) for(typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
typedef long long I64; typedef unsigned long long U64;
const double EPS=1e-12;
const int INF=999999999;
typedef vector<int> VI;
typedef vector<string> VS; 

typedef pair<int,int> PII;

int m,n;
int xf,yf;

char g[30][31];
int f[30][30];
bool flag[30][30];
int dx[]={0,0,1,-1};
int dy[]={-1,1,0,0};
int ans;

void findPath()
{
	PII prev[30][30];
	memset(f,-1,sizeof(f));

	PII p;
	queue<PII> Q;

	p=PII(0,0);
	Q.push(p);
	f[0][0]=0;

	while(f[xf][yf]<0) {
		p=Q.front();
		Q.pop();
		int w=f[p.first][p.second]+1;

		for(int i=0;i<4;i++) {
			int x=p.first+dx[i],y=p.second+dy[i];
			if(x<0 || x>=m || y<0 || y>=n || g[x][y]=='.' || f[x][y]>=0) continue;

			Q.push(PII(x,y));
			f[x][y]=w;

			prev[x][y]=p;
		}
	}

	p=PII(xf,yf);
	int w=f[p.first][p.second],w2=0;

	memset(flag,0,sizeof(flag));
	while(1) {
		flag[p.first][p.second]=1;
		f[p.first][p.second]=w<?w2;
//		printf("%d %d\n",p.first,p.second);

		if(p.first==0 && p.second==0) break;


		p=prev[p.first][p.second];

		ans+=w;
		w--;
		w2++;
	}
}

void solve()
{
	scanf("%d%d",&m,&n);
	xf=yf=-1;
	for(int i=0;i<m;i++) {
		scanf("%s",g[i]);
		for(int j=0;j<n;j++) if(g[i][j]=='T') xf=i,yf=j;
	}

	ans=0;
	memset(f,-1,sizeof(f));
	memset(flag,0,sizeof(flag));
        if(!(xf==0 && yf==0)) findPath();

	flag[0][0]=1;
	f[0][0]=f[xf][yf]=0;

	while(1) {
		int c=0;

		int pi,pj,w=INF;
		pi=pj=-1;
		for(int i=0;i<m;i++)
			for(int j=0;j<n;j++) if(!flag[i][j] && g[i][j]!='.') {
				c++;

				for(int d=0;d<4;d++) {
					int x=i+dx[d],y=j+dy[d];
					if(x<0 || x>=m || y<0 || y>=n || f[x][y]<0) continue;
					if(f[x][y]<w) w=f[x][y],pi=i,pj=j;
				}
			}
		if(c==0) break;

		w++;
		ans+=w;
		flag[pi][pj]=1;
		f[pi][pj]=w;

//		printf("%d %d %d\n",pi,pj,w);
	}

	printf("%d",ans);
}

int main()
{	
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++) {
		printf("Case #%d: ",t);
		solve();
		printf("\n");
	}


	return 0;
}
