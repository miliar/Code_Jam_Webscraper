#include <cstdio>
#include <deque>
#include <vector>
#include <cstring>
#include <algorithm>
#include <string>
#include <cmath>
#include <set>
#include <map>

using namespace std;

int T;

int N, L ,H;
int inp[1024];

void solve(){
	scanf("%d%d%d", &N, &L, &H);
	for (int i=0;i<N;++i){
		scanf(" %d", &inp[i]);
	}
	for (int i=L;i<=H;++i){
		bool can = true;
		for (int j=0;j<N;++j){
			if ( i % inp[j] != 0 && inp[j] % i != 0 ){
				can = false; break;
			}
		}
		if (can){
			printf("%d\n", i); return;
		}
	}
	printf("NO\n");
}

int main(){
	scanf("%d", &T);
	for (int tc=1;tc<=T;++tc){
		printf("Case #%d: ", tc);
		solve();
	}

	return 0;
}
