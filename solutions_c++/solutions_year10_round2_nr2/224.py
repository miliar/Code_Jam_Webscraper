#include<iostream>
#include<algorithm>
#include<math.h>
#include<vector>
#include<set>
#include<list>
#include<map>
#include<deque>
#include<stack>
#include<queue>
#include<string>
#include<sstream>
#include<time.h>
#include<numeric>
#include<functional>

using namespace std;
#define INF  ((1 << 31) - 1)
#define eps 1e-9
#define PI 3.14159265358979323846
#define sz(v) ((int)(v).size())
#define MP make_pair
#define all(v) (v).begin(), (v).end()
typedef long long ll;

bool cut(string &s){
	int i;
	for (i = s.size() - 1; i >= 0; --i){
		if (s[i] == '/') break;
	}
	if (i == 0) return false;
	s = s.substr(0,i);
	return true;
} 
int main(){
	freopen("B-large.in", "r", stdin);
	freopen("largeout.txt", "w", stdout);
	int C;
	cin >> C;
	for (int it = 1; it <= C; ++it){
		ll n, k, b, t, tmp;
		cin >> n >> k >> b >> t;
		vector<ll> coor;
		for (int i = 0; i < n; ++i){
			scanf("%lld", &tmp);
			coor.push_back(tmp);
		}
		vector<ll> speed;
		for (int i = 0; i < n; ++i){
			scanf("%lld", &tmp);
			speed.push_back(tmp);
		}
		ll slow = 0;
		ll swaps = 0, tot_chickens = 0;
		for (int i = n - 1; i >= 0; --i){
			if (tot_chickens >= k) break;
			if (b - coor[i] <= speed[i]*t){
				++tot_chickens;
				swaps += slow;
			}
			else {
				++slow;
			}
		}
		if (tot_chickens >= k)
			printf("Case #%d: %d\n", it, swaps);
		else
			printf("Case #%d: IMPOSSIBLE\n", it);
		cerr << it << endl;
	}
	return 0;
}