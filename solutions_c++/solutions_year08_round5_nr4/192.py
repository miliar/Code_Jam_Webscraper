#include <iostream>
using namespace std;

bool e[101][101];
int y[101][101];

int main()
{
    int N; cin >> N;
    for (int X = 1; X <= N; ++X) {
	int w, h, r; cin >> w >> h >> r;
	for (int i = 1; i <= w; ++i)
	    for (int j = 1; j <= h; ++j)
		e[i][j] = false;
	while (r--) {
	    int i, j;
	    cin >> i >> j;
	    e[i][j] = true;
	}
	for (int i = 1; i <= w; ++i)
	    for (int j = 1; j <= h; ++j) {
		if (i == 1 && j == 1)
		    y[i][j] = 1;
		else {
		    y[i][j] = 0;
		    if (i > 2 && j > 1 && !e[i-2][j-1])
			y[i][j] += y[i-2][j-1];
		    if (j > 2 && i > 1 && !e[i-1][j-2])
			y[i][j] += y[i-1][j-2];
		    y[i][j] %= 10007;
		}
	    }
	cout << "Case #" << X << ": " << (e[w][h] ? 0 : y[w][h]) << endl;
    }
}
