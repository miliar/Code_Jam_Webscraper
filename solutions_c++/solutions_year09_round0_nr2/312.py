#include <cstdio>
#include <vector>
#include <iostream>
#include <map>

#define REP(i,n) for(int i=0; i<(n); ++i)
#define pi pair<int,int>
#define mp make_pair

using namespace std;

struct Node
{
	int alt;
	int label;
	pi parent;
};

Node nodes[110][110];
int dx[4] = {0, -1, 1, 0};
int dy[4] = {-1, 0, 0, 1};

pi get_parent(pi cur)
{
	pi &par = nodes[cur.first][cur.second].parent;
	if(par == cur) return par;
	return (par = get_parent(par));
}

void process(int kase)
{
	int w,h;
	scanf("%d %d",&h,&w);
	REP(i,h) {
		REP(j,w) {
			scanf("%d", &nodes[j][i].alt);
			nodes[j][i].label = -1;
			nodes[j][i].parent = mp(j,i);
		}
	}

	// recognize parent
	REP(i,h) {
		REP(j,w) {
			int min_alt = nodes[j][i].alt;
			REP(k,4) {
				int nx = j+dx[k];
				int ny = i+dy[k];
				if(nx < 0 || ny < 0 || nx >= w || ny >= h) continue;
				if(min_alt > nodes[nx][ny].alt) {
					min_alt = nodes[nx][ny].alt;
					nodes[j][i].parent = mp(nx,ny);
				}
			}
			pi parent = nodes[j][i].parent;
//			cout << "(" << parent.first << "," << parent.second << ")";
		}
//		cout << endl;
	}

	cout << "Case #" << kase << ":" << endl;
	
	// set label
	int last_label = -1;
	REP(i,h) {
		REP(j,w) {
			pi parent = get_parent(mp(j,i));
//			cout << "(" << parent.first << "," << parent.second << ")";
			if(nodes[parent.first][parent.second].label == -1) {
				nodes[parent.first][parent.second].label = ++last_label;
			}
			nodes[j][i].label = nodes[parent.first][parent.second].label;
			cout << (char)(nodes[j][i].label+'a') << " ";
		}
		cout << endl;
	}
}

int main()
{
	int t;
	scanf("%d",&t);
	REP(i,t) process(i+1);
	return 0;
}
