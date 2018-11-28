#include <cstdio>
#include <queue>
using namespace std;
int TC,R,k,n,TR,p,rd[10005],t;
struct node{
	int pos,g;
	node(){}
	node(int pos,int g):pos(pos),g(g){}
	 
};
long long D[10005],cost=0,AC=0;
queue<node> Q;
int main(){
	scanf("%d",&TC);
	for (int C=1;C<=TC;C++){
		scanf("%d%d%d",&R,&k,&n);
		while (!Q.empty()) Q.pop();
		for (int i=1;i<=n;i++){
			scanf("%d",&p),
			Q.push(node(i,p)),
			D[i]=-1; rd[i]=-1;
		}
		D[1]=0; rd[1]=0; TR=0; cost=0;
		while (TR<R){
			TR++;
			long long cnt=0; int w=0;
			while (w<n && cnt+Q.front().g<=k){
				w++;
				cnt+=Q.front().g;
				Q.push(Q.front()); Q.pop();
			}
			cost+=cnt; t=Q.front().pos;
			if (D[t]==-1){
				D[t]=cost; rd[t]=TR;
			}
			else {
				int cycle=TR-rd[t];
				long long cc=cost-D[t],
				re=rd[t]+(R-rd[t])%cycle;
				if (R<rd[t]){
					for (int i=1;i<=n;i++)
						if (rd[i]==R) AC=D[i];
				}
				else {
					for (int i=1;i<=n;i++)
						if (rd[i]==re) AC=D[i]-D[t];
					AC+=D[t]+cc*((R-rd[t])/cycle);
				}
				break;
			}
		}
		if (TR==R) AC=cost;
		printf("Case #%d: %lld\n",C,AC);
	}
	scanf("\n");
	return 0;
}
