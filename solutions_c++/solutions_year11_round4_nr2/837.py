
#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <queue>
#include <set>
#include <cstring>
#include <sstream>
#include <cassert>
#include <map>
#include <stack>

#define FOR(I,A,B) for(int I=(A);I<(B);I++)
#define REP(I,N) FOR(I,0,N)
#define ALL(A) (A).begin(),(A).end()

#define SQR(x) ((x)*(x))
#define PB(x) push_back(x)

#define PI (acos(-1.0))

using namespace std;

typedef vector<int> VI;
typedef vector< vector<int> > VVI;

int R,C,D;
int sheet[500][500];

bool check(int K) {
	double center = (double) (K-1) / 2;
	REP(i,R-K+1) {
		REP(j,C-K+1) {
			double x = 0;
			double y = 0;

			REP(i2,K) {
				REP(j2,K) {
					if(i2 == 0 && j2 == 0) continue;
					if(i2 == K-1 && j2 == 0) continue;
					if(i2 == 0 && j2 == K-1) continue;
					if(i2 == K-1 && j2 == K-1) continue;
					x += (center - j2) * sheet[i+i2][j+j2];
					y += (center - i2) * sheet[i+i2][j+j2];
				}
			}
			if(abs(x) > 1e-9) continue;
			if(abs(y) > 1e-9) continue;
//			cout << "K : " <<K<<endl;
//			cout << "i = "<<i<<" ,  j = "<< j<<endl;
			return true;
		}
	}
	return false;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int testcase;
	cin >>testcase;
	for(int tc=1;tc<=testcase;tc++) {
		cin >>R>>C>>D;
		REP(i,R) {
			string str;
			cin >> str;
			REP(j,C) {
				sheet[i][j] = D + str[j]-'0';
			}
		}

		int result = -1;
		for(int i = 500;i>=3;i--) {
			if(check(i)){
			       	result = i;
				break;
			}
		}
		if(result == -1) printf("Case #%d: IMPOSSIBLE\n",tc);
		else printf("Case #%d: %d\n",tc,result);

		

		


	}
}
