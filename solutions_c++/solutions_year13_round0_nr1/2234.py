#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <iostream>
#include <climits>
#include <cstring>
using namespace std;

#define forn(a, n) for(int a = 0; a<(n); ++a)
#define forsn(a,s,n) for(int a = (s); a<(n); ++a)
#define forall(a, all) for(typeof((all).begin()) a = (all).begin(); a != (all).end(); ++a)

#define dforn(a, n) for(int a = (n)-1; a>=0; --a)
#define dforsn(a,s,n) for(int a = (n)-1; a>=(s); --a)
#define dforall(a, all) for(typeof((all).rbegin()) a = (all).rbegin(); a != (all).rend(); ++a)

#define contains(mask, bit) ((mask & (1LL<<bit)) != 0LL)

typedef long long tint;

const int DX[4] = {0,1,1,-1};
const int DY[4] = {1,0,1,1};

string mapa[4];

bool gana(char c){
	forn(i,4) forn(j,4) forn(k,4){
		int match = 0, x = i, y = j;
		
		while(min(x,y) >= 0 && max(x,y) < 4 && (mapa[x][y] == c || mapa[x][y] == 'T')){
			if(mapa[x][y] == c || mapa[x][y] == 'T') match++;
			x += DX[k]; y += DY[k];
		}
		
		if(match == 4) return true;
	}
	return false;
}

bool completo(){
	forn(i,4) forn(j,4) if(mapa[i][j] == '.')
		return false;
	return true;
}

int main()
{
#ifdef __YO__
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	
	int T;
	cin >> T;
	
	forn(t, T){
		forn(i,4) cin >> mapa[i];
		
		printf("Case #%i: ", t+1);
		if(gana('X'))
			printf("X won\n");
		else if(gana('O'))
			printf("O won\n");
		else if(completo())
			printf("Draw\n");
		else
			printf("Game has not completed\n");
		
	}

	return 0;
}
