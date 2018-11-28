#include <cstdio>
#include <vector>
using namespace std;

vector<int> pt;
int main() {
	int T;
	scanf("%d", &T);
	for(int q=1;q<=T;q++) {
		int n, s, p;
		scanf("%d %d %d", &n, &s, &p);
		pt.clear();
		for(int i=0;i<n;i++) {
			int t;
			scanf("%d", &t);
			pt.push_back(t);
		}
		int ans = 0;
		vector<int> candi;
		for(int i=0;i<pt.size();i++) {
			int temp = (pt[i] + 2) / 3;
			if(temp >= p) {
				ans++;
			} else {
				candi.push_back(pt[i]);
			}
		}
		if(s != 0){
			for(int i=0;i<candi.size();i++) {
				if(candi[i] < 2) continue;
				int temp = (candi[i]-2) / 3;
				if(temp+2 >= p) {
					ans++;
					s--;
				}
				if(s == 0) break;
			}
		}
		printf("Case #%d: %d\n", q, ans);
	}
}
