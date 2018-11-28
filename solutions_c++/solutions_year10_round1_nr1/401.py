#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <fstream>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <limits>
#include <queue>
#include <deque>
#include <cmath>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;

#define SIZE(X) ((int)X.size())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)

typedef long long LL;
typedef pair<int,int> PII;

template<class T> void out(T A[],int n) {cout<<"{"; for (int i=0;i<n;i++){ cout<<A[i];if (i==n-1) cout<<"}"; else cout<<",";} cout<<endl;}
template<class T> void out(T A[],int n, int m) {for(int i=0;i<n;++i) out(A[i],m); cout<<endl;}\
template<class T> void out(vector<T> A,int n=-1) {if (n<0 || n>SIZE(A)) n=SIZE(A);cout<<"{";for (int i=0;i<n;i++) {cout<<A[i];if (i==n-1) cout<<"}"; else cout<<",";} cout<<endl;}

const int MAXN = 110;
const int INF = 1000000000;
const double EPS = 1e-8;
const double PI = acos(-1.0);

int T, N, K;
char mat[51][51];

int di[4] = {0, -1, 1, 1};
int dj[4] = {1, 1, 0, 1};

bool legal(int i, int j) {
	return (i >= 0 && i < N && j >= 0 && j < N);
}
bool check(char c) {
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) if (mat[i][j] == c) {
			for (int k = 0; k < 4; ++k) {
				bool flag = true;
				for (int x = 0; x < K; ++x) {
					int ii = i + di[k] * x;
					int jj = j + dj[k] * x;
					if (!legal(ii, jj) || mat[ii][jj] != c) {
						flag = false;
						break;
					}
				}
				if (flag) return true;
			}
		}
	}
	return false;
}
int main ()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas) {
		scanf("%d %d", &N, &K);
		for (int i = 0; i < N; ++i) {
			scanf("%s", mat[i]);
		}
		for (int i = 0; i < N; ++i) {
			int cnt = 0;
			for (int j = N - 1; j >= 0; --j) {
				if (mat[i][j] != '.') {
					cnt++;
					mat[i][N - cnt] = mat[i][j];
				}
			}
			for (int j = 0; j < N - cnt; ++j)
				mat[i][j] = '.';
		}
		bool flag1 = check('R');
		bool flag2 = check('B');
		printf("Case #%d: ", cas);
		if (flag1 && flag2) {
			puts("Both");
		} else if (flag1) {
			puts("Red");
		} else if (flag2) {
			puts("Blue");
		} else {
			puts("Neither");
		}
	}
	return 0;
}