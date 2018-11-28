#include <cstdio>
#include <cstring>

int in[30];

char opp[30][100];
char comb[30][100];
int deg[30];
char list[200];
int main() {
	int T,n;
	scanf("%d",&T);
	char seq[5];
	for(int t=1;t<=T;++t) {
		printf("Case #%d: ",t);
		scanf("%d",&n);
		memset(comb,0,sizeof(comb));
		memset(in,0,sizeof(in));
		for(int a=0;a<n;++a) {
			scanf(" %s",seq);
			comb[seq[0]-'A'][seq[1]-'A'] = seq[2];
			comb[seq[1]-'A'][seq[0]-'A'] = seq[2];
		}
		scanf("%d",&n);
		for(int a=0;a<30;++a) {
			deg[a] = 0;
		}
		memset(opp,0,sizeof(opp));
		for(int a=0;a<n;++a) {
			scanf(" %s",seq);
			opp[seq[0]-'A'][deg[seq[0]-'A']++] = seq[1]-'A';
			opp[seq[1]-'A'][deg[seq[1]-'A']++] = seq[0]-'A';
		}
		int size = 0;
		scanf("%d",&n);
		char elem;
		for(int a=0;a<n;++a) {
			scanf(" %c",&elem);
			if(size > 0 && comb[elem-'A'][list[size-1]-'A'] != 0) {
				in[list[size-1]-'A']--;
				int d = list[size-1] - 'A';
				list[size-1] = comb[elem-'A'][d];
				in[list[size-1]-'A']++;
				continue;
			}
			bool next = false;
			for(int b=0;b<deg[elem-'A'];++b) {
				int op = opp[elem-'A'][b];
				if(in[op]>0) {
					size = 0;
					for(int c=0;c<30;++c) {
						in[c]=0;
					}
					next = true;
				}
			}
			if(next) continue;
			list[size++] = elem;
			in[elem-'A']++;
		}
		printf("[");
		bool first = true;
		for(int a=0;a<size;++a) {
			if(a == size-1) printf("%c",list[a]);
			else if(first) {
				printf("%c, ",list[a]);
				first = false;
			}
			else {
				printf("%c, ",list[a]);
			}
		}
		printf("]\n");
	}
	return 0;
}
