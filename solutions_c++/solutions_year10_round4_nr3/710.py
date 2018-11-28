#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

bool bact[102][102];
bool cct[102][102];

bool simulate(){
	memset(cct, 0, sizeof cct);
	bool ret = false;
	for (int i=0; i<=100; i++){
		for (int j=0; j<=100; j++){
			if (!bact[i][j] && i && j && bact[i-1][j] && bact[i][j-1]){
				ret = true;
				cct[i][j] = true;
			} else if (bact[i][j] && i && j && (bact[i-1][j] || bact[i][j-1])){
				ret = true;
				cct[i][j] = true;
			} else if (bact[i][j] && (!i || !j || (!bact[i-1][j] && !bact[i][j-1]))){
				ret = true;
			}
		}
	}
	memcpy(bact, cct, sizeof cct);
	return ret;
}

int main(){
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int t;
	cin >> t;
	for (int I=0; I<t; I++){
		cout << "Case #" << I+1 << ": ";
		memset(bact, 0, sizeof bact);
		int R;
		cin >> R;
		for (int i=0; i<R; i++){
			int x1, x2, y1, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			for (int y = y1; y<=y2; y++){
				for (int x = x1; x<=x2; x++){
					bact[x][y] = true;
				}
			}
		}
		int ret = 0;
		for (;simulate(); ret++){
		}
		cout << ret << endl;
	}
	return 0;
}