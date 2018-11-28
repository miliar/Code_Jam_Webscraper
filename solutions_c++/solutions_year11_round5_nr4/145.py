#include<cstdio>
char line[1001];
int ans[100];
bool found;
inline long long sqr(long long K){return K * K;}
long long Sqrt(long long K){
	long long bg = 0, ed = 2147483647, mid;
	while(1){
		mid = (bg + ed) / 2;
		if(sqr(mid) <= K){
			if(sqr(mid + 1) > K)return mid;
			else bg = mid + 1;
		}else ed = mid - 1;
	}
	return -1;
}
void DFS(int dep, long long now){
	if(!line[dep]){
		long long tmp = Sqrt(now);
		if(sqr(tmp) == now)found = true;
	}else if(line[dep] != '?'){
		DFS(dep + 1, now * 2 + line[dep] - '0');
		ans[dep] = line[dep] - '0';
	}else{
		ans[dep] = 0;
		DFS(dep + 1, now * 2);
		if(found)return;
		ans[dep] = 1;
		DFS(dep + 1, now * 2 + 1);
		if(found)return;
	}
}
int T;
int main(){
	freopen("D-small.in", "r", stdin);
	freopen("D-small.out", "w", stdout);
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		found = false;
		scanf("%s", line);
		DFS(0, 0);
		printf("Case #%d: ", t);
		for(int i = 0; line[i]; i++)
			printf("%d", ans[i]);
		putchar('\n');
	}
}
