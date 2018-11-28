/*
Author: TangQiao @ Netease Youdao.
2011.5.7
*/
#include <stdio.h>
#include <string>
#include <math.h>
using namespace std;

int ans;
int task[2][110];
int move[110];

void init() {
	char str[3];
	int j, k;
	ans = 0;
	memset(task, 0, sizeof(task));
	memset(move, 0, sizeof(move));
	int n;
	scanf("%d", &n);
	
	for (int i = 0; i < n; ++i) {
		scanf("%s%d", str, &j);
		k = str[0] == 'O' ? 0 : 1;
		task[k][++task[k][0]] = j;    
		move[++move[0]] = k;
	}
}

void deal() {
	int pos[2] = {1, 1};
	int pt[2] = {1, 1};
	int cost, toCost;
	int a, b;

	for (int i = 0 ; i < move[0]; ++i) {
		a = move[i+1];
		b = a^1;
		cost = abs(task[a][pt[a]] - pos[a]) + 1;
		ans += cost;
		pos[a] = task[a][pt[a]];
		pt[a]++;
		toCost = abs(task[b][pt[b]] - pos[b]);
		if (cost >= toCost) {
			pos[b] = task[b][pt[b]];
		} else {
			if (task[b][pt[b]] > pos[b]) {
				pos[b] += cost;
			} else {
				pos[b] -= cost;
			}
		}	
	}
}

int main() {
    int N;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
    scanf("%d", &N);
    for (int i = 0; i < N; ++i) {
        init();
        deal();
        printf("Case #%d: %d\n", i+1, ans);
    }
    return 0;
}

/*
Sample Test Case:
   
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
Case #1: 6
Case #2: 100
Case #3: 4

My Test Case:
10
1 O 1
1 B 1
2 O 1 B 1
2 O 2 B 2


*/