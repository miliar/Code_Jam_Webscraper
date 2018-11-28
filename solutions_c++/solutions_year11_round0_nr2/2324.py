#include <cstdio>

const int NN = 128, MM = 48;

int T, n, c, o;
char combine[MM][4];
char opposed[MM][3];
char seq[NN];
int a;
char ans[NN];

char combines(char a, char b) {
	for(int i = 0; i < c; i++) {
		if(combine[i][0] == a && combine[i][1] == b) return combine[i][2];
		if(combine[i][0] == b && combine[i][1] == a) return combine[i][2];
	}
	return 0;
}

bool opposes(char a, char b) {
	for(int i = 0; i < o; i++) {
		if(opposed[i][0] == a && opposed[i][1] == b) return true;
		if(opposed[i][0] == b && opposed[i][1] == a) return true;
	}
	return false;
}

int main(void) {
	scanf("%d", &T);
	for(int C = 1; C <= T; C++) {
		scanf("%d", &c);
		for(int i = 0; i < c; i++) 
			scanf("%s", combine[i]);
		scanf("%d", &o);
		for(int i = 0; i < o; i++)
			scanf("%s", opposed[i]);
		scanf("%d", &n);
		scanf("%s", seq);

		a = 0;
		for(int i = 0; i < n; i++) {
			char cmb = 0;
			ans[a] = seq[i];
			if(a) cmb = combines(ans[a], ans[a-1]);
			if(cmb) {
				ans[--a] = cmb;
				a++;
				continue;
			}
			bool cleared = false;
			for(int j = 0; j < a; j++) {
				if(opposes(ans[a], ans[j])) {
					a = 0;
					cleared = true;
					break;
				}
			}
			if(!cleared) a++;
		}
		printf("Case #%d: ", C);
		printf("[");
		for(int i = 0; i < a; i++) {
			if(i) printf(", ");
			printf("%c", ans[i]);
		}
		printf("]\n");
	}

	return 0;
}
