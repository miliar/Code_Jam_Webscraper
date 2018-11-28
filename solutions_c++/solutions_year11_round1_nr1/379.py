#include <iostream>
#include <cmath>
#include <ctime>
#include <cassert>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <vector>
#include <stack>

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define X first
#define Y second
#define sz(a) (int)a.size()

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

li n;
int px, py;

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int tests;
	cin >> tests;
	bool was = false;
	forn(test, tests){
		cin >> n >> px >> py;
		li x, y;
		bool good = false, was = false;
		/*forn(x, 200)
			forn(y, 20000){
				if(x > 0 && x <= n && (x * px) % 100 == 0 && ((x + y) * py) % 100 == 0){
				if(x > 0 && x <= n && (x * px) % 100 == 0 && ((x + y) * py) % 100 == 0 && py * (x + y) - px * x <= y * 100 && py * (x + y) - px * x >= 0){
					good = true;			
				}
				}
		}
		*/
		forn(i, 100)
			forn(j, 100){
				if((i * px) % 100 == 0 && ((i + j) * py) % 100 == 0){
					x = i;
					if(x == 0)
						x += 100;
					if(x <= n){
						y = j + li(1e15);
						if(py * x - px * x <= (100 - py) * y && py * x - px * x >= -py * y)
							was = true;
					}
				}
		}
		//assert(was == good);
		if(was)
			printf("Case #%d: Possible\n", test + 1);
		else
			printf("Case #%d: Broken\n", test + 1);
		
	}
	return 0;
}