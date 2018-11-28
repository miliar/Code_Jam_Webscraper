#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int inp[1024];

void solve(){
	int n;
	scanf("%d", &n);
	int t = 0, s=0, m=5000000;
	for (int i=0;i<n;++i){
		scanf(" %d", &inp[i]);
		t ^= inp[i];
		s += inp[i];
		m = min(m, inp[i]);
	}
	
	if (t == 0){
		printf("%d\n", s-m);
	}else{
		printf("NO\n");
	}
	
}

int main(){
	int T;
	scanf("%d", &T);
	for (int i=1;i<=T;++i){
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
