#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
using namespace std;
static const double EPS = 1e-10;
typedef long long ll;

int solve(int R, int C, int D, vector<vector<int> > A){
	int result = 0;
	
	for(int i = 0; i < R; i++){
		for(int j = 0; j < C; j++){
			for(int k = 3; ;k++){
				int a = i, b = i+k-1;
				int c = j, d = j+k-1;
				double cx=(double)0.5*(double)(k-1)+(double)j, cy=(double)0.5*(double)(k-1)+(double)i;
				if(a < 0 || c < 0 || b >= R || d >= C) break;
				double sumX = 0, sumY=0;
				for(int ii = a; ii <= b; ii++){
					for(int jj = c; jj <= d; jj++){
						if(ii == a && jj == c || ii == b && jj == c || ii == a && jj == d || ii == b && jj == d) continue;
						sumX += (double)A[ii][jj]*((double)ii-cy);
						sumY += (double)A[ii][jj]*((double)jj-cx);
					}
				}
				if(i == 1 && j == 1 && k == 5){
			//		cout << cx << ", " << cy << endl;
			//		cout << sumX << ", " << sumY << endl;
				}
				if(fabs(sumX) < EPS && fabs(sumY) < EPS){
					result = max(k, result);
				}
			}
		}
	}
	
	return result;
}

int main(){
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		int R, C, D;
		cin >> R >> C >> D;
		vector< vector<int> > A;
		for(int i = 0; i < R; i++){
			string s;
			cin >> s;
			vector<int> B;
			for(int j = 0; j < C; j++){
				B.push_back(s[j]-'0'+D);
			}
			A.push_back(B);
		}
		int result = solve(R, C, D, A);
		if(result == 0) cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
		else cout << "Case #" << t << ": " << result << endl;
	}
	return 0;
}
