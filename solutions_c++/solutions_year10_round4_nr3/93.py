#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <string>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cctype>

using namespace std;
typedef long long int64;
const int inf = 0x3f3f3f3f;
typedef double real;
const real eps = 1e-6;
typedef pair<int,int> pip;
#define Eo(x) { cerr << #x << " = " << (x) << endl; }

const int maxn = 128;
char a[2][maxn][maxn];

int main(){
	int T; cin >> T;
	for (int  _ = 0; _ < T; _++){
		printf("Case #%d: ",_+1);
		int r; cin >> r;
		memset(a,0,sizeof(a));
		for (int i = 0; i < r; i++){
			int x1,y1,x2,y2; cin >> x1 >> y1 >> x2 >> y2;
			if (x1 > x2) swap(x1,x2);
			if (y1 > y2) swap(y1,y2);
			for (int i = y1; i <= y2; i++)
				for (int j = x1; j <= x2; j++)
					a[0][i][j] = 1;
		}
		int cnt = 0;
		bool any = true;
		int fr = 0;
		int ba = 1;
		for (;any;cnt++){
			any = false;
			swap(fr,ba);
			memset(a[fr],0,sizeof(a[fr]));
			for (int i = 1; i < maxn; i++){
				for (int j = 1; j < maxn; j++){
					if (a[ba][i][j] == 1){
						if (!a[ba][i-1][j] && !a[ba][i][j-1]) a[fr][i][j] = 0;
						else a[fr][i][j] = 1;
					} else {
						if (a[ba][i-1][j] && a[ba][i][j-1]) a[fr][i][j] = 1;
						else a[fr][i][j] = 0;
					}
					if (a[fr][i][j]) any = true;
				}
			}
		}
		printf("%d\n",cnt);
	}
	return 0;
}

