#include <stdio.h>
#define	MAX	55

int n,k,b;
int x[MAX];
int v[MAX];
int reach[MAX];
int pass(int i, int j){
	double ti, tj;
	ti = (double)(b - x[i])/v[i];
	tj = (double)(b - x[j])/v[j];
	if(ti < tj) return 1;
	return 0;
}
int crane(int cur){
	int i, count=0;
	for(i=cur+1;i<n;i++){
		if(!reach[i])
			count++;
	}
	return count;
}
void solve(){
	int i,j,count=0;
	int t;
	scanf("%d %d %d %d", &n,&k,&b,&t);
	for(i=0;i<n;i++){
		scanf("%d", &x[i]);
		reach[i]=0;
	}
	for(i=0;i<n;i++){
		scanf("%d", &v[i]);
		if(x[i]+v[i]*t >= b){
			count++;
			reach[i]=1;
		}
	}
	if(count < k){
		printf("IMPOSSIBLE\n");
		return;
	}
	count=0;
	for(i=n-1;i>=0&&k>0;i--){
		if(reach[i]){
			count+=crane(i);
			k--;
		}
	}
	printf("%d\n", count);
	return;
}
int main(){
    int i,T;
    scanf("%d", &T);
    for(i=1;i<=T;i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}

