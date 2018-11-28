#include <iostream>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <vector>

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i < int(n); i++)
#define mp(a, b) make_pair(a, b);
#define X first
#define Y second
#define pb(a) push_back(a)
#define sz(a) a.size()

using namespace std;

typedef long long li;
typedef pair<int, int> pt;

string a[100];
int b[100];
int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int n, t;
	cin >> t;
	forn(x, t){
		cin >> n;
		forn(i, n){
			b[i] = 0;
			cin >> a[i];
			forn(j, a[i].size())
				if (a[i][j] == '1')
					b[i] = max(b[i], j);

		}
		int ans = 0;
		bool fl = true;
		forn(j, n){
			forn(i, n - 1){
				if (b[i] > i&& b[i + 1] < b[i] && b[i + 1] <= i){
					swap(b[i], b[i + 1]);
					ans++;
				}
				else{
					if (b[i] > i){
						for(int k = i + 1; k < n; k++){
							if (b[k] <= i){
								for(int i1 = k; i1 >= i + 1; i1--){
									swap(b[i1], b[i1-1]);
									ans++;
								}
								break;
									
							}
						}
					}
				}
			}
		}
		cout << "Case #" << x + 1 << ": " << ans << endl;
	}
	return 0;
}