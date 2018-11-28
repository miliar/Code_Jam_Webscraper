#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <set>
#include <map>
#include <algorithm>

#define FOR(i, a, b) for(int i = int(a); i < int(b); i++)
#define INF 2000000000
#define EPS 1e-9
#define PB push_back
#define MP make_pair
#define F first
#define S second
using namespace std;

typedef long long ll;
typedef pair <int, int> ii;

int main() {
	int T;
	scanf("%d", &T);
	
	for(int tc = 1; tc <= T; ++tc) {
		int r, c;
		scanf("%d%d", &r, &c);
		
		char mat[55][55];
		for(int i = 0; i < r; ++i) scanf("%s", &mat[i]);
		
		bool valid = 1;
		for(int i = 0; i < r; ++i)
			for(int j = 0; j < c; ++j) {
				if(mat[i][j] != '#') continue;
				if(i + 1 >= r || j + 1 >= c) valid = 0;
				char a = mat[i][j+1], b = mat[i+1][j], c = mat[i+1][j+1];
				if(a != '#' || b != '#' || c != '#') valid = 0;
				mat[i][j] = mat[i+1][j+1] = '/';
				mat[i][j+1] = mat[i+1][j] = '\\';
			}	
			
		printf("Case #%d:\n", tc);
		if(valid) for(int i = 0; i < r; ++i) {
			printf("%s\n", mat[i]);
		}
		else printf("Impossible\n");
	}
	
	return 0;
	}
