#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;


int n, t, na, nb, dh, dm, ah, am, ca, cb, mina, minb;

int main() {
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%i\n", &n);
	for (int i = 0; i<n; i++) {
		scanf("%i\n", &t);
		scanf("%d %d\n", &na, &nb);
		vector <pair<int, int> > ttable;
		for (int j = 0; j<na; j++) {
			scanf("%d:%d %d:%d\n", &dh, &dm, &ah, &am);
			ttable.push_back(make_pair(dh*60+dm, 1));
			ttable.push_back(make_pair(ah*60+am+t, 2));
		}
		for (int j = 0; j<nb; j++) {
			scanf("%d:%d %d:%d\n", &dh, &dm, &ah, &am);
			ttable.push_back(make_pair(dh*60+dm, 3));
			ttable.push_back(make_pair(ah*60+am+t, 0));
		}
		sort(ttable.begin(), ttable.end());
		ca = cb = 0;
		mina = minb = 0;
		for (int j = 0; j<ttable.size(); j++) {
			switch (ttable[j].second) {
				case 0:
					ca++;
					break;
				case 1:
					ca--;
					if (ca<mina)
						mina = ca;
					break;
				case 2:
					cb++;
					break;
				case 3:
					cb--;
					if (cb<minb) 
						minb = cb;
					break;
			}
		}
		printf("Case #%i: %i %i\n", i+1, -mina, -minb);
	}
}