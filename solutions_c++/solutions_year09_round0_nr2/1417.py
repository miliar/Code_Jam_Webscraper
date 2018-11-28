/*
 * basins.cpp
 *
 *  Created on: Sep 3, 2009
 *      Author: gatanov
 */

#include <iostream>
#include <algorithm>


using namespace std;

int height[200][200];
char label[200][200];
int H,W;
char Cur;

bool sink(int i,int j) {
	return height[i][j] <= height[i + 1][j] &&
		   height[i][j] <= height[i - 1][j] &&
		   height[i][j] <= height[i][j + 1] &&
		   height[i][j] <= height[i][j - 1];
}

char mark(int i,int j) {
	if (label[i][j] != 0)
		return label[i][j];
	if (sink(i,j)) {
		label[i][j] = Cur;
		return Cur++;
	}
	int m = min(min(height[i + 1][j],height[i - 1][j]),min(height[i][j + 1],height[i][j - 1]));
	if (m == height[i - 1][j])
		return label[i][j] = mark(i-1,j);
	else if (m == height[i][j - 1])
		return label[i][j] = mark(i,j-1);
	else if (m == height[i][j + 1])
		return label[i][j] = mark(i,j + 1);
	return label[i][j] = mark(i + 1,j);
}

int main(int argc, char **argv) {

	int T;

	cin >> T;

	for (int cn = 1;cn <= T;cn++) {
		cin >> H >> W;
		for (int i = 1; i <= H; ++i) {
			for (int j = 1; j <= W; ++j) {
				cin >> height[i][j];
				label[i][j] = 0;
			}
		}
		for (int i = 0;i <= H + 1;++i)
			height[i][0] = height[i][W + 1] = 200000;
		for (int j = 0;j <= W + 1;++j)
			height[0][j] = height[H + 1][j] = 200000;
		Cur = 'a';
		for (int i = 1; i <= H; ++i) {
			for (int j = 1;j <= W;++j) {
				mark(i,j);
			}
		}
		printf("Case #%d:\n",cn);
		for (int i = 1;i <= H;i++) {
			for (int j = 1;j <= W;j++)
				cout << label[i][j] << " ";
			cout << endl;
		}
	}
	return 0;
}
