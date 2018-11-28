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


void solution(int tstNum){
	bool field[102][102] = {0};
	bool nfield[102][102] = {0};
	int r;
	scanf("%d", &r);
	for (int ti = 0; ti < r; ti++){
		int x1, x2, y1, y2;
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
		for (int i = y1; i <= y2; i++){
			for (int j = x1; j <= x2; j++){
				field[i][j] = true;
			}
		}
	}
	int t = 0;
	
	while (true){
		bool was = false;
		for (int i = 1; i < 101; i++){
			for (int j = 1; j < 101; j++){
				bool can = false;
				if (field[i][j]){
					can = (field[i - 1][j] || field[i][j - 1]);
				}else{
					can = (field[i - 1][j] && field[i][j - 1]);
				}
				
				was |= can;
				nfield[i][j] = can;
			}
		}
		++t;
		if (!was){
			break;
		}
		
		for (int i = 1; i < 101; i++){
			for (int j = 1; j < 101; j++){
				field[i][j] = nfield[i][j];
			}
		}
	}
	printf("Case #%d: %d\n", tstNum + 1, t);
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


	freopen("C-small.in", "rt", stdin);
	freopen("C-small.out", "wt", stdout);

	//freopen("C-large.in", "rt", stdin);
	//freopen("C-large.out", "wt", stdout);

	int t = 0;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++){
		solution(tt);
	}

	return 0;
}