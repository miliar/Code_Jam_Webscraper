#include <cstdio>
#include <map>
#include <set>
#include <cstring>
#include <algorithm>
using namespace std;

int X,S,R,t,N;

const int INF = 0xFFFFFFF;

struct Edge {
	int xi,xf,v;
};

Edge corr[2000];

map<int,int> xs;
int adj[3000][3000];
int deg[3000];
double w[2000][2000];
bool foi[1000020];
int map1[1000020];
int map2[1000020];
int verts[3000];
double dist[3000];
bool dentro[3000];
int pai[3000];
int V[3000][3000];
int num;

void dijkstra() {
	for(int a=0;a<num;++a) {
		dist[a] = INF;
		dentro[a] = false;
		pai[a] = -1;
	}
	dist[0] = 0;
	int v = 0;
	while(v != -1) {
		//printf("%d\n",v);
		dentro[v] = true;
		for(int a=v+1;a<num;++a) {
			if(dist[a] >= dist[v] + w[v][a]) {
				dist[a] = dist[v] + w[v][a];
				pai[a] = v;
			}
		}
		v = -1;
		double d = INF;
		for(int a=0;a<num;++a) {
			if(dist[a] < d && !dentro[a]) {
				v = a;
				d = dist[a];
			}
		}
	}
	return;
}

int main() {
	int I;
	scanf("%d",&I);
	for(int q=1;q<=I;++q) {
		scanf("%d%d%d%d%d",&X,&S,&R,&t,&N);
		memset(foi,false,sizeof(foi));
		num = 0;		
		foi[0] = foi[X] = true;
		verts[num++] = 0;
		verts[num++] = X;
		for(int a=0;a<N;++a) {
			scanf("%d%d%d",&corr[a].xi,&corr[a].xf,&corr[a].v);
			if(!foi[corr[a].xi]) {
				foi[corr[a].xi] = true;
				verts[num++] = corr[a].xi;
			}
			if(!foi[corr[a].xf]) {
				foi[corr[a].xf] = true;
				verts[num++] = corr[a].xf;
			}
		}
		
		sort(&verts[0],&verts[num]);
		for(int a=0;a<num;++a) {
			map1[verts[a]] = a;
			map2[a] = verts[a];
		}
		for(int a=0;a<num;++a) {
			for(int b=a+1;b<num;++b) {
				adj[a][deg[a]++] = b;
				w[a][b] = double(map2[b]-map2[a])/S;
				V[a][b] = S;
			}
		}
		for(int a=0;a<N;++a) {
			int i = map1[corr[a].xi];
			int f = map1[corr[a].xf];
			w[i][f] = min(w[i][f], double(corr[a].xf-corr[a].xi)/(S+corr[a].v));
			V[i][f] = S+corr[a].v;
		}
		dijkstra();
		multiset< pair<int,int> > vels;
		vels.clear();
		int cur = map1[X];
		while(cur != 0) {
			vels.insert(make_pair(V[pai[cur]][cur],map2[cur]-map2[pai[cur]]));
			cur = pai[cur];
		}
		//printf("vels.size = %d\n",vels.size());
		double res;
		double v = double(X)/dist[map1[X]];
		res = double(X)/v;
		double left = t;
		while(left > 0 && !vels.empty()) {
			//printf("left = %lf\n",left);
			int vel = vels.begin()->first;
			int ds = vels.begin()->second;
			//printf("vel = %d, ds = %d\n",vel,ds);
			vels.erase(vels.begin());
			double time = double(ds)/vel;
			double time2 = double(ds)/(vel+R-S);
			if(time2 < left) {
				//printf("greater\n");
				res -= time;
				left -= time2;
				res += time2;
			}
			else {
				double DS = (vel+R-S)*left;
				res -= double(DS)/vel;
				res += double(DS)/(vel+R-S);
				break;
			}
			//printf("left = %lf\n",left);
		}
		printf("Case #%d: %lf\n",q,res);
	}
	return 0;
}
		
