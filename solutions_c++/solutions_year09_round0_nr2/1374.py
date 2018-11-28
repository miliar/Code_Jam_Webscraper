#include <iostream>
#include <fstream>
#include <vector>
#define MAX 101
using namespace std;

ifstream fin("watersheds2.in");
ofstream fout("watersheds2.out");

const int h[] = {-1, 0, 0, 1};
const int c[] = {0, -1, 1, 0};

struct POINT {
	int x, y;
	POINT() {
	}
	POINT(int _x, int _y) {
		x = _x;
		y = _y;
	}
};

int m, n;
int a[MAX][MAX];

void BFS() {
}

void process(int test) {
	char d[MAX][MAX];
	for (int i=0; i<MAX; i++)
		for (int j=0; j<MAX; j++) d[i][j] = 0;
	char currentCh = int('a') - 1;
	for (int i=1; i<=m; i++)
		for (int j=1; j<=n; j++)
			if (d[i][j] == 0) {
				int x = i;
				int y = j;
				vector<POINT> stack;
				stack.clear();
				bool found = true;
				while (found) {
					POINT p(x, y);
					stack.push_back(p);
					found = false;
					int rx, ry, minv = INT_MAX;
					for (int k=0; k<4; k++) {
						int xx = x + h[k];
						int yy = y + c[k];
						if (xx < 1 || xx > m || yy < 1 || yy > n) continue;
						if (a[xx][yy] < a[x][y] && a[xx][yy] < minv) {
							minv = a[xx][yy];
							rx = xx;
							ry = yy;
						}
					}
					if (minv == INT_MAX) {
						currentCh ++;
						for (int ii=0; ii<stack.size(); ii++) {
							d[stack[ii].x][stack[ii].y] = currentCh;
						}
						break;
					}
					if (d[rx][ry] != 0) {
						for (int ii=0; ii<stack.size(); ii++) {
							d[stack[ii].x][stack[ii].y] = d[rx][ry];
						}
						break;
					}
					found = true;
					x = rx; y = ry;
				}
			}
			
	fout << "Case #" << test << ":" << endl;
	for (int i=1; i<=m; i++) {
		for (int j=1; j<=n; j++) {
			fout << d[i][j] <<" ";
		}
		fout << endl;
	}
}

int main()
{
	int numOfTest;
	fin >> numOfTest;
	for (int test = 1; test <= numOfTest; test++) {
		fin >> m >> n;
		for (int i=1; i<=m; i++)
			for (int j=1; j<=n; j++) fin >> a[i][j];
		process( test );	
	}
	
		
	fin.close();
	fout.close();
}
