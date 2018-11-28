#include<cstdio>
#include<queue>
#include<iostream>
#include<vector>
using namespace std;
typedef vector<int> VI;
typedef pair<int,int> PII;
const int MAXN = 23;
const int MAXQ = 520;
//const int MAXQ = 90;
#define REP(i,n) for(int i=0;i<(n);i++)
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
const bool dbg = 0;

string dis[MAXN][MAXN][MAXQ];
string best[MAXQ];
char square[MAXN][MAXN];
char s[MAXQ];
int w,q;
VI queries;
int dx[] = {1,0,-1,0};
int dy[] = {0,1,0,-1};

inline int good(int x,int y){
	return (x>=0 && x<w && y>=0 && y<w);
}

void init(){
	REP(i,w)
		REP(j,w)
			REP(k,MAXQ)
			dis[i][j][k] = "";
	queries.clear();
	REP(k,MAXQ)
		best[k] = "";
}

void read(){
	scanf("%d%d",&w,&q);
	init();
	REP(i,w){
		scanf("%s",s);
		if(dbg)printf("s:%s\n",s);
		REP(j,w)
			square[i][j] = s[j];
	}
	REP(i,q){
		int qq;
		scanf("%d",&qq);
		queries.PB(qq);
	}
	if(dbg)printf("READ:OK\n");
}
inline bool relax(string &s,string &p){
	if(p=="")return false;
	return (s == "" || s.length() > p.length() || (s.length() == p.length() && s > p));
}

void bfs(){
	queue<pair<PII,int> > que;
	REP(i,w)REP(j,w){
		if( square[i][j] >= '0'){
			dis[i][j][MAXQ/2 + square[i][j]-'0'] = string(1,square[i][j]);
			que.push(MP(MP(i,j),square[i][j] - '0'));
		}
	}
	if(dbg)printf("BFS:INIT\n");
	while(!que.empty()){
		PII p = que.front().ST;
		int d = que.front().ND;
		que.pop();
		if(dbg)printf("BFS: p:[%d,%d] d:%d[%s]\n",p.ST,p.ND,d,dis[p.ST][p.ND][MAXQ/2 + d].c_str());
		REP(i,4){
			int x = p.ST + dx[i];
			int y = p.ND +dy[i];
			if(!good(x,y))continue;
			int nD = d;
			string dS = dis[p.ST][p.ND][MAXQ/2 + d];
			dS.append(1,square[x][y]);
			if(dS[dS.size()-2] == '-') nD -= square[x][y] - '0';
			if(dS[dS.size()-2] == '+') nD += square[x][y] - '0';
			if(nD>=MAXQ/2 || nD<=-MAXQ/2)continue;
			if(relax(dis[x][y][MAXQ/2 + nD],dS)){
				dis[x][y][MAXQ/2 + nD] = dS;
				que.push(MP(MP(x,y),nD));
			}
		}
	}
}
void compute(int cas){
	bfs();
	REP(i,w)REP(j,w)REP(k,MAXQ){
		if(dbg)printf("dis[%d][%d][%d]:%s (best:%s)\n",i,j,k-MAXQ/2,dis[i][j][k].c_str(),best[k].c_str());
		if((square[i][j] >= '0') && relax(best[k],dis[i][j][k]))
			best[k] = dis[i][j][k];
	}
	printf("Case #%d:\n",cas+1);
	REP(i,q){
		printf("%s\n",best[queries[i]+MAXQ/2].c_str());
	}
}

int main(){
	int t;
	scanf("%d",&t);
	REP(i,t){
		read();
		compute(i);
	}
	return 0;
}
