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
	freopen("A-large.in", "r", stdin);
	freopen("largeout.txt", "w", stdout);
	int T;
	cin >> T;
	for (int it = 1; it <= T; ++it){
		int n, m;
		set<string> data;
		string s;
		cin >> n >> m;
		getline(cin,s);
		for (int i = 0; i < n; ++i){
			getline(cin,s);
			do{
				data.insert(s);
			} while (cut(s));
		}
		int old = data.size();
		for (int i = 0; i < m;++i){
			getline(cin,s);
			do{
				data.insert(s);
			} while (cut(s));
		}
		cerr << it << endl;
		printf("Case #%d: %d\n", it, data.size() - old);
	}
	return 0;
}