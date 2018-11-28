#include<cstdio>
#include<cstring>
#include<vector>
using namespace std;

int adj[20][30][30];
int ptr[5010];
char line[250000];
char word[5010][50];

int main(){
	int L, N, K;
	scanf("%d%d%d", &L, &K, &N);
	for (int i = 0 ; i < K; ++i) scanf("%s", word[i]);

	for (int i = 0 ; i < N; ++i){
		scanf("%s", line);
		int len = strlen(line);
		memset(ptr, 0, sizeof(ptr));
		for (int j = 0, lv=0 ; j < len; ++j, ++lv)
			if (line[j] != '('){
				int y = line[j];
				for (int k = 0 ; k < K; ++k)
					if (ptr[k] == lv && word[k][lv] == y)
						ptr[k]++;
			}else{
				while (line[++j] != ')'){
					int y = line[j];
					for (int k = 0 ; k < K; ++k)
						if (ptr[k] == lv && word[k][lv] == y)
							ptr[k]++;
				}
			}
		int ans = 0;
		for (int j = 0 ; j < K; ++j) ans += ptr[j] == L;
		printf("Case #%d: %d\n", i+1, ans);
	}
	return 0;
}
