/**********************************************************************
Author: LiuLixiang
Created Time:  2010/6/5 22:55:39
File Name: \TopCoder\gcj2010\Round2\B.cpp
Description: 
**********************************************************************/
#include <iostream>
using namespace std;

const int MAXN = 1<<10;

int P, n;
int M[MAXN+10];
int table[11][MAXN+10];
bool yes[11][MAXN+10];

void get_input() {
	scanf("%d", &P);
	n = 1 << P;
	for (int i = 0; i < n; i++) {
		scanf("%d", &M[i]);
	}
	for (int r = 1; r <= P; r++) {
		for (int i = 0; i < (1<<(P-r)); i++) {
			scanf("%d", &table[r][i]);
		}
	}
}

bool cmp(const int &a, const int &b) {
	return M[a] < M[b];
}

int solve() {
	int res = 0;
	//same for small
	int cnt = 0;
	int order[n+10];
	for (int i = 0; i < n; i++) order[i] = i;
	
	sort(order, order+n, cmp);
	memset(yes, false, sizeof(yes));
//	cout << " =========== " << n << endl;//
	for (int i = 0; i < n; i++) {
//		cout << order[i] << endl;///
		for (int j = 0; j < P-M[ order[i] ]; j++) {
			int id = order[i] / ( 1<<(P-j) ); //FIXME
//			cout << id << ",";///
			if (!yes[P-j][id]) {
				++cnt;
				yes[P-j][id] = true;
			}
		}
//		cout << endl;///
	}
	res = cnt * table[1][0]; 
	return res;
}

int main() {
	freopen("B_A.txt", "w", stdout);///
    int T;
	scanf("%d", &T);
	for (int ca = 1; ca <= T; ca++) {
		get_input();
		printf("Case #%d: %d\n", ca, solve());
	}
	fclose(stdout);///
    return 0;
}

