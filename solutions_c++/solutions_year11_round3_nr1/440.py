#include <iostream>
using namespace std;

int main() {
	int ntc;

	scanf("%d", &ntc);
	
	for (int tc = 1; tc <= ntc; ++tc) {
		
		int n,m;
		scanf("%d %d", &n, &m);
		
		string str[n];
		
		for (int i = 0; i < n; ++i)
			cin >> str[i];
			
		int gogo[n][m];
		
		for (int i = 0; i < n; ++i){
			for (int j = 0; j < m; ++j){
				if (str[i][j] == '#')
					gogo[i][j] = 1;
				else
					gogo[i][j] = 0;
			}
		}
		
		bool bisa = true;
		
		for (int i = 0; i < n - 1; ++i) {
			for (int j = 0; j < m - 1; ++j) {
				if (gogo[i][j] == 1) {
					if (gogo[i + 1][j] == 1 && gogo[i + 1][j + 1] == 1 && gogo[i][j + 1] == 1) {
						gogo[i][j] = 2;
						gogo[i + 1][j] = 3;
						gogo[i][j + 1] = 4;
						gogo[i + 1][j + 1] = 5;
					} else {
						bisa = false;
						break;
					}
				}
			}
			
			if (!bisa) break;
		}
		
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				if (gogo[i][j] == 1) bisa = false;
		
		printf("Case #%d:\n", tc);
		if (!bisa) {
			printf("Impossible\n");
		} else {
			for (int i = 0; i < n; ++i) {
				for (int j = 0; j < m; ++j) {
					if (gogo[i][j] == 0)
						printf(".");
					else if (gogo[i][j] == 2 || gogo[i][j] == 5 )
						printf("/");
					else if (gogo[i][j] == 3 || gogo[i][j] == 4 )
						printf("\\");
				}
				printf("\n");
			}
		}
	}
	return 0;
}
