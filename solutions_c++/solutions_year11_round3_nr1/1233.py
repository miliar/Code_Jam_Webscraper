#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <stack>
using namespace std;

char str[55][55];

bool f(int x, int y, int n, int m){
	if (x >= 0 && x < n && y >= 0 && y < m){
		if (str[x][y] == '#')
			return true;
	}
		
	return false;
}

int main(){

	freopen("A-small-attempt2.in", "r", stdin);
	freopen("Aout.txt", "w", stdout);
	int T;
	int cas = 1;
	int n, m;

	scanf("%d", &T);
	while (T--){
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++){
			scanf("%s", str[i]);
		}

		for (int i = 0; i < n; i++){
			for (int j = 0; j < m; j++){
				if (str[i][j] == '#'){
					if (f(i, j, n, m) && f(i, j+1, n, m) && f(i+1, j, n, m) && f(i+1, j+1, n, m)){
						str[i][j] = '/';
						str[i][j+1] = '\\';
						str[i+1][j] = '\\';
						str[i+1][j+1] = '/';
					}
				}
			}
		}
		bool flag = true;
		for (int i = 0; i < n; i++){
			for (int j = 0; j < m; j++){
				if (str[i][j] == '#'){
					flag = false;
				}
			}
		}
		printf("Case #%d:\n", cas++);
		if (flag == false)
			printf("Impossible\n");
		else{
			for (int i = 0; i < n; i++)
				printf("%s\n", str[i]);
		}
	}
	
	return 0;
}