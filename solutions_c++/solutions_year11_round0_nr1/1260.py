/*
ID: ahaigh1
PROG: 
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <queue>
#include <utility>
#include <memory>
#include <set>
#include <stack>
#include <string>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <limits>
#include <map>
#include <bitset>
using namespace std;

#define REP(i, n) for(int i = 0; i < n; i++)
#define CL(x) memset(x, 0, sizeof(x))
#define eps (1e-10)
#define inf (1<<30)
#define ll long long
#define MP make_pair

char col[106]; int pos[106]; int t, n;

int next_task(char colour, int index) { 
	int j = index; while (j < n && col[j] != colour) j++;
	if (j == n) return 105; // no tasks, where should we go ?
	return j;
}

int main() { 
	cin >> t;
	
	/* if (t == -1) { 
		cout << 80 << endl;
		REP(i, 20) { 
			cout << 100 << endl;
			REP(j, 100) cout << ((j<50)?"O":"B") << " " << (j%50)+1 << endl;
		}
		REP(i, 20) { 
			cout << 100 << endl;
			//cout << "O 50 B 50" << endl;
			REP(j, 50) cout << "O " << (50-j) << " B " << (50+j) << endl;
		}
		REP(i, 20) { 
			cout << 100 << endl;
			REP(j, 50) cout << "O " << 1 << " O " << 100 << endl;
		}
		REP(i, 20) { 
			cout << 100 << endl;
			REP(j, 100) cout << ((rand()%2)?"O":"B") << " " << (rand()%100)+1 << endl;
		}
		return 0;
	} */
	
	REP(i, t) { 
		cin >> n;
		REP(j, n) cin >> col[j] >> pos[j];
		pos[105] = (1<<20);
		
		int x_pos = 1, y_pos = 1, comp = 0, time = 0, j, k;
		while (comp < n) { 
			j = next_task('O', comp);
			k = next_task('B', comp);
			
			//cout << "#" << j << " " << k << endl;
		
			if (x_pos == pos[j] && y_pos == pos[k]) { 
				//who should push? whoever is next
				comp++;
				time++;
			} else if (x_pos == pos[j]) { 
				if (j == comp) comp++;
				if (y_pos < pos[k]) y_pos++; else y_pos--;
				time++;
			} else if (y_pos == pos[k]) { 
				if (k == comp) comp++;
				if (x_pos < pos[j]) x_pos++; else x_pos--;
				time++;
			} else { 
				int time_inc = min( abs(y_pos-pos[k]), abs(x_pos-pos[j]) );
				
				if ( abs(y_pos-pos[k]) <= time_inc) y_pos = pos[k];
				else if (y_pos < pos[k]) y_pos += time_inc; else y_pos -= time_inc;
				
				if ( abs(x_pos-pos[j]) <= time_inc) x_pos = pos[j];
				else if (x_pos < pos[j]) x_pos += time_inc; else x_pos -= time_inc;
				time += time_inc;
			}
			
			//cout << time << ": " << x_pos << " " << y_pos << endl;
		}
		cout << "Case #" << (i+1) << ": " << time << endl;
	}
}