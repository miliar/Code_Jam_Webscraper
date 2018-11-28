#include <iostream>
#include <vector>
using namespace std;
int abs(int x){
	return x > 0 ? x : -x;
}
int main(){
	int cases;
	scanf("%d", &cases);
	for (int tt = 0; tt < cases; ++tt){
		int n;
		scanf("%d", &n); getchar();
		vector<int> O, B, order;
		for (int i = 0; i < n; ++i){
			char ch;
			int id;
			scanf("%c %d", &ch, &id);
			getchar();
			if (ch == 'O'){
				O.push_back(id);
				order.push_back(0);
			} else {
				B.push_back(id);
				order.push_back(1);
			}
		}
		int pos1 = 1, pos2 = 1;
		int p1 = 0, p2 = 0;
		int cnt1 = 0, cnt2 = 0;
		int ans = 0;
		for (int i = 0; i < n; ++i){
			if (order[i] == 0){
				if (abs(O[p1] - pos1) > cnt1){
					ans += abs(O[p1] - pos1) + 1 - cnt1;
					cnt2 += abs(O[p1] - pos1) + 1 - cnt1;
				} else {
					ans += 1;
					cnt2 += 1;
				}
				pos1 = O[p1];
				p1++;
				cnt1 = 0;
				
			} else {
				if (abs(B[p2] - pos2) > cnt2){
					ans += abs(B[p2] - pos2) + 1 - cnt2;
					cnt1 += abs(B[p2] - pos2) + 1 - cnt2;
				} else {
					ans += 1;
					cnt1 += 1;
				}
				pos2 = B[p2];
				p2++;
				cnt2 = 0;
				
			}
		}
		printf("Case #%d: %d\n", tt + 1, ans);
	}
	return 0;
}
