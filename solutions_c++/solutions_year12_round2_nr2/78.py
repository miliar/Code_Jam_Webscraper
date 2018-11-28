#include <vector>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <list>
#include <ctime>
#include <string>
#include <cassert>

using namespace std;

//----------------------zjut_DD for Topcoder-------------------------------
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
#define PB push_back
#define MP make_pair
#define ff first
#define ss second
#define two(w) (1<<(w))
#define test(x,w) (x&two(w))
#define sz(v) (int)v.size()
#define all(c) c.begin(),c.end() 
#define clr(buf,val) memset(buf,val,sizeof(buf))
#define rep(i,l,r) for(int i=(l);i<(r);i++)
#define repv(i,v)  for(int i=0;i<(int)v.size();i++)
#define repi(it,c) for(typeof(c.begin()) it=c.begin();it!=c.end();++it)
//------------------------------------------------------------------------

const double eps=1e-8;

int sgn(double a){
	return a>eps?1:(a<-eps?-1:0);
}

int hi[110][110];
int lo[110][110];
double dp[110][110];


struct DD{
	int r, c;
	double time;
	DD(int _r=0, int _c=0, double _t=0):r(_r), c(_c),time(_t){};
	bool operator<(const DD &b)const{
		return time > b.time;
	}
};
priority_queue<DD> pq;

int dir[4][2]={0,1, 1,0, 0,-1, -1,0};
int H, N, M;
bool canGo(int r, int c, int tr, int tc, double time){
	double h=H-10*time;
	if( h+50 > hi[tr][tc] ) return false;
	if( lo[r][c]+50 > hi[tr][tc] ) return false;
	if( lo[tr][tc]+50 > hi[tr][tc] ) return false;
	if( lo[tr][tc]+50 > hi[r][c] ) return false;
	return true;
}

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T; cin>>T;
	rep(Te, 1, T+1){
		
		cin>>H>>N>>M;
		rep(i, 0, N) rep(j, 0, M) cin>>hi[i][j];
		rep(i, 0, N) rep(j, 0, M) cin>>lo[i][j];
		queue<int> q;
		rep(i, 0, N) rep(j, 0, M) dp[i][j]=1e50;
		q.push(0); q.push(0); dp[0][0]=0; pq.push(DD(0, 0, 0));
		while( !q.empty() ){
			int r=q.front(); q.pop();
			int c=q.front(); q.pop();
			rep(in, 0, 4){
				int tr=r+dir[in][0];
				int tc=c+dir[in][1];
				if( tr<0 || tr>=N || tc<0 || tc>=M ) continue;
				if( sgn(dp[tr][tc]==0 )  )continue;
				if( canGo(r, c, tr, tc, 0) ) {
					q.push(tr); q.push(tc); dp[tr][tc]=0; pq.push(DD(tr, tc, 0));
				}
			}
		}
		
		while( !pq.empty() ){
			DD cur=pq.top(); pq.pop();
			int r=cur.r, c=cur.c;
			double time=cur.time;
			if( sgn(time-dp[r][c]) >0 ) continue;
			rep(in, 0, 4){
				int tr=r+dir[in][0];
				int tc=c+dir[in][1];
				double add=0, h=H-time*10;
				if( tr<0 || tr>=N || tc<0 || tc>=M ) continue;
				if( lo[r][c]+50 > hi[tr][tc] ) continue; //
				if( lo[tr][tc]+50 > hi[tr][tc] ) continue; //
				if( lo[tr][tc]+50 > hi[r][c] ) continue; //
				if( hi[tr][tc]-h < 50 ){
					add=(50-(hi[tr][tc]-h))/10.0;
					h-=add*10.0;
				}
				if( sgn(h-20-lo[r][c])>=0 ) add+=1.0;
				else add+=10.0;
				
				if( sgn(dp[tr][tc]-(dp[r][c]+add))>0 ){
					dp[tr][tc]=dp[r][c]+add;
					pq.push(DD(tr, tc, dp[tr][tc]) );
				}
			}
		}
		printf("Case #%d: %.10lf\n", Te, dp[N-1][M-1]);
	}
}










