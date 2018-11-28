#include <cstdio>
#include <map>

using namespace std;

const int maxn = 10010;

typedef pair<int, int> cord;

#define mp make_pair
#define f first
#define s second

int cornerx[6]={1,0,-1,-1,0,1}, cornery[6]={1,1,0,-1,-1,0};

map<cord, int> board;
int p[maxn];
int s, n;

int findrep(int a) {
	if (p[a] == a) {
		return a;
	}
	return p[a] = findrep(p[a]);
}

class Tset {
public:
	bool flag[12];
	void clear() {
		for (int i=0; i<12; i++) {
			flag[i] = false;
		}
	}
	void merge(const Tset &s) {
		for (int i=0; i<12; i++) {
			flag[i] |= s.flag[i];
		}
	}
	void attrib(int x, int y) {
		/*
		1 in x is bot right	- 0
		1 in y is bot left	- 1
		x+s-1 = y is right	- 2
		y+s-1 = x is left	- 3
		2*s-1 = x is top left	- 4
		2*s-1 = y is top right	- 5
		corner top		- 6
		corner topleft		- 7
		corner top right	- 8
		corner botleft		- 9
		corner botright		- 10
		corner bot		- 11
		*/
		if (x==1 && y==1) flag[11] = true;
		else if (x==1 && x+s-1 == y) flag[10] = true;
		else if (x+s-1 == y && 2*s-1 == y) flag[8] = true;
		else if (2*s-1==y && 2*s-1==x) flag[6] = true;
		else if (2*s-1 == x && y+s-1 == x) flag[7] = true;
		else if (y+s-1 == x && y==1) flag[9] = true;
		else if (x==1) flag[0] = true;
		else if (y==1) flag[1] = true;
		else if (x+s-1 == y) flag[2] = true;
		else if (y+s-1 == x) flag[3] = true;
		else if (2*s-1 == x) flag[4] = true;
		else if (2*s-1 == y) flag[5] = true;
		else {
			//printf("Error\n");
		}
	}
}set[maxn];

void merge(int a, int b) {
	set[findrep(a)].merge(set[findrep(b)]);
	p[findrep(b)] = findrep(a);
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int ti=0; ti<t; ti++) {
		printf("Case #%d: ", ti+1);
		scanf("%d%d", &s, &n);
		board.clear();
		for (int i=0; i<n; i++) {
			p[i] = i;
			set[i].clear();
		}
		bool found = false;
		for (int i=0; i<n; i++) {
			int x, y;
			scanf("%d%d", &x, &y);
			board[mp(x, y)] = i;
			set[i].attrib(x, y);
			int corner[6];
			for (int j=0; j<6; j++) {
				corner[j] = board.count(mp(x+cornerx[j], y+cornery[j]));
				if (corner[j]) {
					corner[j] = board[mp(x+cornerx[j], y+cornery[j])];
					corner[j] = findrep(corner[j]);
				}
				else {
					corner[j] = -1;
				}
			}
			for (int j=0; j<6; j++) {
				if (corner[j] != -1) {
					merge(i, corner[j]);
				}
			}
			bool loop = false, bridge=false, fork=false;
			for (int a=0; a<6; a++) {
				for (int b=a+1; b<6; b++) {
					bool l=false, r=false;
					if (corner[a] == corner[b] && corner[a] != -1) {
						for (int c=(a+1)%6; c!= b; c=(c+1)%6) {
							if (corner[c] == -1) {
								l = true;
							}
						}
						for (int c=(b+1)%6; c!= a; c=(c+1)%6) {
							if (corner[c] == -1) {
								r = true;
							}
						}
					}
					if (l && r) {
						loop = true;
					}
				}
			}
			int e = 0, c = 0;
			for (int j=0; j<6; j++) {
				if (set[i].flag[j]) {
					e++;
				}
			}
			for (int j=6; j<12; j++) {
				if (set[i].flag[j]) {
					c++;
				}
			}
			if (c>1) {
				bridge = true;
			}
			if (e>2) {
				fork = true;
			}
			if (loop || bridge || fork) {
				found = true;
				if (loop && bridge && fork) printf("bridge-fork-ring");
				else if (loop && bridge) printf("bridge-ring");
				else if	(loop && fork) printf("fork-ring");
				else if (fork && bridge) printf("bridge-fork");
				else if (bridge) printf("bridge");
				else if (fork) printf("fork");
				else if (loop) printf("ring");
				else {
					printf("ERROR");
					return 1;
				}
				printf(" in move %d\n", i+1);
				while (++i < n) {
					scanf("%d%d", &x, &y);
				}
				break;
			}
		}
		if (!found) {
			printf("none\n");
		}
	}
	return 0;
}