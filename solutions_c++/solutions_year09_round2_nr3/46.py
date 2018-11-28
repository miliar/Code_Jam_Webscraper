#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
template <class T> inline string itos(T n) {return (n)<0?"-"+itos(-(n)):(n)<10?(string)("")+(char)('0'+(n)):itos((n)/10)+itos((n)%10);}
#define gcj_print(ans) {cout << "Case #" << ((test)+1) << ":" << (ans) << endl;}

#define INF (1<<29)
#define mp(x,y,s) (make_pair(make_pair((x),(y)),(s)))
#define inside(x,y) ((x)>=0&&(x)<(W)&&(y)>=0&&(y)<(W))

int W;
int dx[]={1,-1,0,0},dy[]={0,0,1,-1};
char board[25][25];
int dist[25][25][2010];
bool can[25][25],can2[25][25];

void bfs(void){
	int i,j,s;
	
	REP(i,W) REP(j,W) REP(s,2010) dist[i][j][s] = INF;
	
	queue <pair <pair <int, int>, int> > q;
	REP(i,W) REP(j,W) if(board[i][j] >= '0' && board[i][j] <= '9'){
		dist[i][j][1000] = 0;
		q.push(mp(i,j,1000));
	}
	
	while(!q.empty()){
		int x=q.front().first.first,y=q.front().first.second; s=q.front().second; q.pop();
		REP(i,4){
			int x2=x+dx[i],y2=y+dy[i];
			if(inside(x2,y2)) REP(j,4){
				int x3=x2+dx[j],y3=y2+dy[j];
				if(inside(x3,y3)){
					int s2 = ((board[x2][y2] == '+') ? (s + (board[x][y] - '0')) : (s - (board[x][y] - '0')));
					if(s2 < 0 || s2 > 2000 || dist[x3][y3][s2] != INF) continue;
					dist[x3][y3][s2] = dist[x][y][s] + 1;
					q.push(mp(x3,y3,s2));
				}
			}
		}
	}
}

string query(int Q){
	int D=INF,i,j,d,c,x,y;
	
	REP(i,W) REP(j,W) if(board[i][j] >= '0' && board[i][j] <= '9'){
		int tmp = Q - (board[i][j] - '0');
		D = min(D,dist[i][j][tmp+1000]);
	}
	
//	cout << D << endl;
	
	string ans;
	
	int start = INF;
	REP(i,W) REP(j,W) if(board[i][j] >= '0' && board[i][j] <= '9'){;
		int tmp = Q - (board[i][j] - '0');
		if(dist[i][j][tmp+1000] == D){
		//	cout << i << ' ' << j << endl;
			start = min(start,(int)(board[i][j]-'0'));
		}
	}
	ans += (char)('0' + start);
	
	REP(i,W) REP(j,W){
		can[i][j] = false;
		if(board[i][j] == '0' + start && dist[i][j][Q-start+1000] == D) can[i][j] = true;
	}
	
//	cout << ans << endl;
	
	Q -= start;
	for(d=D-1;d>=0;d--){
		for(int _oper=0;_oper<2;_oper++) REP(c,10){
			char oper = ((_oper == 0) ? '+' : '-');
			int tmp = ((oper == '+') ? (Q - c) : (Q + c));
			if(tmp < -1000 || tmp > 1000) continue;
			bool flag = false;
			
			REP(x,W) REP(y,W) can2[x][y] = false;
			REP(x,W) REP(y,W) if(can[x][y]) REP(i,4){
				int x2=x+dx[i],y2=y+dy[i];
				if(inside(x2,y2) && board[x2][y2] == oper) REP(j,4){
					int x3=x2+dx[j],y3=y2+dy[j];
					if(inside(x3,y3) && board[x3][y3] == '0' + c && dist[x3][y3][tmp+1000] == d){
						flag = true;
						can2[x3][y3] = true;
					}
				}
			}
			
			if(flag){
				Q = tmp;
				ans += oper; ans += (char)('0' + c);
				REP(x,W) REP(y,W) can[x][y] = can2[x][y];
				goto found;
			}
		}
		found:;
	}
	
	return ans;
}

int main(void){
	int T,Q,i,j,test;
	
	cin >> T;
	REP(test,T){
		cin >> W >> Q;
		REP(i,W) REP(j,W) cin >> board[i][j];
		bfs();
		gcj_print("");
		REP(i,Q){
			int q; cin >> q;
			string ans = query(q);
			cout << ans << endl;
		}
	}
	
	return 0;
}
