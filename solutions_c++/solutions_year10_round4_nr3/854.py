#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

typedef unsigned long long ULL;
bool isEmpt(bool a[102][102]){
	for (int i = 1; i <= 100; i++){
		for (int j = 1; j <= 100; j++){
			if (a[i][j] == 1)
				return false;
		}
	}
	return true;
}
int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int tests;
	scanf("%d",&tests);
	for (int test = 1; test <= tests; test++){
		int d;
		bool map[102][102] = {0};
		scanf("%d",&d);
		for (int i = 0; i < d; i++){
			int x1, x2, y1, y2;
			scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
			for (int y = y1; y <= y2; y++)
				for (int x = x1; x <= x2; x++)
					map[y][x] = 1;
		}
		int count = 0;
		bool map2[102][102] = {0};
		while (!isEmpt(map)){
			count++;
			for (int i = 1; i <= 100; i++){
				for (int j = 1; j <= 100; j++){
					if (map[i][j] == 1 && map[i-1][j] == 0 && map[i][j-1] == 0)
						map2[i][j] = 0;
					else
						if (map[i][j] == 0 && map[i-1][j] == 1 && map[i][j-1] == 1)
							map2[i][j] = 1;
						else
							map2[i][j] = map[i][j];
				}
			}
			for (int i = 1; i <= 100; i++)
				for (int j = 1; j <= 100; j++)
					map[i][j] = map2[i][j];
		}
		printf("Case #%d: %d\n",test,count);
	}
	return 0;
}