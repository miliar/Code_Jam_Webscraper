#include <cstdio>
#include <algorithm>
#include <map>
#include <string>
#include <sstream>
#include <iostream>
#include <set>
#include <vector>
#include <queue>
#include <numeric>
#include <cstdlib>

using namespace std;

#define go(i,v) for(typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
#define fo(i,n) for(int i=0;i<n;i++)
#define fi fo(i,n)
#define fj fo(j,n)
#define fk fo(k,n)

#define mp make_pair

#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define CLEAR(v) memset(v,0,sizeof(v))

typedef pair<int,int> point;
#define x first
#define y second

#define INF (1<<29)

int get() { int x; scanf("%d",&x); return x; }

template<typename T> int sign(T x) { return x < 0 ? -1 : x > 0; }

int ccw(point a,point b,point c){
	b.x-=a.x;
	b.y-=a.y;
	c.x-=a.x;
	c.y-=a.y;
	return sign(b.x*c.y-c.x*b.y);
}

vector<point> hull(vector<point> a) {
	sort(all(a));
	vector<point> ret;

	go(i,a) {
		while(ret.size()>=2&&ccw(ret[ret.size()-2],ret[ret.size()-1],*i)!=-1) ret.pop_back();
		ret.push_back(*i);
	}
	sort(rall(a));
	a.pop_back();
	int limit=ret.size()+1;

	go(i,a) {
		while(ret.size()>=limit&&ccw(ret[ret.size()-2],ret[ret.size()-1],*i)!=-1) ret.pop_back();
		ret.push_back(*i);
	}

	return ret;
}

#define MAX_N 1000

int n;

int adj[MAX_N][MAX_N];
int flow[MAX_N][MAX_N];
int sink,source;

int seen[MAX_N];

bool push(int x,int val) {
	if(x==sink) return true;
	if(seen[x]) return false;
	seen[x]=1;
	fo(i,n) if(adj[x][i]>=val && push(i,val)) {
		adj[x][i]-=val;
		adj[i][x]+=val;
		flow[x][i]+=val;
		flow[i][x]-=val;
		return true;
	}
	return false;
}

int maxflow() {
	int val=(1<<29);
	int ret=0;
	while(val){
		while(true){
			bool worked=push(source,val);
			CLEAR(seen);
			if(!worked)break;
			ret+=val;
		}
		val>>=1;
	}
	return ret;
}

int soln(){
	map<pair<int,int>,bool> isbird;

	n=get();
	// CLEAR(seen);

	vector<int> h(n),w(n),is(n);
	char buf[100];
	fi {
		scanf("%d %d",&h[i],&w[i]);
		scanf("%s",buf);
		if(buf[0]=='N'){
			scanf("%s",buf);
			is[i]=isbird[mp(h[i],w[i])]=false;
		} else {
			is[i]=isbird[mp(h[i],w[i])]=true;
		}
	}

	int m=get();
	fo(i,m) {
		int H,W;
		scanf("%d %d",&H,&W);

		if(isbird.count(mp(H,W))) printf(isbird[mp(H,W)]?"BIRD\n":"NOT BIRD\n");

		bool isbird=false;
		bool know=false;

		fi fj if(i!=j) {
			if(is[i]&&is[j]&&sign(H-h[i])*sign(H-h[j])<=0&&
					         sign(W-w[i])*sign(W-w[j])<=0){
				isbird=true;
				know=true;
				break;
			}
			if(is[i]&&!is[j]&&sign(h[j]-h[i])*sign(h[j]-H)<=0&&
					          sign(w[j]-w[i])*sign(w[j]-W)<=0)
			{
				isbird=false;
				know=true;
				break;
			}
		}

		if(!know) printf("UNKNOWN\n");
		else printf(isbird?"BIRD\n":"NOT BIRD\n");
	}

	return 0;
}

int main() {
	int cases=get();
	fo(i,cases) {
		printf("Case #%d:\n",i+1);
		soln();
	}
	return 0;
}
