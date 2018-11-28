
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

int N, K;
char a[50][50];
char b[50][50];

void rotate() {
	// (i, j) -> (j, N-i-1)
	for(int i = 0; i < N; i++)
		for(int j = 0; j < N; j++)
			b[j][N-i-1] = a[i][j];
}

void fall() {
	for(int j = 0; j < N; j++) {
		vector <char> row;
		for(int i = 0; i < N; i++)
			if(b[i][j] != '.')
				row.push_back(b[i][j]);
		for(int i = 0; i < (int) row.size(); i++)
			b[N-row.size()+i][j] = row[i];
		for(int i = (int) row.size(); i < N; i++)
			b[i-row.size()][j] = '.';
	}
}

inline bool in_bounds(int i, int j) {
	return i >= 0 && j >= 0 && i < N && j < N;
}

bool check(char z) {
	int di[4] = {1, 0, 1, -1};
	int dj[4] = {0, 1, 1, 1};
	for(int i = 0; i < N; i++) {
		for(int j = 0; j < N; j++) {
			int totals[4] = {0, 0, 0, 0};
			for(int k = 0; k < K; k++) {
				for(int l = 0; l < 4; l++) {
					int i2 = i + di[l] * k;
					int j2 = j + dj[l] * k;
					if(in_bounds(i2, j2) && b[i2][j2] == z)
						totals[l]++;
				}
			}
			for(int l = 0; l < 4; l++)
				if(totals[l] == K)
					return true;
		}
	}
	return false;
}

string solve() {
	rotate();
	fall();

	bool red = check('R');
	bool blue = check('B');

	if(!red && !blue)
		return "Neither";
	if(!red && blue)
		return "Blue";
	if(red && !blue)
		return "Red";
	return "Both";
}

int main() {
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++) {
		scanf("%d%d", &N, &K);
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				char c = ' ';
				while(c != 'B' && c != 'R' && c != '.')
					scanf("%c", &c);
				a[i][j] = c;
			}
		}
		/*
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++)
				printf("%c", a[i][j]);
			printf("\n");
		}
		printf("\n");
		rotate();
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++)
				printf("%c", b[i][j]);
			printf("\n");
		}
		printf("\n");
		fall();
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++)
				printf("%c", b[i][j]);
			printf("\n");
		}
		*/

		printf("Case #%d: %s\n", t, solve().c_str());
	}

	return 0;
}
