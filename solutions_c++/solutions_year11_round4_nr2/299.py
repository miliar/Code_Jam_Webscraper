#include <cstdio>

int R, C, D;
int weight[510][510];
int wxpx[510][510];
int wxpy[510][510];

int sumw[510][510];
int sumwxpx[510][510];
int sumwxpy[510][510];

void Open() {
	freopen ("P2.in", "r", stdin);
	freopen ("P2.out", "w", stdout);
}

void Close() {
	fclose(stdin);
	fclose(stdout);
}

void init() {
	scanf ("%d %d %d", &R, &C, &D);
	for (int i = 0; i <= R; i++) {
		scanf ("\n");
		for (int j = 0; j <= C; j++) {
			if (i == 0 || j == 0) {
				weight[i][j] = 0;
				wxpx[i][j] = wxpy[i][j] = 0;
				sumw[i][j] = 0;
				sumwxpx[i][j] = sumwxpy[i][j] =  0;
			} else {
				char tmp;
				scanf ("%c", &tmp);
				weight[i][j] = tmp - 48;
				wxpx[i][j] = weight[i][j] * i;
				wxpy[i][j] = weight[i][j] * j;
				sumw[i][j] = sumw[i - 1][j] + sumw[i][j - 1] - sumw[i - 1][j - 1] + weight[i][j];
				sumwxpx[i][j] = sumwxpx[i - 1][j] + sumwxpx[i][j - 1] - sumwxpx[i - 1][j - 1] + wxpx[i][j];
				sumwxpy[i][j] = sumwxpy[i - 1][j] + sumwxpy[i][j - 1] - sumwxpy[i - 1][j - 1] + wxpy[i][j];
			}
		}
	}
}

bool search(int K) {
	for (int bx = 1; bx <= R - K + 1; bx++)
		for (int by = 1; by <= C - K + 1; by++) {
			int ex = bx + K - 1;
			int ey = by + K - 1;
			int delwxpx = weight[bx][by] * bx + weight[bx][ey] * bx + weight[ex][by] * ex + weight[ex][ey] * ex;
			int delwxpy = weight[bx][by] * by + weight[bx][ey] * ey + weight[ex][by] * by + weight[ex][ey] * ey;
			int delw = weight[bx][by] + weight[bx][ey] + weight[ex][by] + weight[ex][ey];
			int rsumwxpx = sumwxpx[ex][ey] - sumwxpx[ex][by - 1] - sumwxpx[bx - 1][ey] + sumwxpx[bx - 1][by - 1] - delwxpx;
			int rsumwxpy = sumwxpy[ex][ey] - sumwxpy[ex][by - 1] - sumwxpy[bx - 1][ey] + sumwxpy[bx - 1][by - 1] - delwxpy;
			int rsumw = sumw[ex][ey] - sumw[ex][by - 1] - sumw[bx - 1][ey] + sumw[bx - 1][by - 1] - delw;
			if ((rsumwxpx * 2) == (rsumw * (bx + ex)) && (rsumwxpy * 2) == (rsumw * (by + ey))) 
				return true;
		}
	return false;
}

int work() {
	int answer = R < C ? R : C;
	for (; answer > 2; answer--) {
		if (search(answer)) break;
	}
	return answer;
}

void output(int caseNo, int answer) {
	printf ("Case #%d: ", caseNo);
	if (answer < 3) 
		printf ("IMPOSSIBLE\n");
	else 
		printf ("%d\n", answer);
}

void process() {
	int T;
	scanf ("%d", &T);
	for (int caseNo = 1; caseNo <= T; caseNo++) {
		init();
		output(caseNo, work());
	}
}

int main() {
	Open();
	process();
	Close();
	return 0;
}