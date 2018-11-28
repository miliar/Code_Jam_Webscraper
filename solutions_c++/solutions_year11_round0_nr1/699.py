#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <vector>

using namespace std;
vector<int> o, b;
int id[100000];
int main() {
	int T;
	int n;
	scanf("%d", &T);
	char ch[10];
	int x;
	int i;
	int cas = 1;
	while (T--) {
		o.clear();
		b.clear();
		scanf("%d", &n);
		for (i = 0; i < n; i++) {
			scanf("%s%d", ch, &x);
			if (ch[0] == 'B') {
				b.push_back(x);
				id[i] = 1;
			} else {
				o.push_back(x);
				id[i] = 0;
			}
		}
		int cnt = 0;
		int nowo = 1, nowb = 1;
		int bi = 0, oi = 0;
		i = 0;
		while (i < n) {
			if (id[i]) {
				if (nowb == b[bi]) {
					cnt++;
					i++;
					bi++;
				} else {
					if (nowb > b[bi])
						nowb--;
					else nowb++;
					cnt++;
				}
				if (oi < o.size() && nowo > o[oi])
					nowo --;
				else if(oi < o.size() && nowo < o[oi])
					nowo++;
			} else {
				if (nowo == o[oi]) {
					cnt++;
					i++;
					oi++;
				} else {
					if (nowo > o[oi])
						nowo --;
					else nowo++;
					cnt++;
				}
				if (bi < b.size() && nowb > b[bi])
					nowb--;
				else if(bi < b.size() && nowb < b[bi])
					nowb++;
			}
		}
		printf("Case #%d: %d\n", cas++, cnt);
	}
	
	return 0;
}