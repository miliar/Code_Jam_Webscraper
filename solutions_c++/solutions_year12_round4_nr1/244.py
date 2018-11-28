#include <stdio.h>
#include <queue>
#include <string>
using namespace std;

int N;
int d[10003];
int l[10003];
int D;

void run(int fall) {
	printf("Case #%d: ", fall);
	scanf("%d", &N);
	for(int i=0;i<N;i++){
		scanf("%d %d", &d[i], &l[i]);
	}
	scanf("%d", &D);
	d[N] = D;
	l[N] = 0;
	queue<pair<int, int> > q;
	q.push(make_pair(-1,0));
	while(!q.empty()){
		pair<int, int> nu = q.front();
		//printf("nu: %d_>%d\n", nu.first, nu.second);
		q.pop();
		int nud = 0;
		if(nu.first>=0){
			nud = d[nu.first];
		}
		int halld = d[nu.second];
		int svingHojd = halld-nud;
		if(svingHojd>l[nu.second]){
			svingHojd = l[nu.second];
		}
		for(int nextDi = nu.second+1; nextDi <= N; nextDi++){
			int nextd = d[nextDi];
			if(nextd-halld > svingHojd)break;
			//if(svingHojd*svingHojd > (nextd-halld)*(nextd-halld) + l[nextDi]*l[nextDi])continue;
			q.push(make_pair(nu.second, nextDi));
			if(nextDi == N){
				printf("YES\n");
				return;
			}
		}
	}
	printf("NO\n");
}


int main(){
	int T;
	scanf("%d", &T);
	for(int i=0;i<T;i++){
		run(i+1);
	}	
}