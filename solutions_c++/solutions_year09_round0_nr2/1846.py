#include "stdio.h"
#include "algorithm"
#include "queue"
#include "iostream"
using namespace std;

struct Q{
	char ch;
	int x,y;
};
struct H{
	int x,y;
	int num;
	friend bool operator < (H a,H b) {
		return a.num > b.num;
	}
};
priority_queue <H> qq;
queue <Q> q;
int maze[101][101];
bool dire[101][101][4];
char ans[101][101];
int dir[][2] = {{-1,0},{0,-1},{0,1},{1,0}};
int n , m ;
bool yes(Q a,Q b) {
	if(b.x < 0 || b.y < 0 || b.x >= n || b.y >= m || ans[b.x][b.y] != 0) {
		return false;
	}
	int best = -1;
	int minnum = 0x7fffffff;
	for(int i = 0 ; i < 4; i ++) {
		Q next;
		next.x = b.x + dir[i][0];
		next.y = b.y + dir[i][1];
		if(next.x < 0 || next.y < 0 || next.x >= n || next.y >=m || maze[next.x][next.y] >= maze[b.x][b.y]) {
			continue;
		}
		if(minnum > maze[next.x][next.y]) {
			minnum = maze[next.x][next.y];
			best = i;
		}
	}
	if(best != -1 && b.x + dir[best][0] == a.x && b.y + dir[best][1] == a.y) {
		return true;
	}
	return false;
}
void bfs() {
	while(!q.empty()) {
		Q now = q.front();
		q.pop();
		for(int i = 0 ; i < 4; i ++) {
			Q next;
			next.x = now.x + dir[i][0];
			next.y = now.y + dir[i][1];
			next.ch = now.ch;
			if(yes(now,next)) {
				ans[next.x][next.y] = next.ch;
				q.push(next);
			}
		}
	}
}
void BFS(char ch) {
	while(!q.empty()) {
		Q now = q.front();
		q.pop();
		for(int i = 0 ; i < 4; i ++) {
			Q next;
			next.x = now.x + dir[i][0];
			next.y = now.y + dir[i][1];
			next.ch = now.ch;
			if(next.x >= 0 && next.y >= 0 && next.x < n && next.y < m && ans[next.x][next.y] == ch) {
				ans[next.x][next.y] = next.ch;
				q.push(next);
			}
		}
	}
}
int main() {
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int T;
	cin >> T;
	for(int cas = 1; cas <= T ; cas ++) {
		cin >> n >> m;
		for(int i = 0 ; i < n ; i ++) {
			for(int j = 0 ; j < m ; j ++) {
				cin >> maze[i][j];
				H buf;
				buf.x = i;
				buf.y = j;
				buf.num = maze[i][j];
				qq.push(buf);
			}
		}
		memset(ans,0,sizeof(ans));
		int cnt = 0;
		while(!qq.empty()) {
			H now = qq.top();
			qq.pop();
			int i = now.x;
			int j = now.y;
			if(ans[i][j] == 0) {
				Q buf;
				buf.ch = 'A' + cnt;
				buf.x = i;
				buf.y = j;
				cnt ++;
				ans[i][j] = buf.ch;
				q.push(buf);
				bfs();
			}
		}
		cnt = 0;
		for(int i = 0 ; i < n ; i ++) {
			for(int j = 0 ; j < m ; j ++) {
				if(isupper(ans[i][j])) {
					Q buf;
					buf.ch = 'a' + cnt;
					buf.x = i;
					buf.y = j;
					q.push(buf);
					char ch = ans[i][j];
					ans[i][j] = buf.ch;
					BFS(ch);
					cnt ++;
				}
			}
		}
		cout << "Case #" << cas << ":" << endl;
		for(int i = 0 ; i < n ; i ++) {
			cout << ans[i][0];
			for(int j = 1; j < m ; j ++) {
				cout << " " << ans[i][j];
			}
			cout << endl;
		}
	}
	return 0;
}