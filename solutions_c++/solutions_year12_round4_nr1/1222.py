#include <bits/stdc++.h>
using namespace std;




#define Fr(i,a,b) for(int i=a;i<b;++i)
#define F first
#define S second

struct lol{
	int ind, bal;
	lol(int ind=0, int bal=0): ind(ind), bal(bal) {}
	bool operator <(const struct lol &lhs) const{
		if(ind == lhs.ind) return bal < lhs.bal;
		return ind > lhs.ind;
	}
};


int n,d,t;
pair<int,int> v[10010];
bool mark[10100];

int main(){
	scanf("%d",&t);
	Fr(cas,1,t+1){
		memset(mark, false, sizeof(mark));
		scanf("%d",&n);
		Fr(i,0,n){
			scanf("%d %d",&v[i].F,&v[i].S);
		}
		scanf("%d",&d);
		v[n++] = make_pair(d, 0);
		bool vai = false;
		int contant;
		priority_queue<lol> fila;
		fila.push(lol(0, v[0].F));
		while(!fila.empty()){
			lol aux = fila.top();fila.pop();
			if(mark[aux.ind]) continue;
			mark[aux.ind] = true;
			if(aux.ind == n-1) break;
			for(int i = aux.ind+1; i < n; i++){
				if(v[aux.ind].F + aux.bal < v[i].F) break;
				fila.push(lol(i, min(v[i].S, v[i].F-v[aux.ind].F)));
			}
		}
		if(mark[n-1]){
			printf("Case #%d: YES\n",cas);
		}
		else printf("Case #%d: NO\n",cas);
	}
	return 0;
}




































