#include <cstdio>
#include <cstring>

char dict[200][30];
bool tem[200][30];
bool pos[200];
bool has[50];
char alpha[50];

int main() {
	int T,N,M;
	scanf("%d",&T);
	for(int t=1;t<=T;++t) {
		printf("Case #%d: ",t);
		scanf("%d%d",&N,&M);
		for(int a=0;a<N;++a) {
			memset(tem[a],false,sizeof(tem[a]));
		}
		for(int a=0;a<N;++a) {
			scanf(" %s",dict[a]);
			int s = strlen(dict[a]);
			for(int b=0;b<s;++b) {
				tem[a][dict[a][b]-'a'] = true;
			}
		}
		for(int a=0;a<M;++a) {
			scanf(" %s",alpha);
			int s = strlen(alpha);
			int best = -1;
			int ans;
			for(int b=0;b<N;++b) {
				int cont = 0;
				int qntd = N;
				int len = strlen(dict[b]);
				for(int c=0;c<N;++c) {
					if(strlen(dict[c]) == len)pos[c] = true;
					else pos[c] = false;
				}
				for(int c=0;c<s;++c) {
					char letter = alpha[c];
					bool exist = false;
					for(int d=0;d<N;++d) {
						if (pos[d] && tem[d][letter-'a']) exist = true;
					}
					if(!exist) continue;
					if(!tem[b][letter-'a']) ++cont;
					for(int d=0;d<N;++d) {						
						if(d == b) continue;
						if(!pos[d]) continue;
						if(strlen(dict[d]) != len) {
							pos[d] = false;
							--qntd;
							continue;
						}
						for(int e=0;e<len && pos[d];++e) {
							if(dict[b][e] == letter) {
								if(dict[d][e] != letter) {
									pos[d] = false;
									--qntd;
								}
							}
							else if(dict[b][e] != letter) {
								if(dict[d][e] == letter) {
									pos[d] = false;
									--qntd;
								}
							}
						}
					}
					if(qntd == 1) break;
				}
				if(cont > best) {
					best = cont;
					ans = b;
				}
			}
			printf("%s ",dict[ans]);
		}
		printf("\n");
	}
	return 0;
}
