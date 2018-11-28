#include<cstdio>
#include<queue>
using namespace std;

struct State {
	int l,m,id;
	State(){}
	State(int a,int b,int i):l(a),m(b),id(i) {}
};

int d[10011],l[10011];
int n;
int aim;

bool bfs() {
	queue<State> q;
	q.push(State(d[0],d[0],0));
	while(!q.empty()) {
		State t=q.front(); q.pop();
		int L=t.m+t.l;
		if(L>=aim) return true;
		for(int i=t.id+1;i<n&&d[i]<=L;i++) {
			q.push(State(min(d[i]-t.m,l[i]),d[i],i));
		}
	}
	return false;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	int T; scanf("%d",&T);
	for(int ka=1;ka<=T;ka++) {
		printf("Case #%d: ",ka);
		scanf("%d",&n);
		for(int i=0;i<n;i++) scanf("%d%d",&d[i],&l[i]);
		scanf("%d",&aim);
		puts(bfs()?"YES":"NO");
	}

	return 0;
}
