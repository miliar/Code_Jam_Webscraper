#include<cstdio>
#include<string>
#include<queue>
#include<set>
#include<cmath>
#include<map>
#include<iostream>
using namespace std;
set<string> deleted;
map<string, char> combin;
char pattern[110];
int C, D, N;
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	char str1[110];
	cin>>T;
	for(int t = 1; t <= T; t++){
		combin.clear();
		deleted.clear();
		scanf("%d", &C);
		int i;
		for (i = 0; i < C; i++) {
			scanf("%s", str1);
			string str;
			str.insert(0, str1[0]);
			str.insert(0, str1[1]);
			combin[str] = str1[2];
			reverse(str.begin(), str.end());
			combin[str] = str1[2];
		}
		scanf("%d", &D);
		for (i = 0; i < D; i++) {
			scanf("%s", str1);
			string str;
			str.insert(0, str1[0]);
			str.insert(0, str1[1]);
			deleted.insert(str);
			reverse(str.begin(), str.end());
			deleted.insert(str);
		}
		scanf("%d%s", &N, pattern);
		vector<char> ans;
		for (i = 0; i < N; i++) {
			string str = "";
			str.insert(0, pattern[i]);
			int len = ans.size();
			if (len >= 1) {
				str.insert(0, ans[len - 1]);
				if(combin.find(str) != combin.end()) {
					ans[ans.size() - 1] = combin[str];
				} else {
					ans.push_back(pattern[i]);
					vector<char>::iterator it = ans.begin();
					bool f = false;
					for (; it != ans.end(); it++) {
						str = "";
						str.insert(0, *it);
						str.insert(0, pattern[i]);
						if (deleted.find(str) != deleted.end()) {
							f = true;
							break;
						}
					}
					if (f) ans.clear();
				}
			} else {
				ans.push_back(pattern[i]);
			}
		}
		printf("Case #%d: [", t);
		for(i = 0; i < ans.size(); i++) {
			if (i == 0) {
				printf("%c", ans[0]);
			} else {
				printf(", %c", ans[i]);
			}
		}
		printf("]\n");
	}
	return 0;
}
