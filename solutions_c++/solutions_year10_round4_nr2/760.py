#include <iostream>
using namespace std;
const int MAXP = 10;
int M[1 << MAXP];
int ans;
void dfs(int a, int b){
	bool ok = true;
	if (a == b) return;
	for (int i = a; i <= b; ++i){
		if (M[i] != 0){
			ok = false; break;
		}
	}
	if (ok) return;
	for (int i = a; i <= b; ++i){
		if (M[i] > 0) --M[i];
	}
	++ans;
	dfs(a, (a + b) / 2);
	dfs((a + b) / 2 + 1, b);
}
int main(){
	int cases;
	cin >> cases;
	for (int tt = 0; tt < cases; ++tt){
		int p;
		cin >> p;
		for (int i = 0; i < (1 << p); ++i){
			cin >> M[i];
			M[i] = p - M[i];
		}
		for (int i = 0; i < p; ++i){
			for (int j = 0; j < 1 << (p - i - 1); ++j){
				int x; cin >> x;
			}
		}
		ans = 0;
		dfs(0, (1 << p) - 1);
		printf("Case #%d: %d\n", tt + 1, ans);
	}
	return 0;
}