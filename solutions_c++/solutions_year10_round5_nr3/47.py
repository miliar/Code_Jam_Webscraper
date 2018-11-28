#include <iostream>
#include <cstring>
#include <cstdio>
#include <map>

using namespace std;

const int maxn = 1000;
const int maxq = 100000;

map<int,int> a;
map<int,bool> iq;
int queue[maxq], qin, qout;

int main()
{
	freopen("C.in","r",stdin); freopen("C.out", "w", stdout);
	int c; scanf("%d", &c);
	for (int casenum=1; casenum<=c; ++casenum){
		int n;
		scanf("%d",&n);
		a.clear(); iq.clear();
		qin = -1; qout = -1;
		for (int i=0; i<n; ++i){
			int p,v; scanf("%d%d",&p,&v);
			a[p] = v;
			if (v>=2){
				qin=(qin+1)%maxq;
				queue[qin]=p;
				iq[p]=true;
			}
		}
		int ans=0;
		while (qout!=qin){
			qout=(qout+1)%maxq;
			int u=queue[qout];
			if (a[u]>=2){
				int v=a[u]/2;
				ans+=v;
				a[u]-=v*2;
				a[u-1]+=v; if (a[u-1]>=2&&!iq[u-1]){ qin=(qin+1)%maxq; queue[qin]=u-1; iq[u-1]=true;}
				a[u+1]+=v; if (a[u+1]>=2&&!iq[u+1]){ qin=(qin+1)%maxq; queue[qin]=u+1; iq[u+1]=true;}
			}
			iq[u]=false;
		}
		printf("Case #%d: %d\n", casenum, ans);
	}
	return 0;
}
