#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <sstream>
#include <algorithm>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <cmath>

using namespace std;

#define RP(i,j,k) for(int i=j; i<k; ++i)
#define R(i,x) RP(i,0,(x).size())
#define RP3(x,y,z) RP(i,0,x) RP(j,0,y) RP(k,0,z)
#define RI(i,x) for(typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define pB push_back
#define P(a) cout << #a << " : " << a << endl;
#define M make_pair

template <class T, class R>
ostream & operator<<(ostream & o, pair<T,R> a){return o<<a.first<<"," << a.second;}

template <class T>
ostream & operator<<(ostream & o, vector<T> a){R(i,a) o<<a[i]<<","; return o;}

typedef vector<string> vs;
typedef vector<int> vi;
typedef long long ll;

int m[110][110];
int t[110][110][4];
char p[110][110];
char p2[110][110];
int H, W;
int dx[]={0,-1,1,0,0},dy[]={-1,0,0,1,0},v[]={3,2,1,0};
#define ib(x,y) ((x)>=0 && (y)>=0 && (y)<H && (x)<W)

void go(int x, int y, char c)
{
	if(!ib(x,y) || p[y][x]) return;
	p[y][x]=c;
	RP(i,0,4) if(t[y][x][i]) go(x+dx[i],y+dy[i],c);
}

bool go2(int x, int y, char c, char f)
{
	if(!ib(x,y) || p[y][x]!=c || p2[y][x]) return 0;
	p2[y][x]=f;
	RP(i,0,4) go2(x+dx[i],y+dy[i],c,f);
	return 1;
}

int main()
{
	int C;
	cin >> C;
	for(int cs=1; cs<=C; ++cs)
	{
		
		cin >> H >> W;
		
		RP(i,0,H) RP(j,0,W) cin >> m[i][j];
		memset(t,0,sizeof(t));
		vector<pair<int,int> > l;
		
		RP(i,0,H) RP(j,0,W)
		{
			int r=4;
			RP(k,0,4)
			if(ib(j+dx[k],i+dy[k]) && m[i+dy[k]][j+dx[k]]<m[i+dy[r]][j+dx[r]]) r=k;
			if(r<4) t[i+dy[r]][j+dx[r]][v[r]]=1;
			else l.pB(M(j,i));
		}
		
		memset(p,0,sizeof(p));
		memset(p2,0,sizeof(p2));
		
		R(i,l)
		{
			//sP(l[i]);
			go(l[i].first,l[i].second,i+'a');
		}
		int u=0;
		RP(i,0,H) RP(j,0,W) if(go2(j,i,p[i][j],u+'a')) ++u;
		
		cout << "Case #" << cs << ": " << endl;
		RP(i,0,H){RP(j,0,W-1) cout << p2[i][j] << " "; cout << p2[i][W-1] << endl;}
		//cout << endl;
	}
	
	return 0;
}