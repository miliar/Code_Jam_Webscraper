#include <iostream>
using namespace std;
int row(char tab[4][4],char s) {
	for (int i = 0; i < 4; ++i) {
		int s_cnt = 0, t_cnt = 0;
		for (int j=0; j<4; ++j) {
			if (tab[i][j] == s) ++s_cnt;
			if (tab[i][j] == 'T') ++t_cnt;
		}
		if (s_cnt == 4) return 1;
		else if (s_cnt == 3 && t_cnt == 1) return 1;
	}
	return 0;
}

int col(char tab[4][4],char s) {
	for (int i=0; i<4; ++i) {
		int s_cnt = 0, t_cnt = 0;
		for (int j=0; j<4; ++j) {
			if (tab[j][i] == s) ++s_cnt;
			if (tab[j][i] == 'T') ++t_cnt;
		}
		if (s_cnt == 4) return 1;
		else if (s_cnt == 3 && t_cnt == 1) return 1;
	}
	return 0;
}

int dig(char tab[4][4],char s) {
	int s_cnt = 0, t_cnt = 0;
	for (int i=0; i<4; ++i) {
		if (tab[i][i] == s) ++s_cnt;
		if (tab[i][i] == 'T') ++t_cnt;
	}
	if (s_cnt == 4) return 1;
	else if (s_cnt == 3 && t_cnt == 1) return 1;
	s_cnt = t_cnt = 0;
	for (int i=0; i<4; ++i) {
		if (tab[3-i][i] == s) ++s_cnt;
		if (tab[3-i][i] == 'T') ++t_cnt;
	}
	if (s_cnt == 4) return 1;
	else if (s_cnt == 3 && t_cnt == 1) return 1;
	return 0;
}

int dot(char tab[4][4]) {
	int d_cnt = 0;
	for (int i=0; i<4; ++i) {
		for (int j=0; j<4; ++j) {
			if (tab[i][j] == '.') d_cnt++;
		}
	}
	return d_cnt;
}
int jdg(char tab[4][4],char s) {
	return 0;
}
int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		char tab[4][4];
		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				cin >> tab[j][k];
			}
		}
		int x_won = row(tab,'X')+col(tab,'X')+dig(tab,'X');
		int o_won = row(tab,'O')+col(tab,'O')+dig(tab,'O');
		if (x_won) {
			cout << "Case #" << i+1 << ": " << "X won" << endl;
			continue;
		}
		if (o_won) {
			cout << "Case #" << i+1 << ": " << "O won" << endl;
			continue;
		}
		if (!x_won && !o_won) {
			int d_cnt = dot(tab);
			if (d_cnt == 0) {
				cout << "Case #" << i+1 << ": " << "Draw" << endl;
				continue;
			}
			else {
				cout << "Case #" << i+1 << ": " << "Game has not completed" << endl;
			}
		}
	}
	return 0;
}
