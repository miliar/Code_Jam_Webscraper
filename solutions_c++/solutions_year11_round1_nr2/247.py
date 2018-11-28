
#include <cstdio>
#include <cstring>

int main(){
	
	int t; scanf("%d", &t);

	char d[100][30]; int len[100];
	char l[10][30];
	int n, m;

	int ex[100][100][26];

	for(int x=1; x<=t; ++x){
		scanf("%d%d", &n, &m);
		for(int i=0; i<n; ++i){
			scanf("%s", d[i]);
			len[i] = strlen(d[i]);
		}
		for(int i=0; i<m; ++i){
			scanf("%s", l[i]);
		}
		memset(ex, 0, sizeof(ex));
		for(int i=0; i<n; ++i){
			for(int j=0; j<n; ++j){
				if(len[i] == len[j] && i != j){
					for(int k=0; k<len[i]; ++k){
						if(d[i][k] != d[j][k]){
							ex[i][j][d[i][k]-'a'] = 1;
							ex[i][j][d[j][k]-'a'] = 1;
						}
					}
				}
			}
		}
		int hash[26];
		printf("Case #%d:", x);
		for(int i=0; i<m; ++i){
			int worse = -1;
			char ans[30];
			for(int j=0; j<n; ++j){
				memset(hash, 0, sizeof(hash));
				for(int k=0; k<n; ++k){
					if(len[j] == len[k] && j != k){
						for(int u=0; u<26; ++u){
							if(ex[j][k][l[i][u]-'a']){
								hash[l[i][u]-'a'] = 1;
								break;
							}
						}
					}
				}
				int sum = 0;
				for(int k=0; k<26; ++k){
					int found = 0;
					if(hash[k]){
						for(int u=0; u<len[j]; ++u){
							if(k == d[j][u]-'a'){
								found = 1;
								break;
							}
						}
						sum += hash[k] - found;
					}
				}
				//printf("sum=%d\n", sum);
				if(sum > worse){
					worse = sum;
					strcpy(ans, d[j]);
				}
			}
			printf(" %s", ans);
		}
		printf("\n");
	}
	return 0;
}
