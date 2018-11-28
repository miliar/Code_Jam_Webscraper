#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>
#include <queue>
#include <stack>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<pii> vpii;
typedef vector<vector<pii> > vvpii;

#define forn(i, n) for(int i = 0; i < n; i++)
#define fors(i, c) for(int i = 0; i < (c).size(); i++)
#define tr(i, c) for((typeof (c).begin()) i = (c).begin(); i != (c).end(); i++)
#define all(c) (c).begin(), (c).end()

int main(){
	int C;
	cin >> C;
	forn(cc, C){
		int res = 0;
		int N, K, B, T;
		cin >> N >> K >> B >> T;
		vpii x(N);
		forn(i, N){
			cin >> x[i].first;
		}
		forn(i, N){
			cin >> x[i].second;
		}
		sort(all(x));
		int k = 0;
		int delayers = 0;
		int s = 0;
		for(int i = N-1; k < K && i >= 0; i--){
			if (B-x[i].first > x[i].second*T)
				delayers += 1;
			else{
				k += 1;
				s += delayers;
			}
		}
		if (k < K)
			cout << "Case #" << cc+1 << ": IMPOSSIBLE\n";
		else
			cout << "Case #" << cc+1 << ": " << s << endl;
	}
}