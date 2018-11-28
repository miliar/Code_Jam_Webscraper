#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <stack>
#include <sstream>
#include <cmath>
#include <map>

using namespace std;

int dx[4] = {0, 1, 1, 1};
int dy[4] = {-1, -1, 0, 1};

int main(void){
	int T;
	cin >> T;
	for(int cas=1; cas <= T; cas++){
	int n,K;
	cin >> n >> K;
	vector<string> b(n);
	for(int i = 0; i < n; i++) cin >> b[i];
	//for(int i = 0; i < n; i++) cout << b[i] << endl;
	for(int i = n-1; i>=0; i--){
		for(int j = n-1; j >=0; j--){
			if(b[i][j] != '.') continue;
			for(int k = j-1; k >=0; k--) {
				if(b[i][k] != '.'){
					char c = b[i][k];
					b[i][k] = b[i][j];
					b[i][j] = c;
					break;
				}
			}
		}
	}
	//for(int i = 0; i < n; i++) cout << b[i] << endl;
	bool foi[256];

	memset(foi, 0, sizeof(foi));
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++){
			if(b[i][j] != '.'){
				for(int k = 0; k < 4; k++){
					bool f = true;
					//printf("From (%d, %d)\n", i, j);
					for(int p = 1; p <= K-1; p++){
						int nx = j + p*dx[k];
						int ny = i + p*dy[k];
						//printf("Testing %d %d\n", ny,nx);
						if(nx < 0 || ny < 0 || nx >= n || ny >=n){
							//printf("Fail 1\n");
							f = false; break;
						}
						if(b[ny][nx] != b[i][j]){
							//printf("Fail 2\n");
							f = false; break;
						}
					}
					//printf("%s\n", f ? "OK" : "FALSE");
					foi[b[i][j]] = foi[b[i][j]] || f;
				}
			}
		}
	}
	//printf("R=%d, B=%d\n",foi['R'], foi['B']);
	printf("Case #%d: %s\n", cas, (foi['R'] && foi['B']) ? "Both" : foi['R'] ? "Red" : foi['B'] ? "Blue" : "Neither" );
	}
	return 0;

}
