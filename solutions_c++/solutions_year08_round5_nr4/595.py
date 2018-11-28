#include <cstdio>
#include <map>
#include <set>
#include <queue>
using namespace std;

typedef pair<int,int> pii;
typedef set<pii> spii;
typedef map<pii, int> mpiii;
typedef queue<pii> qpii;

int main () {
	int N, H,W,R;
	scanf("%d",&N);
	for(int n=0;n<N;++n) {
		scanf("%d%d%d",&H,&W,&R);
		spii argh;
		for(int r=0;r<R;++r) {
			int a,b;
			scanf("%d%d",&a,&b);
			argh.insert(make_pair(a-1,b-1));
		}
		mpiii ways;
		ways[make_pair(H-1,W-1)]=1;
		qpii q;
		q.push(make_pair(H-1,W-1));
		while(!q.empty()) {
			pii p = q.front();
			q.pop();
			if(argh.find(p)!=argh.end())
				continue;
			argh.insert(p);
			pii p2=make_pair(p.first-1,p.second-2);
			if(argh.find(p2)==argh.end() && p2.first<=2*p2.second && p2.second<=2*p2.first) {
				ways[p2]=(ways[p2]+ways[p])%10007;
				q.push(p2);
			}
			p2=make_pair(p.first-2,p.second-1);
			if(argh.find(p2)==argh.end() && p2.first<=2*p2.second && p2.second<=2*p2.first) {
				ways[p2]=(ways[p2]+ways[p])%10007;
				q.push(p2);
			}
		}
		printf("Case #%d: %d\n",n+1, ways[make_pair(0,0)]);
	}
}