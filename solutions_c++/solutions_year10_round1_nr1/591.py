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
#define MAXN 55
char tab[MAXN][MAXN], ntab[MAXN][MAXN];
int N, K;

bool check(char c, int px, int py) {
	
	bool ok = false;
	
	for(int vx = -1; vx <= +1; vx++) {
		for(int vy = -1; vy <= +1; vy++) {
			if(vx == 0 && vy == 0) continue;
			
			int ct = 0;
			int x = px, y = py;
			while( (0 <= x && x < N) && (0 <= y && y < N) && ntab[x][y] == c) {
				ct++;
				x += vx;
				y += vy;
			}
			
			if(ct >= K) {
				ok = true;
			}
			
		}
	}
	
	return ok;
	
}

bool check(char c) {
		
	for(int i = 0; i < N; i++) {
		for(int j = 0; j < N; j++) {
			if( check(c, i, j) ) {
				return true;
			}
		}
	}
	
	return false;
}

void process() {
	// read
	scanf("%d %d",&N,&K);
	for(int i = 0; i < N; i++) {
		scanf("%s",tab[i]);
	}
	
	memset(ntab,0,sizeof(ntab));
	// solve
	int C = N-1;
	for(int i = 0; i < N; i++) {
		int L = 0;
		for(int j = 0; j < N; j++) {
			ntab[L][C] = tab[i][j];
			L++;
		}
		C--;
	}
	
	/*for(int i = 0; i < N; i++) {
		for(int j = 0; j < N; j++) {
			printf("%c",ntab[i][j]);
		}
		printf("\n");
	}*/
	
	// gravidade
	for(int k = 0; k < N*N; k++) {
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				if(ntab[i][j] != '.' && ntab[i+1][j] == '.') {
					swap(ntab[i][j],ntab[i+1][j]);
				}
			}
		}
	}
	
	/*for(int i = 0; i < N; i++) {
		for(int j = 0; j < N; j++) {
			printf("%c",ntab[i][j]);
		}
		printf("\n");
	}*/
	
	bool R = check('R'), B = check('B');
	
	if( R && B ) {
		printf("Both\n");
	}
	else if(R) {
		printf("Red\n");
	}
	else if(B) {
		printf("Blue\n");
	}
	else {
		printf("Neither\n");
	}
	
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
