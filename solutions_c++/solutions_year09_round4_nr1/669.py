
#include <iostream>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

typedef vector<int> vi; 
typedef vector<string> vs;
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define rep(i, n) for(int i = 0; i < n; ++i) 
#define foreach(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it) 
#define INT_INF 0x3F3F3F3F
#define TRACE(x...) x
#define watch(x) TRACE(cout << #x" = " << x << endl)

string itos(int x) { stringstream ss; ss << x; return ss.str(); }
vector<string> split(string s) { vector<string> r; string t; stringstream ss(s); while(ss >> t) r.push_back(t); return r; }

int mat[50];

int main() {
	int T;
	scanf("%d", &T);
	char buf[100];
	rep(t,T) {
		int N;
		scanf("%d", &N);
		
		memset(mat, 0, sizeof(mat));

		rep(i,N) {
			scanf("%s", buf);
			rep(j,N) {
				if (buf[j] == '1') mat[i] = j;
			}
		}
		
		int res = 0;

		rep(i, N) {
			for (int j = i; j < N; j++) {
				if (mat[j] <= i) {
					for (int k = j; k > i; k--) {
						int aux = mat[k];
						mat[k] = mat[k-1];
						mat[k-1] = aux;
						res++;
					}
					
					break;
				}
			}
		}
		
		printf("Case #%d: %d\n", t+1, res);
	}

	return 0;
}

