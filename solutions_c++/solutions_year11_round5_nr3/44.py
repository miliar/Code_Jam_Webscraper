#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

#define EPS 1e-8
#define MOD 1000003

int T;

char buf[205][205];

int R, C, ret;
int A[20005][650];
bool b[105];
int per = 0;

int solve(){
	int ret = 0;
	for (int i=0; i<per; i++){
		int pos = 0;
		for (int j=0; j<(per+31); j++){
			if (A[i][j]){
				for (int k=0; k<32; k++){
					if (A[i][j] & (1<<k)){
						pos = j*32 + k;
						break;
					}
				}
				break;
			}
		}
		for (int j=i+1; j<per; j++){
			if (A[j][pos/32] & (1<<(pos%32))){
				for (int k=pos/32; k<(per+31)/32; k++){
					A[j][k] ^= A[i][k];
				}
				b[j] ^= b[i];
			}
		}
	}
	for (int i=0; i<per; i++){
		bool good = true;
		for (int j=0; j<(per+31)/32; j++){
			if (A[i][j] != 0){
				good = false;
				break;
			}
		}
		if (good && b[i]){
			return -1;
		} else if (good){
			ret++;
		}
	}
	return ret;
}

int main(){
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	cin >> T;
	for (int I=0; I<T; I++){
		cout << "Case #" << I+1 << ": ";
		cin >> R >> C;
		for (int i=0; i<R; i++){
			cin >> buf[i];
		}
		memset(A, 0, sizeof A);
		per = 0;
		for (int i=0; i<R; i++){
			for (int j=0; j<C; j++){
				for (int mask=0; mask<2; mask++){
					int nx, ny;
					if (buf[i][j] == '|'){
						if (mask & 1){
							nx = (R + i - 1) % R;
							ny = j;
						} else {
							nx = (R + i + 1) % R;
							ny = j;
						}
					} else if (buf[i][j] == '\\'){
						if (mask & 1){
							nx = (R + i - 1) % R;
							ny = (C + j - 1) % C;
						} else {
							nx = (R + i + 1) % R;
							ny = (C + j + 1) % C;
						}
					} else if (buf[i][j] == '/'){
						if (mask & 1){
							nx = (R + i - 1) % R;
							ny = (C + j + 1) % C;
						} else {
							nx = (R + i + 1) % R;
							ny = (C + j - 1) % C;
						}
					} else if (buf[i][j] == '-'){
						if (mask & 1){
							nx = i;
							ny = (C + j - 1) % C;
						} else {
							nx = i;
							ny = (C + j + 1) % C;
						}
					}
					A[nx*C + ny][per/32] |= 1<<(per % 32);
					b[per] = 1;
					per++;
				}
			}
		}
		for (int i=0; i<per; i++){
			A[R*C+i/2][i/32] |= 1<<(i % 32);
			b[R*C+i/2] = 1;
		}
		int val = solve();
		if (val == -1){
			ret = 0;
		} else {
			ret = 1;
			for (int i=0; i<val; i++){
				ret = (ret * 2) % MOD;
			}
		}
		cout << ret << endl;
	}
	return 0;
}