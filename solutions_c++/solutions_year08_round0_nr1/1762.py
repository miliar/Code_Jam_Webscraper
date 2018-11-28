#include <iostream>
#include <string>
#include <map>
using namespace std;
map<string, int> m;
const int MAXN = 1010;
int main(){
	int cases;
	cin >> cases;
	for (int t = 0; t != cases; ++t){
		int n;
		cin >> n;
		m.clear(); getchar();
		for (int i = 0; i != n; ++i){
			string str;
			getline(cin, str);
			m[str] = i;
		}
		int k; cin >> k; getchar();
		int occur = 0, ans = 0;
		bool used[MAXN];
		memset(used, 0, sizeof(used));
		for (int i = 0; i != k; ++i){
			string str; getline(cin, str);
			int x = m[str];
			if (!used[x]){
				++occur;
				used[x] = true;
				if (occur == n){
					++ans; memset(used, 0, sizeof(used));
					used[x] = true; occur = 1;
				}
			}
		}
		if (occur == n) ++ans;
		printf("Case #%d: %d\n", t + 1, ans);
	}
	return 0;
}