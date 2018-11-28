#include <iostream>
#include <vector>
using namespace std;
vector<int> need1, need2, canuse1, canuse2;
int main(){
	int cases;
	cin >> cases;
	for (int tt = 0; tt != cases; ++tt){
		int t, m, n;
		cin >> t >> m >> n;
		need1.clear(); need2.clear(); canuse1.clear(); canuse2.clear();
		for (int i = 0; i != m; ++i){
			int x, y;
			scanf("%d:%d", &x, &y);
			int temp = x * 60 + y;
			need1.push_back(temp);
			scanf("%d:%d", &x, &y);
			temp = x * 60 + y + t;
			canuse2.push_back(temp);
		}
		for (int i = 0; i != n; ++i){
			int x, y;
			scanf("%d:%d", &x, &y);
			int temp = x * 60 + y;
			need2.push_back(temp);
			scanf("%d:%d", &x, &y);
			temp = x * 60 + y + t;
			canuse1.push_back(temp);
		}
		sort(need1.begin(), need1.end());
		sort(need2.begin(), need2.end());
		sort(canuse1.begin(), canuse1.end());
		sort(canuse2.begin(), canuse2.end());
		int ans1 = 0, ans2 = 0, now = 0, pos = 0;
		for (int i = 0; i != m; ++i){
			while (pos < canuse1.size() && canuse1[pos] <= need1[i]){
				++pos; ++now;
			}
			if (now == 0) ++ans1; else --now;
		}
		//cout << "ok" << endl;
		//system("pause");
		now = pos = 0;
		for (int i = 0; i != n; ++i){
			while (pos < canuse2.size() && canuse2[pos] <= need2[i]){
				++pos; ++now;
			}
			if (now == 0) ++ans2; else --now;
		}
		printf("Case #%d: %d %d\n", tt + 1, ans1, ans2);
	}
	return 0;
}
