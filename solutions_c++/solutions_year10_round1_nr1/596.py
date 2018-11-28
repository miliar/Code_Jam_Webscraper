#include <cstdio>

const int N = 55;

const int di[] = { 0, 1, 1, 1 };
const int dj[] = { 1, 0, 1, -1 };

int n, k;
char before[N][N], after[N][N];

void rotate(){
	int curr_i = 0, curr_j = n - 1;
	for (int i = 0; i < n; i++) for (int j = 0; j < n; j++){
		after[curr_i][curr_j] = before[i][j];
		curr_i++;
		if (curr_i == n){
			curr_i = 0;
			curr_j--;
		}
	}
}

void fall(){
	for (int j = 0; j < n; j++){
		bool moving = true;
		while (moving){
			moving = false;
			for (int i = 1; i < n; i++) if (after[i][j] == '.' && after[i - 1][j] != '.'){
				int curr_i = i;
				while (curr_i > 0){
					after[curr_i][j] = after[curr_i - 1][j];
					curr_i--;
				}
				after[0][j] = '.';
				moving = true;
			}
		}
	}
}

bool val(int x){
	return x >= 0 && x < n;
}

bool join(char c, int ini_i, int ini_j, int delta_i, int delta_j){
	int i = ini_i, j = ini_j;
	int need = k;
	while (need > 0 && val(i) && val(j) && after[i][j] == c){
		i += delta_i;
		j += delta_j;
		need--;
	}
	return (need == 0);
}

int evaluate(){
	bool ok[2] = { false, false };
	for (int color = 0; color < 2; color++){
		for (int i = 0; i < n; i++) for (int j = 0; j < n; j++){
			for (int dir = 0; dir < 4; dir++){
				ok[color] |= join("RB"[color], i, j, di[dir], dj[dir]);
			}
		}
	}
	if (!ok[0] && !ok[1]) return 0;
	if (ok[0] && !ok[1]) return 1;
	if (!ok[0] && ok[1]) return 2;
	return 3;
}

int main(){
	int tests; scanf("%d", &tests);
	for (int test = 1; test <= tests; test++){
		scanf("%d %d", &n, &k);
		for (int i = 0; i < n; i++) for (int j = 0; j < n; j++)
			scanf(" %c", &before[i][j]);
		rotate();

		/*for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++) printf("%c", after[i][j]);
			printf("\n");
		}*/

		fall();

		/*for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++) printf("%c", after[i][j]);
			printf("\n");
		}*/

		int ans = evaluate();
		if (ans == 0) printf("Case #%d: Neither\n", test);
		if (ans == 1) printf("Case #%d: Red\n", test);
		if (ans == 2) printf("Case #%d: Blue\n", test);
		if (ans == 3) printf("Case #%d: Both\n", test);
	}

	return 0;
}
