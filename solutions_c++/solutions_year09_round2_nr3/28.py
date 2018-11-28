#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <cstring>
#include <set>
#include <map>
#include <bitset>
#include <cmath>
#include <algorithm>
#include <sstream>
using namespace std;
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define FORD(i,a,b) for (int i=(a); i>=(b); --i)
#define FORE(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define debug(x) cerr << #x << " = " << x << "\n";
#define debugv(x) cerr << #x << " = "; FORE(it,(x)) cerr<< *it <<","; cerr<<"\n";
#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset(x,0,sizeof x)
#define xx first
#define yy second
typedef long long int lli;
typedef pair<int, char> P;
typedef vector<int> vi;
#define MAXN 57
#define STALA 500
#define ZAK 1257
#define INF 999999

int dx[]={1,-1,0,0};
int dy[]={0,0,1,-1};

int T,W,Q;

char c[MAXN][MAXN];
int que[MAXN];

int dp[23][23][ZAK];
bool ok,pier;
int jest[23][23],nowe[23][23];

bool znak(int x,int y){
	return c[x][y] == '+' || c[x][y] == '-';
}

P war(int x,int y,int w){return P(dp[x][y][w],c[x][y]);}
bool kon;

int main(){
	cin >> T;
	FOR(cas,1,T){
		//in
		cin >> W >> Q;
		REP(i,W) scanf("%s",c[i]);
		REP(i,Q) cin >> que[i];
		//rozw
		REP(i,W) REP(j,W) REP(w,ZAK) dp[i][j][w]=INF;
		REP(i,W) REP(j,W) dp[i][j][STALA]=0;
		do{
			ok=false;
			REP(x,W) REP(y,W) REP(w,ZAK) if(dp[x][y][w] != INF)
				REP(k,4){
					int nx=x+dx[k];
					int ny=y+dy[k];
					if(nx<0 || ny<0 || nx>=W || ny>=W) continue;
					int nw= znak(nx,ny) ? w+(c[nx][ny] == '+'?1:-1)*(int)(c[x][y]-'0'): w;
					if(nw<0 || nw>=ZAK) continue;
					int& old=dp[nx][ny][nw];
					if(dp[x][y][w]+1<old){
						old=dp[x][y][w]+1;
						ok=true;
					}
				}
		}while(ok);
		//out
		cout << "Case #" << cas << ": " << endl;
		REP(q,Q){
			int zap=que[q]+STALA;
			REP(i,W) REP(j,W) jest[i][j]= znak(i,j) ? 0 : zap-(c[i][j]-'0');
		kon=false;
		string res="";
			while(true){
				P naj=P(INF,'9');
				REP(i,W) REP(j,W) if(jest[i][j]) naj=min(naj,war(i,j,jest[i][j]));
				if(naj.xx == INF) {cout << "error"; return 0;}
				//cout << naj.xx; break;
				res+=naj.yy;
				if(kon) break;
//				cout << "n" << naj.xx << "/" << naj.yy << endl;
				P dru=P(INF,'9');
//				cout << dru.xx << "/" << dru.yy << "!" << " " << INF << endl;
				REP(x,W) REP(y,W) if(jest[x][y] && naj==war(x,y,jest[x][y])){
					REP(k,4){
						int nx=x+dx[k];
						int ny=y+dy[k];
						if(nx<0 || ny<0 || nx>=W || ny>=W) continue;
						int nw= znak(x,y) ? (c[x][y] == '+'?1:-1)*(int)(c[nx][ny]-'0'): 0;
						int nzap=jest[x][y]-nw;
						if(nzap<0 || nzap>=ZAK) continue;
//cout << "OK" << c[nx][ny] << " " << nzap-STALA << "   " << jest[x][y]-STALA << " war " << war(nx,ny,nzap).xx << endl;
						dru=min(dru,war(nx,ny,nzap));
					}
				}
//				cout << dru.xx << "/" << dru.yy << endl;
				if(dru.xx == INF) {cout << "error2"; return 0;}
				CLR(nowe);
				kon=false;
				REP(x,W) REP(y,W) if(jest[x][y] && naj==war(x,y,jest[x][y])){
					REP(k,4){
						int nx=x+dx[k];
						int ny=y+dy[k];
						if(nx<0 || ny<0 || nx>=W || ny>=W) continue;
						int nw= znak(x,y) ? (c[x][y] == '+'?1:-1)*(int)(c[nx][ny]-'0'): 0;
						int nzap=jest[x][y]-nw;
						if(nzap<0 || nzap>=ZAK) continue;
						if(dru==war(nx,ny,nzap)) {
							nowe[nx][ny]=nzap;
							if(nzap==STALA) kon=true;
					//		cout << "nzap " << nzap << endl;
//				cout << "nowe " << nx << " " << ny << " " << c[nx][ny] << " " << zap-STALA << endl;
						}
					}
				}
				REP(i,W) REP(j,W) jest[i][j]=nowe[i][j];
			}
			if(res[res.size()-1] == '+') res=res.substr(0,res.size()-1);
			if(res[res.size()-1] == '-') res=res.substr(0,res.size()-1);
			cout << res << endl;
		}
	}
	return 0;
}
