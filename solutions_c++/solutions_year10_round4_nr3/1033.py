#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <fstream>

using namespace std;


int main() 
{
    freopen("A-small.in", "r", stdin);
    ofstream fp("A-small.out");

	int cell[102][102];
	int tran[102][102];

	int M = 102;

	int T;
	scanf("%d", &T);

	for(int i = 0; i < T; i++)
	{
		memset(cell, 0, sizeof(cell));
		memset(tran, 0, sizeof(tran));
		int R;
		scanf("%d", &R);
		int X1, Y1, X2, Y2;
		for(int j = 0; j < R; j++) {
			scanf("%d%d%d%d", &X1, &Y1, &X2, &Y2);
			for(int p = X1; p <= X2; p++) {
				for(int q = Y1; q <= Y2; q++) {
					cell[p][q] = 1;
				}
			}
		}
		int res = 0;
		while(true) {
			bool mark = true;
			for(int p = 0; p < M; p++) {
				for(int q = 0; q < M; q++) {
					if(cell[p][q] == 1) {
						mark = false;
						break;
					}
				}
				if(!mark) break;
			}
			if(mark) break;
			res ++;
			memset(tran, 0, sizeof(tran));
			for(int p = 1; p < M; p++) {
				for(int q = 1; q < M; q++) {
					if(cell[p-1][q] == 1 && cell[p][q-1] == 1) {
						tran[p][q] = 1;
					}
					else if(cell[p-1][q] == 0 && cell[p][q-1] == 0) {
						tran[p][q] = 0;
					}
					else {
						tran[p][q] = cell[p][q];
					}
				}
			}
			for(int p = 1; p < M; p++) {
				for(int q = 1; q < M; q++) {
					cell[p][q] = tran[p][q];
				}
			}

		}
		fp << "Case #" << i+1 << ": " << res << endl;
	}

    fp.close();
    return 0;
}
