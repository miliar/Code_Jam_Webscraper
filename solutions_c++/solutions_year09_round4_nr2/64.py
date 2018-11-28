#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>

using namespace std;

#define fr(i, N) for(i = 0; i < (int)N; i++)
#define setContains(i,j) (((1<<j)&i) != 0)
#define MP make_pair
#define F first
#define S second
#define pb push_back
#define Eps 1e-11

typedef pair<int, int> pi;

int R, C, F;
int Map[60][60];
map<pair<pi, int>, int> Data[60];

void input()
{
	int i, j;
	char a;
	scanf("%d%d%d", &R, &C, &F);
	
	fr (i, R) fr (j, C) {
		scanf("%c", &a);
		if (a == '.') {
			Map[i][j] = 0;
		} else if (a == '#') {
			Map[i][j] = 1;
		} else {
			j--;
		}
	}
}

void addData(int row, pair<pi, int> info, int best) {
	if (Data[row].find(info) == Data[row].end()) {
		Data[row][info] = best;
	}

	Data[row][info] = min(best, Data[row][info]);
}

void process()
{
	int i, j, k, l, res = 300000;
	fr (i, R) Data[i].clear();

	Data[0][MP(MP(-1, -1), 0)] = 0;

	fr (i, (R-1)) {
		for (map<pair<pi, int>, int>::iterator it = Data[i].begin(); it != Data[i].end(); it++) {
			int pos = it->F.S;
			int s = it->F.F.F;
			int e = it->F.F.S;
	
			while (pos > 0 && Map[i+1][pos-1] == 1 &&
					(Map[i][pos-1] == 0 || (s <= pos-1 && pos-1 < e))) pos--;

			if (pos > 0 && Map[i+1][pos-1] == 0 &&
					(Map[i][pos-1] == 0 || (s <= pos-1 && pos-1 < e))) {
				for (k = i+1; k < R; k++) if (Map[k][pos-1] == 1) break;
				
				k--;
				if (k - i <= F) addData(k, MP(MP(-1, -1), pos-1), it->S);
			}

			int enpos = pos;
			while (enpos < C-1 && Map[i+1][enpos+1] == 1 &&
					(Map[i][enpos+1] == 0 || (s <= enpos+1 && enpos+1 < e))) enpos++;

			if (enpos - pos != 0) {
				for (j = pos; j <= enpos; j++) {
					for (l = j; l <= enpos; l++) {
						if (j > pos) {
							for (k = i+2; k < R; k++) if (Map[k][j] == 1) break;
							
							k--;

							if (k - i <= F) {
								if (k == i+1) {
									addData(k, MP(MP(j, l+1), j), it->S + (l - j + 1));
								} else {
									addData(k, MP(MP(-1, -1), j), it->S + 1);
								}
							}
						}

						if (l < enpos) {
							for (k = i+2; k < R; k++) if (Map[k][l] == 1) break;

							k--;
							if (k - i <= F) {
								if (k == i+1) {
									addData(k, MP(MP(j, l+1), l), it->S + (l-j+1));
								} else {
									addData(k, MP(MP(-1, -1), l), it->S + 1);
								}
							}
						}
					}
				}
			}

			pos = enpos;
			if (pos < C-1 && Map[i+1][pos+1] == 0 &&
					(Map[i][pos+1] == 0 || (s <= pos+1 && pos+1 < e))) {
				for (k = i+1; k < R; k++) if (Map[k][pos+1] == 1) break;
				k--;
				if (k - i <= F) addData(k, MP(MP(-1, -1), pos+1), it->S);
			}
		}
	}

	for (map<pair<pi, int>, int>::iterator it = Data[R-1].begin(); it != Data[R-1].end(); it++) {
		res = min(res, it->S);
	}
	

	if (res == 300000) {
		printf("No\n");
	} else {
		printf("Yes %d\n", res);
	}
}

int main()
{
	int t, T;
	scanf("%d", &T);

	fr(t, T)
	{
		input();
		printf("Case #%d: ", t+1);
		process();
	}
	return 0;
}

