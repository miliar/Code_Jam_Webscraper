#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <functional>
#include <numeric>

using namespace std;

typedef long long ll;

#define eps 1e-10
#define inf 0x3f3f3f3f

#define fr(x,y,z) for(int(x)=(y);(x)<(z);(x)++)
#define cast(x,t) *({stringstream ss;static t __ret;ss<<x,ss>>__ret;&__ret;})

#define dbg(x) cout << #x << " == " << x << endl
#define print(x) cout << x << endl

// vars
char tab[2][110][110];
int R, N;

void process() {
	// read
	memset(tab,0,sizeof(tab));
	scanf("%d",&R);
	
	int t = 0;
	for(int i = 0; i < R; i++) {
		int x1, y1, x2, y2;
		scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
		for(int x = x1; x <= x2; x++) {
			for(int y = y1; y <= y2; y++) {
				tab[t][x][y] = 1;
			}
		}
		N = max(N, max( max(x1,x2), max(y1,y2)) );
	}
	
	// solve
	int tot = 0;
	for(;;) {
		tot++;
		bool tem = false;
		for(int x = 1; x <= N; x++) {
			for(int y = 1; y <= N; y++) {
				tab[t^1][x][y] = tab[t][x][y];
				if(tab[t][x][y] && !tab[t][x][y-1] && !tab[t][x-1][y]) { // nort && west
					tab[t^1][x][y] = 0;
				}
				else if(!tab[t][x][y] && tab[t][x][y-1] && tab[t][x-1][y]) {
					tab[t^1][x][y] = 1;
				}
				if(tab[t^1][x][y]) {
					tem = true;
				}
			}
		}
		t ^= 1;
		if(!tem) break;
	}
	
	printf("%d\n",tot);
}

int main() {

	int t;
	scanf("%d",&t);
	
	for(int i = 1; i <= t; i++) {
		printf("Case #%d: ",i);
		process();
	}
	
	return(0);
}
