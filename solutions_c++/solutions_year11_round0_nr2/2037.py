#include <cstdio>
#include <cstring>

using namespace std;

const int N = 110;
const int SIZE = 130;
const int INF = -1;

int combine[SIZE][SIZE];
bool oppose[SIZE][SIZE];

char strRet[N];
int cnt;
char strTmp[N];

void initCombine() {
	for (int i = 0; i < SIZE; i ++) {
		for (int j = 0; j < SIZE; j ++) {
			combine[i][j] = INF;
		}
	}	
}

void initOppose() {
	for (int i = 0; i < SIZE; i ++) {
		for (int j = 0; j < SIZE; j ++) {
			oppose[i][j] = false;
		}
	}
}

void scaf(int &n) {

	initCombine();
	initOppose();

	int c, d;

	scanf("%d", &c);

	for (int i = 0; i < c; i ++) {
		scanf("%s", strTmp); 
		combine[strTmp[0]][strTmp[1]] = strTmp[2];
		combine[strTmp[1]][strTmp[0]] = strTmp[2];
	}

	scanf("%d", &d);

	for (int i = 0; i < d; i ++) {
		scanf("%s", strTmp);
		oppose[strTmp[0]][strTmp[1]] = true;
		oppose[strTmp[1]][strTmp[0]] = true;
	}

	scanf("%d%s", &n, strTmp);
}
bool isCombineOk() {
	int i = strRet[cnt - 1];
	int j = strRet[cnt - 2];

	if (combine[i][j] == INF)
		return false;
	
	strRet[cnt - 2] = combine[i][j];
	cnt --;
}

bool isOppose() {
	int idx = cnt - 1;

	for (int i = 0; i < idx; i ++) {
		if (oppose[strRet[i]][strRet[idx]]) {
			return true;
		}
	}

	return false;
}
void solve(int n) {
	cnt = 0;

	for (int i = 0; i < n; i ++) {
		strRet[cnt ++] = strTmp[i];


		while (cnt > 1 && isCombineOk()) {
		}

		if (cnt > 1 && isOppose())
			cnt = 0;
	}

}
void prit(int cas) {
	printf("Case #%d: ", cas);

	printf("[");
	int ed = cnt - 1;
	for (int i = 0; i < ed; i ++) {
		printf("%c, ", strRet[i]);
	}
	if (ed >= 0)
		printf("%c", strRet[ed]);
	printf("]\n");
}

int main() {

	//freopen("Lin.txt", "r", stdin);
	//freopen("Lout.txt", "w", stdout);

	int t, n;
	scanf("%d%*c", &t);

	for (int cas = 1; cas <= t; cas ++) {
		scaf(n);

		solve(n);
	
		prit(cas);
	}
	return 0;
}