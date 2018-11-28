#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector< vector<char> > solve(int h, int w, vector< vector<int> >& a)
{
	// Стоки
	vector<int> basini, basinj;
	// Соседи
	enum side { N, W, E, S }; int si[] = {-1,0,0,1}; int sj[] = {0,-1,1,0}; side r[] = {S, E, W, N};
	// Матрица направлений смежности
	vector< vector< vector<bool> > > link(h, vector< vector<bool> >(w, vector<bool>(4)));
	// Для каждой ячейки
	for (int i = 0; i < h; ++i) {
		for (int j = 0; j < w; ++j) {
			// Находим сторону, в которой высота наименьшая
			side mins = N; int mina = a[i][j], mini = i, minj = j;
			for (side s = N; s <= S; s = (side) ((int) s + 1)) {
				int ni = i + si[s], nj = j + sj[s];
				if (ni >= 0 && ni < h && nj >= 0 && nj < w) {
					if (a[ni][nj] < mina) {
						mins = s;
						mina = a[ni][nj];
						mini = ni;
						minj = nj;
					}
				}
			}
			// Если наименьшая высота у соседей меньше текущей
			if (mina < a[i][j]) {
				link[i][j][mins] = true;
				link[mini][minj][r[mins]] = true;
			} else {
				basini.push_back(i);
				basinj.push_back(j);
			}
		}
	}
	// Исходя из стоков, пронумеруем все ячейки
	vector< vector<int> > c(h, vector<int>(w, -1));
	struct dfs {
		int *si, *sj;
		dfs(int *si, int *sj) : si(si), sj(sj) {}
		void operator() (vector< vector<int> >& c, const vector< vector< vector<bool> > >& link, int h, int w, int i, int j, int num) {
		c[i][j] = num;
		for (side s = N; s <= S; s = (side) ((int) s + 1)) {
			int ni = i + si[s], nj = j + sj[s];
			if (ni >= 0 && ni < h && nj >= 0 && nj < w) {
				if (link[i][j][s] && c[i + si[s]][j + sj[s]] == -1) {
					(*this)(c, link, h, w, ni, nj, num);
				}
			}
		}
	} };

	int nbasin = (int) basini.size();
	dfs dfs_(si, sj);
	for (int i = 0; i < nbasin; ++i) {
		dfs_(c, link, h, w, basini[i], basinj[i], i);
	}

	// Перенумеруем ячейки, исходя из лексикографической минимальности ответа
	vector<char> abasin(nbasin, ' ');
	vector< vector<char> > result(h, vector<char>(w, ' '));
	int cchar = 'a';
	for (int i = 0; i < h; ++i) {
		for (int j = 0; j < w; ++j) {
			if (abasin[c[i][j]] == ' ') abasin[c[i][j]] = cchar++;
			result[i][j] = abasin[c[i][j]];
		}
	}

	return result;
}

int main()
{
	int t;
	cin >> t;
	for (int test = 0; test < t; ++test) {
		int h, w;
		cin >> h >> w;
		vector< vector<int> > a(h, vector<int>(w));
		for (int i = 0; i < h; ++i) {
			for (int j = 0; j < w; ++j) {
				int alt;
				cin >> alt;
				a[i][j] = alt;
			}
		}
		vector< vector<char> > b = solve(h, w, a);
		cout << "Case #" << (test + 1) << ":" << endl;
		for (int i = 0; i < h; ++i) {
			for (int j = 0; j < w; ++j) {
				if (j != 0) cout << " ";
				cout << b[i][j];
			}
			cout << endl;
		}
	}
}
