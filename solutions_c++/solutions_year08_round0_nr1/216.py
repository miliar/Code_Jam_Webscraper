#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <utility>
#include <queue>

using namespace std;

map<string, int> meat;

int getnum(const string &s){
	if (meat.find(s) == meat.end()){
		int res = meat.size();
		meat[s] = res;
		return res;
	}else return meat[s];
}


#define maxn 1100
int ans[maxn][maxn];

int main(){
	int ferlon;
	cin >> ferlon;
	for (int _ = 0; _ < ferlon; ++_){
		meat.clear();
		int s;
		cin >> s;
		string tmp;
		getline(cin, tmp);
		int i;
		for (i = 0; i < s; i++) {
			getline(cin, tmp);
//			cerr << tmp << endl;
			getnum(tmp);			
		}
		memset(ans, 63, sizeof(ans));
		ans[0][0] = 0;
		int q;
		cin >> q;
//		cerr << q << endl;
		getline(cin, tmp);
		for (i = 1; i <= q; i++){
			getline(cin, tmp);
			int num = getnum(tmp);
			int j;
			for (j = 1; j <= s; j++) if (j - 1 != num){
				int t;
				for (t = 0; t <= s; t++) ans[i][j] = min(ans[i][j], ans[i - 1][t] + (t != j));
			}
		}
		int res = 0x3f3f3f3f;
//		cerr << "PREVED" << endl;
//		cerr << s << endl;
//		cerr << q << endl;
		for (i = 0; i <= s; i++) if (ans[q][i] < res) res = ans[q][i];
//		cerr << "PREVED" << endl;
		if (res == 0) res = 1;
		printf("Case #%d: %d\n", _ + 1, res - 1);
	}
	return 0;
}	
