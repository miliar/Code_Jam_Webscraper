#include <stdio.h>
#include <set>
using namespace std;

multiset <pair <pair <int, int>, bool> > vlaky;
int a, b, n, pa, pb, t, sh, sm, kh, km, i, c;
multiset <int> ina, inb;

int main() {
	scanf("%d", &n);
	for (c = 1; c <= n; c++) {
		a = b = 0;
		vlaky.clear();
		ina.clear();
		inb.clear();
		scanf("%d", &t);
		scanf("%d%d", &pa, &pb);
		for (i = 0; i < pa; i++) {
			scanf("%d:%d %d:%d", &sh, &sm, &kh, &km);
			vlaky.insert(make_pair( make_pair(sh*60+sm, kh*60+km), true));
		}
		for (i = 0; i < pb; i++) {
			scanf("%d:%d %d:%d", &sh, &sm, &kh, &km);
			vlaky.insert(make_pair( make_pair(sh*60+sm, kh*60+km), false));
		}
		while (!vlaky.empty()) {
			if (vlaky.begin()->second) {
				if (ina.empty() || *(ina.begin()) > vlaky.begin()->first.first) {
					a++;
				} else {
					ina.erase(ina.begin());
				}	
				inb.insert(vlaky.begin()->first.second + t);
			} else {
				if (inb.empty() || *(inb.begin()) > vlaky.begin()->first.first) {
					b++;
				} else {
					inb.erase(inb.begin());
				}	
				ina.insert(vlaky.begin()->first.second + t);
			}
			vlaky.erase(vlaky.begin());
		}
		printf("Case #%d: ", c);
		printf("%d %d\n", a, b);
	}
	return 0;
}
