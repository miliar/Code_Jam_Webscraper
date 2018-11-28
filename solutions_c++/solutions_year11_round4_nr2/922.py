#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <numeric>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define eps 1e-10
#define inf 0x3f3f3f3f

#define console cout
#define dbg(x) console << #x << " == " << x << endl
#define print(x) console << x << endl

int R, C, D;
char mat[501][501];
int m[501][501];
double accX[501][501], accY[501][501], sum[501][501];
double line[501][501];
int read(){
	cin >> R >> C >> D;
	for(int i = 0; i < R; i++){
		scanf("%s", mat[i]);
		for(int j = 0; j < C; j++){
			m[i][j] = mat[i][j]-'0' + D;
			accX[i][j]=accY[i][j]=sum[i][j]=0.0;
		}
	}
	return 1;
}
void process(){
	for(int i = 0; i < R; i++){
		for(int j = 0; j < C; j++){
			sum[i][j] = m[i][j];
			accX[i][j] = j*m[i][j];
			accY[i][j] = i*m[i][j];
			if(j){
				sum[i][j] += sum[i][j-1];
				accX[i][j] += accX[i][j-1];
				accY[i][j] += accY[i][j-1];
			}
		}
	}
	for(int i = 1; i < R; i++){
		for(int j = 0; j < C; j++){
			sum[i][j] += sum[i-1][j];
			accX[i][j] += accX[i-1][j];
			accY[i][j] += accY[i-1][j];
		}
	}
	int melhor = 0;
	for(int k = 3; k <= min(R,C); k++){
	//	dbg(k);
		for(int i = 0; i+k-1 < R; i++){
			for(int j = 0; j+k-1 < C; j++){
				long long M = sum[i+k-1][j+k-1];
				if(i)M -= sum[i-1][j+k-1];
				if(j)M -= sum[i+k-1][j-1];
				if(i && j)M += sum[i-1][j-1];
				M -= m[i][j]+m[i][j+k-1]+m[i+k-1][j]+m[i+k-1][j+k-1];
				double sumX = accX[i+k-1][j+k-1];
				if(i)sumX -= accX[i-1][j+k-1];
				if(j)sumX -= accX[i+k-1][j-1];
				if(i && j)sumX += accX[i-1][j-1];
				sumX-=m[i][j]*j + m[i][j+k-1]*(j+k-1)+m[i+k-1][j]*(j)+m[i+k-1][j+k-1]*(j+k-1);
				
				double sumY = accY[i+k-1][j+k-1];
				if(i)sumY -= accY[i-1][j+k-1];
				if(j)sumY -= accY[i+k-1][j-1];
				if(i && j)sumY += accY[i-1][j-1];
				sumY-=m[i][j]*i + m[i+k-1][j]*(i+k-1)+m[i][j+k-1]*(i)+m[i+k-1][j+k-1]*(i+k-1);
				double mX = sumX/(M), mY = sumY/(M);
					if(fabs(mX-(2*j+k-1)/2.0) < 1e-5 && fabs(mY-(2*i+k-1)/2.0) < 1e-5){
						melhor = max(melhor, k);
					}
				
			}
		}
	}
	if(melhor == 0)printf("IMPOSSIBLE\n");
	else printf("%d\n", melhor);
}

// BEGIN CUT HERE
int main() {
//freopen("out.txt","w",stdout);
//freopen("out.txt","w",stderr);
	int casos;
	scanf("%d", &casos);
	for(int i = 1; i <= casos && read(); i++){
		fprintf(stderr, "i(%d)\n", i);
		printf("Case #%d: ", i);
		process();
	}
	return 0;
}
// END CUT HERE 
