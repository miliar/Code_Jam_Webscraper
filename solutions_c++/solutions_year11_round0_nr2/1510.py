#include <cstdio>
#include <cstring>
using namespace std;

int C, D, N;
char combi[30][30];
char clear[30][30];
char list[110];
char buf[110];
int nlist;

void init()
{
	for(int i = 0; i < 30; i++) {
		for(int j = 0; j < 30; j++) {
			combi[i][j] = clear[i][j] = -1;
		}
	}
}

int main()
{
	int T,nCase=0;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	while(T--) {
		init();
		scanf("%d",&C);
		for(int i = 0; i < C; i++) {
			scanf("%s",buf);
			combi[buf[0] - 'A'][buf[1] - 'A'] = buf[2];
			combi[buf[1] - 'A'][buf[0] - 'A'] = buf[2];
		}
		scanf("%d",&D);
		for(int i = 0; i < D; i++) {
			scanf("%s",buf);
			clear[buf[0] - 'A'][buf[1] - 'A'] = 1;
			clear[buf[1] - 'A'][buf[0] - 'A'] = 1;
		}
		scanf("%d",&N);
		scanf("%s",buf);
		nlist = 0;
		for(int i = 0; i < N; i++) {
			list[nlist++] = buf[i];
			while(nlist - 2 >=0 && combi[list[nlist-1] - 'A'][list[nlist - 2] - 'A'] != -1) {
				list[nlist - 2] = combi[list[nlist-1] - 'A'][list[nlist - 2] - 'A'];
				nlist--;
			}
			if(nlist > 1) {
				for(int j = 0; j < nlist -1; j++) {
					if(clear[list[j] - 'A'][list[nlist - 1] - 'A'] == 1) {
						nlist = 0;
					}
				}
			}
		}
		printf("Case #%d: ",++nCase);
		printf("[");
		for(int i = 0; i < nlist; i++) {
			printf("%c",list[i]);
			if(i != nlist -1) {
				printf(", ");
			}
		}
		printf("]\n");
	}
	return 0;
}