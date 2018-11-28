#include <stdio.h>
#include <math.h>
#include <string.h>
#include <vector>
#include <queue>
#include <algorithm>
#include <stdlib.h>

using namespace std;

#define min(a,b) ((a)>(b)?(b):(a))
#define max(a,b) ((a)>(b)?(a):(b))

#define INF 1000000
#define maxn 2010
#define maxm 2010

int n,m;
int res[maxn];

struct cust{
	int k;
	int pref[maxn];
	int malted;
} mas[maxm];

void init(){
	int i,j,t,y,k;
	scanf("%d%d",&n,&m);
	for (i=0;i<m;i++){
		scanf("%d",&mas[i].k);
		k=0;
		mas[i].malted=-1;
		for (j=0;j<mas[i].k;j++){
			scanf("%d%d",&t,&y);
			if (y){
				mas[i].malted=t-1;
			}else
				mas[i].pref[k++]=t-1;
		}
		if (mas[i].malted!=-1)
			mas[i].k--;
	}
}

int check(int k){
	int i;
	int t;
	for (i=0;i<mas[k].k;i++){
		if (res[mas[k].pref[i]]==0)
			return 1;
	}
	if (mas[k].malted!=-1 && res[mas[k].malted]==1)
		return 1;
	return 0;
}

void solve(){
	int i,j;
	for (i=0;i<n;i++)
		res[i]=0;
	for (i=0;i<m;i++){
		if (check(i)==0){
			if (mas[i].malted!=-1 && res[mas[i].malted]==0){
				res[mas[i].malted]=1;
				i=-1;
			}else{
				printf("IMPOSSIBLE\n");
				return;
			}
		}
	}
	for (i=0;i<n;i++)
		printf("%d ",res[i]);
	printf("\n");
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int ntest,i;
	scanf("%d",&ntest);
	for (i=1;i<=ntest;i++){
		init();
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}