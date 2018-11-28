#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
#include<set>
using namespace std;

typedef long long llt;
#define maxn 55
int ttt;

int N, K, B, T;
int x[maxn],v[maxn];
char flag[maxn];//can reach
int val[maxn];

void solve(){
	int i,j,k;
	int res=0;
	llt tmp;
	scanf("%d%d%d%d", &N,&K, &B,&T);
	for(i=0;i<N;++i) scanf("%d", x+i);
	for(i=0;i<N;++i) scanf("%d", v+i);
	
	for(i=0;i<N;++i){
		tmp = v[i] * T ;
		tmp+= x[i];
		if(tmp >= B) flag[i] = 1;
		else flag[i]=0;
	}
	for(i=0;i<N;++i){
		if(flag[i]){
			val[i]= 0;
			for(j=0;j<N;++j){
				if(!flag[j] && x[i]< x[j]){
					++val[i];
				}
			}
		}else val[i] = maxn;
	}
	
	sort(val, val+N);
/*	printf("test \n");
	for(i=0;i<N;++i) printf("%d ", val[i]); printf("\n");
	printf("test \n");
*/	
	res=0;
	for(i=0;i<K;++i){
		if(val[i]== maxn) break;
		res += val[i];
	}
	printf("Case #%d: ",++ttt);
	if(i>= K) printf("%d\n",res);
	else printf("IMPOSSIBLE\n");
}
int main(){
//	freopen("B-large.in","r",stdin);
//	freopen("B-large.out","w",stdout);
	int t;scanf("%d",&t);
	ttt=0;
	while(--t>=0) solve();
	return 0;
}
