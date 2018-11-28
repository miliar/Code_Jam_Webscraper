#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>

using namespace std;

#define REP(i,n) for(int i=0,_n=n; i<n; i++)

void add(long long &b, int i, int r, int c){
	long long k = r*12 + c;
	if (k>=256) printf("%d %d\n",r,c);
	assert(k<256);
	b &= ~( ((1LL<<8)-1LL) << (i*8LL) );
	b |= k << (i*8);
}

void get(long long b, int i, int &r, int &c){
	b >>= i*8;
	b &= (1LL<<8)-1;
	r = b / 12;
	c = b % 12;
}

char m[20][20];
int dr[] = {-1,0,1,0};
int dc[] = {0,1,0,-1};
int N,R,C;
vector<pair<int,int> > arr;

bool ok(int r, int c, long long pos){
	if (r<0 || r>=R || c<0 || c>=C || m[r][c]=='#') return false;
	int rr, cc;
	REP(i,N){
		get(pos, i, rr,cc);
		if (r==rr && c==cc) return false;
	}
	return true;
}

int vis[100];

int rec(int i){
	if (vis[i]) return 0;
	vis[i] = 1;
	int ret = 1;
	REP(j,N) if (j!=i){
		int dx = abs(arr[j].first - arr[i].first);
		int dy = abs(arr[j].second - arr[i].second);
		if (dx + dy != 1) continue;
		ret += rec(j);
	}
	return ret;
}

struct Node {
	long long pos;
	int move;

	Node(long long p, int m){
		REP(i,N) get(p,i,arr[i].first,arr[i].second);
		sort(arr.begin(),arr.end());
		pos = 0;
		REP(i,N){
			add(pos,i,arr[i].first,arr[i].second);
//			printf("> %d %d\n",arr[i].first,arr[i].second);
		}
		REP(i,N) vis[i] = 0;
		int cnt = rec(0);
//		printf("cnt = %d\n",cnt);
		add(pos,N,cnt==N,0); // disconnected
		move = m;
	}

	bool stable(){
		int r, c;
		get(pos, N, r,c);
		return r;
	}

	bool operator<(Node const &that) const {
		return move > that.move;
	}
};

int main(){
	int nTC;
	scanf("%d",&nTC);
	REP(TC,nTC){
		scanf("%d %d",&R,&C);
		REP(i,R) scanf("%s",m[i]);
		long long box = 0, goal = 0;
		int nx=0, no=0;
		REP(i,R) REP(j,C){
			if (m[i][j]=='x' || m[i][j]=='w') add(goal,nx++,i,j);
			if (m[i][j]=='o' || m[i][j]=='w') add(box,no++,i,j);
		}

		N = nx;
		arr.resize(N);
		Node vg(goal,0);
		assert(nx==no);

		/*
		printf("%d %d\n",nx,no);
		REP(i,N){
			int r, c;
			get(goal, i,r,c);
			printf("g %d %d\n",r,c);
			get(box, i,r,c);
			printf("b %d %d\n",r,c);
		}
		REP(i,R) puts(m[i]);
		*/

		int res = -1;
		priority_queue<Node> pq;
		Node s(box,0);

//		printf("start %lld %lld, %lld\n",s.pos,vg.pos,goal);

		assert(s.stable());
		pq.push(s);
		set<long long> vis;
		while (pq.size()>0){
			Node u = pq.top(); pq.pop();
			if (u.pos==vg.pos){
				res = u.move;
				break;
			}

			if (vis.count(u.pos)) continue;
			vis.insert(u.pos);

//			printf("M = %d, %lld %lld\n",u.move,u.pos,vg.pos);
			/*
			REP(i,N){
				int r, c;
				get(u.pos, i,r,c);
				printf("> %d %d\n",r,c);
			}
			*/

			REP(i,N){
				int r,c;
				get(u.pos, i, r, c);
				REP(j,4){
					int nr = r+dr[j], nc = c+dc[j];
					if (!ok(nr,nc,u.pos)) continue;

					int ir = r+dr[(j+2)%4];
					int ic = c+dc[(j+2)%4];
					if (!ok(ir,ic,u.pos)) continue;
					
					Node v = u;
					add(v.pos, i, nr,nc);

					v = Node(v.pos,v.move+1);
					if (!u.stable() && !v.stable()) continue;
					pq.push(v);
				}
			}
		}
		printf("Case #%d: %d\n",TC+1,res);
		fflush(stdout);
		fprintf(stderr,"Case #%d: %d\n",TC+1,res);
	}
}
