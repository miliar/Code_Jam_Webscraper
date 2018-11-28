#include<cstdio>
#include<cstdlib>
#include<cstring>

char ans[1000], inp[1000], tmp[5];
int opp[500][500], comb[500][500];
int pos;

void fix() {
	if(pos == 1)
		return;
	
	if(comb[ans[pos - 1]][ans[pos - 2]]) {
		ans[pos - 2] = comb[ans[pos - 1]][ans[pos - 2]];
		--pos;
	} else {
		for(int i = 0; i < pos - 1; ++i) {
			if(opp[ans[i]][ans[pos -1]]) {
				pos = 0;
				return;
			}
		}
	}
}

void output() {
	printf("[");
	if(pos) {
		printf("%c", ans[0]);
		for(int i = 1; i < pos; ++i)
			printf(", %c", ans[i]);
	}
	printf("]");
}

int main() {
	int t, n;
	freopen("B-large.in", "r", stdin);
	freopen("OutLargeB.txt", "w", stdout);
	
	scanf("%d", &t);
	//fprintf(stderr, "%d\n", t);
	for(int kase = 1; kase <= t; ++kase) {
		fprintf(stderr, "%d\n", kase);
		
		
		memset(comb, 0, sizeof(comb));
		memset(opp, 0, sizeof(opp));
		scanf("%d", &n);
		while(n--) {
			scanf("%s", tmp);
			comb[tmp[0]][tmp[1]] = comb[tmp[1]][tmp[0]] = tmp[2];
		}
		
		scanf("%d", &n);
		while(n--) {
			scanf("%s", tmp);
			opp[tmp[0]][tmp[1]] = opp[tmp[1]][tmp[0]] = 1;
		}
		
		pos = 0;
		scanf("%d %s", &n, inp);
		for(int i = 0; i < n; ++i) {
			ans[pos++] = inp[i];
			fix();
		}
		
		printf("Case #%d: ", kase);
		output();
		printf("\n");
	}
}

