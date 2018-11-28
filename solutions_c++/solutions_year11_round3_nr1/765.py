#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <map>
#include <algorithm>
#include <utility>
#include <cmath>

using namespace std;

char grid[100][100];
int n, m;

int main(){
	int casos; scanf("%d", &casos);
	int caso = 1;
	int sum;
	while(casos--){
		printf("Case #%d:\n", caso++);
		scanf("%d%d", &n, &m);
		for(int i = 0; i < n; ++i){
			scanf("%s", grid[i]);
		}
		for(int i = 0; i < n; ++i){
			for(int j = 0; j < m;++j){
				if(grid[i][j] == '#'){
					if(j+1 >= m || i+1 >= n) goto imp;
					if(grid[i][j] == '#' && grid[i+1][j] == '#' && grid[i][j+1] == '#' && grid[i+1][j+1] == '#') {
						
						grid[i][j] = '/';
						grid[i][j+1] = '\\';
						grid[i+1][j] = '\\';
						grid[i+1][j+1] = '/';
					}else goto imp;
				}
			}
		}
		for(int i = 0; i < n; ++i){
			printf("%s\n", grid[i]);
		}
		
		continue;
		imp:
		printf("Impossible\n");
	}
	
	return 0;
}