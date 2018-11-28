#include <iostream>
#include <vector>
#include <map>
using namespace std;

typedef vector<vector<bool> > matrix;
typedef vector<vector<int> > tab;

struct chess {
	int x, y, size;
	chess(void) : x(),y(),size() {}
	chess(int a, int b, int c) :
		x(a), y(b), size(c) {
	}
};

matrix t, cut;
tab cost;
int n, m;

void place(int i, int j, char c) {
	int k, v, masque;
	if (c >= 'A' && c <= 'F')
		v = 10 + (int) (c - 'A');
	else
		v = (int) (c - '0');
	for (k = 0; k < 4; ++k) {
		masque = 1 << (3 - k);
		t[i][4 * j + k] = ((v & masque) == masque) ^ ((i + k) % 2 == 0);
	}
	return;
}

void update(chess & res, int i, int j) {
	if (cost[i][j] > res.size) {
		res.size = cost[i][j];
		res.x = i, res.y = j;
	}
}

void make_cut(chess & res) {
	int i = 0, j = 0;
	res.x = 0;
	res.y = 0;
	res.size = 0;
	for (i = 0; i < m; ++i) {
		cost[i][0] = cut[i][0] ? 0 : 1;
		update(res, i, 0);
	}
	for (j = 0; j < n; ++j) {
		cost[0][j] = cut[0][j] ? 0 : 1;
		update(res, 0, j);
	}
	for (i = 1; i < m; ++i) {
		for (j = 1; j < n; ++j) {
			if (cut[i][j])
				cost[i][j] = 0;
			else if (t[i][j] == t[i - 1][j] && t[i][j] == t[i][j - 1] && t[i][j] == t[i-1][j-1])
				cost[i][j] = (1 + min(cost[i-1][j-1], min(cost[i - 1][j], cost[i][j - 1])));
			else
				cost[i][j] = 1;
			update(res, i, j);
		}
	}
}

void cross_chess(chess & c) {
	int i,j;
	for (i = 0; i < c.size; ++i) {
		for (j = 0; j < c.size; ++j) {
			if (cut[c.x - i][c.y - j]) cout << "alert!" << c.x - i << "," << c.y - j << endl;
			cut[c.x - i][c.y - j] = true;
		}
	}
}

void print(matrix & r) {
	int i,j;
	for (i = 0; i < m; ++i) {
		for (j = 0; j < n; ++j) {
			cout << r[i][j];
		}
		cout << endl;
	}
	cout << endl;
}

int main(void) {
	int nt, num, i, j, count;
	chess res;
	map<int, int> e;
	map<int, int> :: reverse_iterator it;
	char c;
	for (cin >> nt, num = 1; num <= nt; ++num) {
		cin >> m >> n;
		t.resize(m, vector<bool> (n, false));
		cut.resize(m, vector<bool> (n, false));
		cost.resize(m, vector<int> (n, 0));
		for (i = 0; i < m; ++i) {
			for (j = 0; j < n / 4; ++j) {
				cin >> c;
				place(i, j, c);
			}
		}
		//print(t);
		count = 0;
		while (count < n*m) {
			make_cut(res);
			//cout << res.x << "," << res.y <<","<< res.size << endl;
			if (res.size == 1) break;
			++e[res.size];
			cross_chess(res);
			count += res.size*res.size;
			//print(cut);
		}
		if (count != n*m) e[1] = n*m - count;
		cout << "Case #" << num << ": " << e.size() << endl;
		for (it = e.rbegin(); it != e.rend(); ++it) {
			cout << it->first << " " << it->second << endl;
		}
		t.clear();
		cut.clear();
		cost.clear();
		e.clear();
	}
}
