#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, N;
	cin >> T;
	for (int t = 1; t <= T; t++){
		cin >> N;
		int o = 1,  b = 1, cur = 0;
		int ot = 0, bt = 0;
		while( N-- ){
			string C;
			int P, temp;
			cin >> C >> P;
			if( C == "O" ){
				temp = abs(P - o) + 1;
				o = P;
				ot = max(ot + temp, cur + 1);
				cur = ot;
			}
			else{
				temp = abs(P - b) + 1;
				b = P;
				bt = max(bt + temp, cur + 1);
				cur = bt;
			}
		}
		cout << "Case #" << t << ": " << cur << endl;
	}
	return 0;
}
