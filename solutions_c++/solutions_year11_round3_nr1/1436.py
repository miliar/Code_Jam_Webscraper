#include <cstdio>

using namespace std; 
const int maxn = 55; 
int T, m, n; 
char g[maxn][maxn];

bool work(){
	for (int i = 0; i < m; i ++) {
		for (int j = 0; j < n; j++) {
			if (g[i][j] == '#'){
				if (i == m-1 || j == n-1) return false; 
				if (g[i+1][j] != '#' || g[i][j+1] != '#' || g[i+1][j+1] != '#') return false; 
				g[i][j] = '/';
				g[i][j+1] = '\\';
				g[i+1][j] = '\\';
				g[i+1][j+1] = '/'; 
			}
		}
	}
	return true; 
}

int main(){
	//freopen("E:\\Algorithms\\GoogleJam\\GoogleJam\\GoogleJam\\input\\A-large.in","r",stdin); 
	//freopen("E:\\Algorithms\\GoogleJam\\GoogleJam\\GoogleJam\\input\\a.out","w",stdout); 
	scanf("%ld", &T); 
	for (int cnt = 1; cnt <= T; cnt++) {
		scanf("%ld %ld\n", &m, &n);
		for (int i = 0; i < m; i++) 
			for (int j = 0; j < n; j++) {
				scanf(" %c", &(g[i][j])); 
			}
		printf("Case #%ld:\n", cnt); 
		if (work()) {
			for (int i = 0; i < m; i++) {
				for (int j = 0; j < n; j++) printf("%c", g[i][j]); 
				printf("\n"); 
			}
		} else printf("Impossible\n"); 
	}
	//fclose(stdout); 
}