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

int t, n, hi[16], arr[16], it;

bool bt(int pos){
	if(pos == -1) return true;
	if(it == 2000000) return false;
	it++;
	dforn(k, 60){
		arr[pos] = k;
		bool p = true;
		forsn(i, pos, n-1){
			double del = 0; int ind = -1;
//			if(i == 0){
//				cout << endl;
//				forn(k, n) cout << arr[k] << " ";
//				cout << endl;
//			}
			forsn(j, i+1, n){
				int h = arr[j]-arr[i];
				if(h < 0) continue;
				double delt = double(h) / double(j-i);
//				if(i == 0){
//					cout << j << " " << delt << endl;
//				}
				if(delt > del){
					del = delt;
					ind = j;
				}
			}
			
//			if(i == 0)
//				cout << "Aba " << ind << " " << hi[i] << endl;
			if(ind != hi[i]){
				p = false;
				break;
			}
		}
		if(p && bt(pos-1))
			return true;
	}
	
	return false;
}

int main()
{
#ifdef __YO__
	freopen("C-small.in", "r", stdin);
	freopen("C-small2.out", "w", stdout);
#endif
	
	cin >> t;
	forn(T, t){
		cin >> n;
		forn(i,n-1) cin >> hi[i];
		forn(i,n-1) hi[i]--;
		
		cerr << T << endl;
		it = 0;
		
		cout << "Case #" << T+1 << ":";
		if(!bt(n-1))
			cout << " Impossible" << endl;
		else{
			forn(i,n){
				cout << " " << arr[i];
			}
			cout << endl;
		}
	}

	return 0;
}
