#include <cstdio>
#include <algorithm>
using namespace std;

const int maxn = 100;

char sold[maxn][maxn];
char snew[maxn][maxn];
char sfinal[maxn][maxn];

int n, K;
bool debug = false;


void read() {
	scanf("%d %d\n", &n, &K);
	for (int i = 0; i < n; i++) {
		gets(sold[i]);		
	}	
	if (debug)
		for (int i = 0; i < n; i++)
			printf("%s\n", sold[i]);
}

void rotate() {
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			snew[j][n-i-1] = sold[i][j];	
	if (debug) {
		printf("rotate\n");
		for (int i = 0; i < n; i++)
			printf("%s\n", snew[i]);
	}
}

void drop() {	
	for (int j = 0; j < n; j++) {
		int t = n-1;
		for (int i = n-1; i >= 0; i--) {
			if (snew[i][j] != '.')
				sfinal[t--][j] = snew[i][j];			
		}
		for (; t >= 0; t--)
			sfinal[t][j] = '.';
		
	}
	if (debug) {
		printf("drop\n");
		for (int i = 0 ; i < n; i++)
			printf("%s\n", sfinal[i]);			
	}
}

int di[4] = {1, 1, 1, 0};
int dj[4] = {-1, 0, 1, 1};

bool find(char c) {
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++) {
			for (int type = 0; type < 4; type++) {
				bool ok = true;
				for (int k = 0; k < K; k++) {
					int ni = i + di[type] * k;
					int nj = j + dj[type] * k;					
					if (!(ni >= 0 && ni < n && nj >= 0 && nj < n)) {
						ok = false;
						break;
					}
					if (sfinal[ni][nj] != c) {
						ok = false;
						break;
					}
				}
				if (ok) return true;
			}
		}			
	return false;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		read();
		rotate();		
		drop();
		bool r = find('R');
		bool b = find('B');		
		if (r && b)
			printf("Both");
		else if (r)
			printf("Red");
		else if (b)
			printf("Blue");
		else
			printf("Neither");
		printf("\n");
	}
	return 0;
}

