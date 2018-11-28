#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
#include <queue> 
#include <cstring> 
using namespace std;

int G[1000][1000], H[1000][1000];
int off = 500;

int main(){
	int T, ca=0;
	scanf("%d", &T);
	while (T--){
		printf("Case #%d: ", ++ca);
		int R, res=0;
		scanf("%d", &R);
		for (int i = 0 ; i < R; ++i){
			int x1, x2, y1, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (int j = x1 ; j <= x2; ++j)
				for (int k = y1; k <= y2; ++k)
					G[j+off][k+off] = 1;
		}
		while (1){
			bool ok = 1;
			for (int i = -100 ; ok && i < 200; ++i)
				for (int j = -100; ok && j < 200; ++j)
					ok &= !G[i+off][j+off];
			if (ok) break;
			res++;
			for (int i = -100; i < 200; ++i)
				for (int j = -100; j < 200; ++j){
					H[i+off][j+off] = G[i+off][j+off];
					int x = i+off, y = j+off;
					if (H[x][y] && (!G[x][y-1] && !G[x-1][y])) H[x][y] = 0;
					else
						if (!H[x][y] && (G[x][y-1] && G[x-1][y])) H[x][y] = 1;
				}
			for (int i = -100; i < 200; ++i)
				for (int j = -100; j < 200; ++j)
					G[i+off][j+off] = H[i+off][j+off];
		}
		printf("%d\n", res);
	}
	return 0;
}
