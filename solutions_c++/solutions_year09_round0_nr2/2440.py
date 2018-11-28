#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <map>
#include <sstream>
#include <fstream>
#include <utility>
#include <string>
#include <vector>
#include <stack>
#include <queue>
using namespace std;
#define REP(i,a) for(int i=0;i<a;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define SIZE(c) (int)c.size()
#define ALL(c) (c).begin(),(c).end() 
typedef pair<int, int> PII;
const int INF = 1000000000;
ifstream fin("B-small-attempt1.in");
ofstream fout("B-small.out");
int board[100][100];
char ret[100][100];
PII go[100][100];
bool vis[100][100];
int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};
int tc,r,c;
char ch;
vector<PII> v;
bool valid(int x,int y){
	return x>=0&&y>=0&&x<r&&y<c;
}
bool contains(vector<char> v, char c){
	REP(i,SIZE(v))if(v[i]==c)return true;
	return false;
}
PII get(int x,int y){
	int best = board[x][y];
	PII ret = PII(-1,-1);
	REP(i,4){
		int nx = x+dx[i], ny = y+dy[i];
		if(valid(nx,ny)){
			if(best > board[nx][ny]){
				best = board[nx][ny];
				ret = PII(nx,ny);
			}
		}
	}
	return ret;
}
void solve(){
	memset(vis,false,sizeof(vis));
	v.clear();
	REP(i,r)REP(j,c)ret[i][j]='0';
	ch='A';
	REP(i,r){
		REP(j,c){
			go[i][j]=get(i,j);
			if(go[i][j].first==-1)v.push_back(PII(i,j));
		}
	}
	REP(i,SIZE(v)){
		queue<PII> q;
		q.push(v[i]);
		while(!q.empty()){
			PII where = q.front();q.pop();
			ret[where.first][where.second] = ch;
			if(go[where.first][where.second].first != -1 && !vis[go[where.first][where.second].first][go[where.first][where.second].second]){
				q.push(PII(go[where.first][where.second].first,go[where.first][where.second].second));
				vis[go[where.first][where.second].first][go[where.first][where.second].second] = true;
			}
			REP(k,4){
				int nx = where.first + dx[k];
				int ny = where.second + dy[k];
				if(go[nx][ny] == where && !vis[nx][ny]){
					vis[nx][ny] = true;
					q.push(PII(nx,ny));
				}
			}
		}
		ch++;
	}

	vector<char> let;
	REP(i,r){
		REP(j,c){
			if(!contains(let,ret[i][j])){
				let.push_back(ret[i][j]);
			}
		}
	}
	int sz = SIZE(let);
	REP(k,sz){
		REP(i,r){
			REP(j,c){
				if(ret[i][j]==let[k]){
					ret[i][j] = 'a'+k;
				}
			}
		}
	}
}
void read(){
	fin>>r>>c;
	REP(i,r){
		REP(j,c){
			fin>>board[i][j];
		}
	}
}
int main() {
    fin>>tc;
	REP(i,tc){
		read();
		solve();
		fout<<"Case #"<<(i+1)<<":"<<endl;
		REP(j,r){
			REP(k,c){
				fout<<ret[j][k]<<" ";
			}
			fout<<endl;
		}
	}
    return 0;
}
