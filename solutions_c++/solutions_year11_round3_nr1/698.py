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
#include <assert.h>
#include <hash_map>
#define rep(x,n) for(int x=0;x<n;x++)
#define mem(a, b) memset(a, b, sizeof(a))
#define mp(x,y) make_pair(x,y)
#define getBit(code, i) (code & (1 << i))
#define setBit(code, i) (code | (1 << i))
#define resetBit(code, i) (code & ~(1 << i))
#define PI acos(-1.0)
using namespace std;
using namespace  stdext;


void gcjSolve()
{
	int r, c;
	char grid[70][70];
	cin >> r >> c;
	rep(i, r) rep(j, c) cin >> grid[i][j];

	rep(i, r){
		rep(j, c){
			if(grid[i][j] == '#' && grid[i][j+1] == '#' && grid[i+1][j] == '#' && grid[i+1][j+1] == '#'){
				grid[i][j] = grid[i+1][j+1] = '/';
				grid[i][j+1] = grid[i+1][j] = '\\';
			}
		}
	}

	bool f = true;
	rep(i, r){
		rep(j, c){
			if(grid[i][j] == '#')
			{
				f = false;
				break;;
			}
		}
	}

	if(!f)
		printf("Impossible\n");
	else
		rep(i, r){
			rep(j, c){
				cout << grid[i][j];
			}
			cout << endl;
	}
}

int main(){

	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	
	int t;
	cin >> t;
	rep(kase, t){
		printf("Case #%d:\n", kase + 1);
		gcjSolve();
	}
	return 0;
}