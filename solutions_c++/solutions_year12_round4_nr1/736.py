#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#define MAX 10345

using namespace std;

int main(){
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++){
		int N, D;
		scanf("%d", &N);
		int t[MAX], d[MAX], l[MAX];
		for (int i = 0; i < N; i++){
			scanf("%d%d", &d[i], &l[i]);
			t[i] = -1;
		}
		scanf("%d", &D);
		if(d[0] <= l[0])
			t[0] = min(d[0], l[0]);
		for (int i = 0; i < N; i++) {
			if(t[i] == -1)
				break;
			for (int j = i+1; j < N; j++){
				if(d[j] - d[i] > t[i])
					break;
				t[j] = max(t[j], min(d[j] - d[i], l[j]));
			}
		}
		bool deu = 0;
		for (int i = 0; i < N; i++){
			if (t[i] != -1 && t[i] >= D - d[i]){
				printf("Case #%d: YES\n", tt);
				deu = 1;
				break;
			}
		}
		if (!deu)
			printf("Case #%d: NO\n", tt);
	}
	return 0;
}
