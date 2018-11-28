#include<stdio.h>
#include<string.h>
#include<map>
using namespace std;

void chkmn(int &t, int a) { if(a<t) t=a; }
void chkmx(int &t, int a) { if(a>t) t=a; }
map<pair<int, int>, int> pt;
pair<int, int> pp[1000000];
bool flag[1000000];
int que[1000000];
int bfs(int n) {
	int head=0, tail=0;
	que[tail++]=n;
	flag[n]=true;
	int mn=10000000, mxx=-1, mxy=-1;
	while(head<tail) {
		pair<int, int> p=pp[que[head++]];
		chkmn(mn, p.first+p.second);
		chkmx(mxx, p.first);
		chkmx(mxy, p.second);
		for(int x=-1;x<=1;x++) {
			for(int y=-1;y<=1;y++) {
				if(x==y) continue;
				pair<int, int> np=make_pair(p.first+x, p.second+y);
				map<pair<int, int>, int>::iterator it=pt.find(np);
				if(it==pt.end()) continue;

				int id=it->second;
				if(flag[id]) continue;

				flag[id]=true;
				que[tail++]=id;
			}
		}
	}
	return mxx+mxy-mn;
}
int solve() {
	pt.clear();
	memset(flag, 0, sizeof(flag));
	int R, p=0;
	scanf("%d", &R);
	for(int i=0;i<R;i++) {
		int X1, Y1, X2, Y2;
		scanf("%d%d%d%d", &X1, &Y1, &X2, &Y2);
		for(int j=X1;j<=X2;j++)
			for(int k=Y1;k<=Y2;k++) {
				pt[pp[p]=make_pair(j, k)]=p;
				p++;
			}
	}
	int mx=-1;
	for(int i=0;i<p;i++) {
		if(!flag[i])
			chkmx(mx, bfs(i));
	}
	return mx+1;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int c=1;c<=T;c++) {
		printf("Case #%d: %d\n", c, solve());
	}
}