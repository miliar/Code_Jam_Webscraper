#include <cstdio>

using namespace std; 

const int maxn = 1003; 

int T;
int N; 
int a[maxn];
double ans; 
bool visited[maxn];

void input(){
	scanf("%ld", &N); 
	for (int i = 1; i <= N; i++){
		scanf("%ld", &(a[i]));
		visited[i] = false; 
	}
}

void work(){
	ans = 0; 
	for (int i = 1; i <= N; i++) {
		if (visited[i] || a[i] == i) continue; 
		int cur = i; 
		int cnt = 0; 
		while (!visited[cur]){
			visited[cur] = true;
			cur = a[i]; 
			cnt++;
		}
		ans += cnt; 
	}
}

void output(int cnt){
	printf("Case #%ld: %.6lf\n", cnt, ans);
}

int main(){
//	freopen("E:\\Algorithms\\GoogleJam\\GoogleJam\\input\\D-large.in","r",stdin);
//	freopen("E:\\Algorithms\\GoogleJam\\GoogleJam\\input\\D-large.out","w",stdout);
	scanf("%ld", &T); 
	for (int i = 0; i < T; i++) {
		input();
		work(); 
		output(i + 1);
	}
//	fclose(stdout);
}