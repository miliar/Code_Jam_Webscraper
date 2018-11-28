#include <stdio.h>
#include <string.h>

int N, S, Q;
char names[101][102];
char used[101];
int unused;

void clear_used(void) {
	int i;
	for(i=0; i<S; i++) {
		used[i] = 0;
	}
	unused = S;
}

void solve(int case_number) {
	int i,j,switches = 0;
	char query[102];
	clear_used();
	for(i=0; i<Q; i++) {
		fgets(query,101,stdin);
		if(query[strlen(query)] == '\n') {
			query[strlen(query)] = '\0';
		}
		for(j=0; j<S; j++) {
			if(!strcmp(names[j],query)) {
				if(!used[j]) {
					if(unused == 1) {
						clear_used();
						switches ++;
					}
					used[j] = 1;
					unused --;
				}
				break;
			}
		}
	}
	printf("Case #%d: %d\n",case_number,switches);
}

int main(void) {
	freopen("A-large.in","rt",stdin);
	freopen("A.out","wt",stdout);
	
	int i,j;
	
	scanf("%d\n",&N);
	for(i=0; i<N; i++) {
		scanf("%d\n",&S);
		for(j=0; j<S; j++) {
			fgets(names[j],101,stdin);
			if(names[j][strlen(names[j])] == '\n') {
				names[j][strlen(names[j])] = '\0';
			}
		}
		scanf("%d\n",&Q);
		solve(i+1);
	}
	return 0;
}
