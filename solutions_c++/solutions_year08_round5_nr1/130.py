#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include <cstring> 
#include <cstdlib> 
#include <cstdio> 
#include <vector> 
#include <string> 
#include <cmath> 
#include <queue> 
#include <map> 
#include <set> 

using namespace std; 

typedef vector<int> VI; 
typedef vector<string> VS; 
typedef long long ll; 

#define sz size() 
#define pb push_back 
#define MAX 0xFFFFFFF 
#define all(x) (x).begin(),(x).end() 
#define For(i,n) for(int i=0, _n=(n);i<_n;++i) 
#define For2(i,a,b) for(int i=(a), _n=(b);i<_n;++i) 
#define Forit(it,x) for(typeof((x).begin()) it=(x).begin(), ed=(x).end();it!=ed;++it) 

char a[6010][6010];
int b[100000][4];
char c[6010][6010];
int di[4][2] = {{-1,0},{0,1},{1,0},{0,-1}};

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int ti = 0, tn;
	scanf("%d",&tn);
	while(tn--)
	{
		int n;
		int x = 0, y = 0, d = 0;
		int maxx = 0, maxy = 0, minx = 0, miny = 0;
		int nn = 0, st = 0;
		scanf("%d",&n);
		For(i,n) 
		{
			int t;
			char p[64];
			scanf("%s %d",p,&t);
			int l = strlen(p);
			For(j,t) For(k,l)
			{
				if(p[k] == 'F') 
				{
					if(!st) {b[nn][0] = x; b[nn][1] = y; st = 1;}
					x += di[d][0]; 
					y += di[d][1];
				}
				if(p[k] == 'R') 
				{
					if(st) {b[nn][2] = x; b[nn++][3] = y; st = 0;}
					d = (d+1) % 4;
				}
				if(p[k] == 'L') 
				{
					if(st) {b[nn][2] = x; b[nn++][3] = y; st = 0;}
					d = (d+3) % 4;
				}
				if(maxx < x) maxx = x;
				if(maxy < y) maxy = y;
				if(minx > x) minx = x;
				if(miny > y) miny = y;
			}
		}
		if(st) {b[nn][2] = x; b[nn++][3] = y;}
		x = -minx + 3;
		y = -miny + 3;
		memset(a, 0, sizeof(a));
		memset(c, 0, sizeof(c));
		For(i,nn) 
		{
			b[i][0] -= minx - 2;
			b[i][1] -= miny - 2;
			b[i][2] -= minx - 2;
			b[i][3] -= miny - 2;
			if(b[i][0] > b[i][2]) swap(b[i][0], b[i][2]);
			if(b[i][1] > b[i][3]) swap(b[i][1], b[i][3]);
		}
		if(maxx-minx > 6000) printf("!");
		if(maxy-minx > 6000) printf("!");
		maxx -= minx - 4;
		maxy -= miny - 4;
		For(i,nn) 
			if(b[i][0] == b[i][2]) For2(j,b[i][1],b[i][3]) {a[b[i][0]-1][j]|=4; a[b[i][0]][j]|=1;}
			else For2(j,b[i][0],b[i][2]) {a[j][b[i][1]-1]|=2; a[j][b[i][1]]|=8;}
		queue<pair<int,int> > q;
		q.push(make_pair(0,0));
		c[0][0] = 1;
		while(!q.empty())
		{
			pair<int,int> p = q.front(); q.pop();
			int x = p.first, y = p.second;
			if(x+1<=maxx && !c[x+1][y] && !(a[x][y]&4)) 
				{q.push(make_pair(x+1,y)); c[x+1][y]=1;}
			if(y+1<=maxy && !c[x][y+1] && !(a[x][y]&2)) 
				{q.push(make_pair(x,y+1)); c[x][y+1]=1;}
			if(x && !c[x-1][y] && !(a[x][y]&1)) 
				{q.push(make_pair(x-1,y)); c[x-1][y]=1;}
			if(y && !c[x][y-1] && !(a[x][y]&8)) 
				{q.push(make_pair(x,y-1)); c[x][y-1]=1;}
		}
		int ans = 0;
		For(i,maxx) 
		{
			int st = 0;
			For(j,maxy) if(!c[i][j]) {st = j; break;}
			For2(j,st,maxy) if(c[i][j])
			{
				int k = j;
				for(; k < maxy; k++) if(!c[i][k]) break;
				if(k < maxy) for(k = j; k < maxy; k++) if(!c[i][k]) break; else {c[i][k] = 2; ans++;}
				j = k;
			}
		}
		For(i,maxy) 
		{
			int st = 0;
			For(j,maxx) if(!c[j][i]) {st = j; break;}
			For2(j,st,maxx) if(c[j][i])
			{
				int k = j;
				for(; k < maxx; k++) if(!c[k][i]) break;
				if(k < maxx) for(k = j; k < maxx; k++) if(!c[k][i]) break; else if(c[k][i] == 1) ans++;
				j = k;
			}
		}
		printf("Case #%d: %d\n",++ti,ans);
	}
}

/*
2
1
FFFR 4
9
F 6 R 1 F 4 RFF 2 LFF 1
LFFFR 1 F 2 R 1 F 5
*/ 