#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <stack>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <complex>
#include <algorithm>
#include <utility>
#include <cstring>

using namespace std;

int r;
bool bact[512][512];
const int lim = 512;

int main(){
	int ttt; cin >> ttt;
	for (int zzz = 1; zzz <= ttt; zzz++){
		memset(bact,false,sizeof(bact));
		cin >> r;
		for (int i = 0; i < r; i++){
			int x1,x2,y1,y2;
			cin >> x1 >> y1 >> x2 >> y2;
			for (int i = x1; i <= x2; i++)
				for (int j = y1; j <= y2; j++)
					bact[i][j] = true;
		}
		/*
		for (int i = 0; i < 20; i++){
			for (int j = 0; j < 20; j++){
				if (bact[i][j]) cout << "+";
				else cout << ".";
			}
			cout << endl;
		}*/
		int t = 0;
		bool finished = true;
		while(true){
			finished = true;
			for (int i = lim - 1; i > 0; i--)
				for (int j = lim - 1; j > 0; j--){
					if (bact[i][j]) {
						bact[i][j] = (bact[i-1][j] || bact[i][j-1]);
					}
					else{
						bact[i][j] = bact[i-1][j] && bact[i][j-1];
					}
					if (bact[i][j]) {
						//cout << "bacteria: t = " << t << ", i = " << i << ", j = " << j << endl;
						finished = false;
					}
				}
				/*
			if (t < 6){
			for (int i = 0; i < 20; i++){
				for (int j = 0; j < 20; j++){
					if (bact[i][j]) cout << "+";
					else cout << ".";
				}
				cout << endl;
			}
			cout << endl;
			}*/
			t++;
			if (finished) break;
		}
		cout << "Case #" << zzz << ": " << t << endl;
	}
	return 0;
}
