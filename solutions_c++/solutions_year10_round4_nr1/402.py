#include <iostream>
#include <algorithm>
using namespace std;

#define MAXN 512

int N, ON;
char m[MAXN][MAXN], om[MAXN][MAXN], tmpm[MAXN][MAXN];

bool valid(int x, int y) {
	for (int i=0; i<2*N-1; i++) {
		for (int j=0; j<2*N-1; j++) {
			if (m[i][j] != ' ' && om[x+i][y+j] == ' ') return false;
		}
	}
	return true;
}

void merge(int x, int y) {
	memcpy(tmpm, om, sizeof(om));
	for (int i=0; i<2*N-1; i++) {
		for (int j=0; j<2*N-1; j++) {
			if (m[i][j] != ' ') tmpm[x+i][y+j] = m[i][j];
		}
	}
}

void print(char mm[MAXN][MAXN], int K) {
	for (int j=0; j<2*K-1; j++) {
		for (int i=0; i<2*K-1; i++) {
			cout << mm[i][j];
		}
		cout << endl;
	}
	cout << endl;
}

bool symmetric() {
	for (int i=0; i<2*ON-1; i++) {
		for (int j=0; j<2*ON-1; j++) {
			if (tmpm[i][j] != ' ' && tmpm[i][j] != '*') {
//				cout << tmpm[i][j] << ' ' << tmpm[i][2*ON-2-j] << endl;
//				cout << tmpm[i][j] << ' ' << tmpm[2*ON-2-i][j] << endl;
				if (tmpm[i][2*ON-2-j] != '*' && tmpm[i][2*ON-2-j] != tmpm[i][j]) return false;
				if (tmpm[2*ON-2-i][j] != '*' && tmpm[2*ON-2-i][j] != tmpm[i][j]) return false;
			}
		}
	}
	return true;
}

int main() {

//freopen("in.txt", "r", stdin);

int i, j, tmp1, tmp2, t, T;
bool flag;

cin >> T;

for (t=1; t<=T; t++) {

cin >> N;

memset(m, ' ', sizeof(m));
for (i=1; i<=2*N-1; i++) {
	tmp1 = min(i, 2*N-i);
	tmp2 = abs(N-i);
	for (j=0; j<tmp1; j++) {
		cin >> m[tmp2+j*2][i-1];
	}
}

ON = N; flag = true;
while (1) {
	memset(om, ' ', sizeof(m));
	for (i=1; i<=2*ON-1; i++) {
		tmp1 = min(i, 2*ON-i);
		tmp2 = abs(ON-i);
		for (j=0; j<tmp1; j++) {
			om[tmp2+j*2][i-1] = '*';
		}
	}

	for (i=0; i+2*N-1<=2*ON-1 && flag; i++) {
		for (j=0; j+2*N-1<=2*ON-1 && flag; j++) {
			if (valid(i, j)) {
				merge(i, j);
				//print(tmpm, ON);
				if (symmetric()) flag = false;
			}
		}
	}
	if (!flag) break;

	ON++;
}

cout << "Case #" << t << ": " << ON*ON - N*N << endl;

}

return 0;
}
