#include<cstdio>
#include<cstring>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>

using namespace std;

int main(){
	int T;
	scanf("%d", &T);
	for (int cc = 1; cc <= T; ++cc){
		printf("Case #%d: ", cc);
		int k, L;
		char s[1011];
		scanf("%d%s", &k, s);
		L = strlen(s);
		int P[k];
		for (int i = 0 ; i < k ; ++i) P[i] = i;
		int ans = (1<<29);
		do{
			char ss[1011];
			for (int i = 0 ; i < L / k; ++i)
				for (int j = 0 ; j < k ; ++j)
					ss[i*k+j] = s[i*k+P[j]];
			ss[L] = 0;
			int cnt = 0;
			char lc = 'A';
			for (int i = 0 ; i < L; ++i)
				if (lc != ss[i]){
					cnt++;
					lc = ss[i];
				}
			ans = min(ans, cnt);
		}while (next_permutation(P, P+k));
		printf("%d\n", ans);
	}
	return 0;
}
