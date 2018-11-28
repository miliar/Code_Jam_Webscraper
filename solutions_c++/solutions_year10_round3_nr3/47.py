#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <list>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <valarray>
#include <ctime>
#include <set>
#include <sstream>

using namespace std;

typedef pair<int, int> PII;
typedef unsigned long long ULL;

const int MaxSize = 512;

int table[MaxSize][MaxSize] = {0};

void solution(int tstNum){
	int m, n;
	scanf("%d %d\n", &m, &n);
	
	for (int i = 0; i < m; i++){
		for (int j = 0 ; j < n / 4; j++){
			char c = getchar();
			if (c >= '0' && c <= '9'){
				c -= '0';
			}else{
				c -= 'A' - 10;
			}
			for (int k = 3; k >= 0; k--){
				table[i][4 * j + (3 - k)] = (c >> k) & 1;
			}
		}
		getchar();
	}
	int was[513] = {0};
	int total = n * m;
	int mn = min(n, m);
	while (true){		
		int bestSide = 0;
		PII coords;

		for (int i = 0; i <= m; i++){
			for (int j = 0; j <= n; j++){					
					bool curr = table[i][j];
					bool currx = curr;
					bool flag = true;
					int maxx = 0;
					int miny = -1;

					int side = 0;
					for (int k = i; k < m; k++){
						if (table[k][j] != currx){						
							break;
						}
						++maxx;
						if (maxx > miny && miny > 0){
							break;
						}
						curr = currx;
						int ty = 0;
						for (int f = j; f < n; f++){
							if (table[k][f] != curr){
								break;
							}
							++ty;
							curr = !curr;
						}
						miny = min(miny, ty);
						if (miny == -1){
							miny = ty;
						}
						side = max(side, min(maxx, miny));
						currx = !currx;
					}
					
					if (side > bestSide){
						bestSide = side;
						coords = PII(i, j);
					}
			}
		}

		if (bestSide == 1){
			was[1] = total;
			break;
		}
		for (int i = coords.first; i < coords.first + bestSide; i++){
			for (int j = coords.second; j < coords.second + bestSide; j++){
				table[i][j] = -1;
			}
		}
		total -= bestSide * bestSide;
		was[bestSide]++;
		if (total == 0){
			break;
		}
	}
	int cnt = 0;
	for (int i = 1; i <= MaxSize; i++){
		cnt += was[i] != 0;
	}
	fprintf(stderr, "%d\n", tstNum);
	printf("Case #%d: %d\n", tstNum + 1, cnt);
	for (int i = MaxSize; i >= 1; i--){
		if (was[i]){
			printf("%d %d\n", i, was[i]);
		}
	}
}

int main(){

	//freopen("A-small.in", "rt", stdin);
	//freopen("A-small.out", "wt", stdout);

	//freopen("A-large.in", "rt", stdin);
	//freopen("A-large.out", "wt", stdout);

	//freopen("B-small.in", "rt", stdin);
	//freopen("B-small.out", "wt", stdout);

	//freopen("B-large.in", "rt", stdin);
	//freopen("B-large.out", "wt", stdout);


	//freopen("C-small.in", "rt", stdin);
	//freopen("C-small.out", "wt", stdout);

	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "wt", stdout);

	int t = 0;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++){
		solution(tt);
	}

	return 0;
}