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

vector<int> robots[2];
int order[104];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int T;
	cin >> T;
	
	forn(p, T){
		int n;
		cin >> n;
		robots[0].clear(); robots[1].clear();
		forn(i, n){
			char let; int num;
			cin >> let >> num;
			
			if(let == 'O')
				order[i] = 0;
			else
				order[i] = 1;
			robots[order[i]].push_back(num);
		}
		robots[0].push_back(-INT_MAX);
		robots[1].push_back(-INT_MAX);
		
		int go = 0, index[2], pos[2];
		index[0] = index[1] = 0;
		pos[0] = pos[1] = 1;
		
		int r = order[go];
		
		forsn(time, 1, INT_MAX){
/*			cout << time << endl;
			cout << go << endl;
			cout << pos[0] << " " << pos[1] << endl;
			cout << robots[0][index[0]] << " " << robots[1][index[1]] << endl << endl;;*/
			if(robots[r][index[r]] == pos[r]){
				go++;
				index[r]++;
				if(go == n){
					printf("Case #%i: %i\n", p+1, time);
					break;
				}
				
				int mov = !r;
				r = order[go];
				
				if(r == mov && robots[r][index[r]] == pos[r]){
					continue;
				}else
					pos[mov] += (robots[mov][index[mov]] > pos[mov] ? 1 : -1);
			}else{
				int diff = INT_MAX;
				forn(i, 2)
					if(robots[i][index[i]] != -INT_MAX && (r == i && robots[i][index[i]] != pos[i]))
						diff = min(diff, abs(robots[i][index[i]] - pos[i]));
				if(diff == INT_MAX) continue;
				
				forn(i, 2)
					if(robots[i][index[i]] != pos[i]){
						if(abs(robots[i][index[i]]-pos[i]) < diff)
							pos[i] = robots[i][index[i]];
						else
							pos[i] += diff * (robots[i][index[i]] > pos[i] ? 1 : -1);
					}
				time += diff-1;
			}
		}
	}

	return 0;
}
