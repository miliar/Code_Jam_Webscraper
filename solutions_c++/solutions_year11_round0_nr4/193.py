#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

int arr[1024];

int main() {
	int T, N, ans;
	
	scanf("%d\n", &T);
	
	for(int nCase = 1; nCase <= T; nCase++) {
		scanf("%d\n", &N);
		
		for(int i = 0; i < N; i++) {
			scanf("%d", &arr[i]);
			arr[i]--;
		}
		
		ans = 0;
		
		for(int i = 0; i < N; i++) {
			int ln = 0;
			int x = i;
			while (arr[x] != -1) {
				int tmp = arr[x];
				arr[x] = -1;
				x = tmp;
				ln++;
			}
			if (ln >= 2)
				ans += ln;
		}
		
		printf("Case #%d: %d.000000\n", nCase, ans);
	}
}
