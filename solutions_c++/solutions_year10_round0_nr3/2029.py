#include <cstdio>
#include <cstring>
#define MAXN 1004
int r, k, n;
int g[MAXN];
int was[MAXN];

long long roll(int &t){
	long long curr;
	fprintf(stderr,"(");
	int cnt = 0;
	for(curr = 0; cnt < n && curr + g[t] <= k; t = (t+1)%n){
		curr += g[t];
		++cnt;
		fprintf(stderr,"%d ", g[t]);
	}
	fprintf(stderr,") ");
	return curr;
}

long long solve(){
	memset(was, 0, sizeof(was));
	
	long long ret=0;
	int t = 0, time = 0;
	
	while(time < r){
		if(was[t]==1) break;
		was[t]=1;
		ret += roll(t);
		++time;
	}
	long long cy_val = 0, cy_len = 0;
	int h=t;
	while(time < r){
		if(was[h]==2) break;
		was[h]=2;
		cy_val += roll(h);
		++cy_len;
	}
	if(cy_len){
		int cy_num = ( r - time ) / cy_len;
		ret += cy_num * cy_val;
		time += cy_num * cy_len;
	}
	while(time < r){
		ret += roll(t);
		++time;
	}
	
	return ret;
}

int main(){
	int num;
	scanf("%d", &num);
	for(int casenum = 0; casenum < num; ++casenum){
		scanf("%d%d%d", &r,&k,&n);
		for(int i = 0; i < n; ++i){
			scanf("%d", &g[i]);
		}
		
		printf("Case #%d: %lld\n", casenum+1, solve());
		
	}
	return 0;
}
