#include <iostream>
#include <vector>
#include <stdio.h>

using namespace std;

vector<char> values;

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	int T,C,D,N;

	char c1,c2,c3;
	char o1,o2;
	char val;

	scanf("%d", &T);
	for (int var = 1; var <= T; ++var) {

		values.clear();
		scanf("%d", &C);
		if (C == 1) {
			cin>>c1;
			cin>>c2;
			cin>>c3;
		}

		scanf("%d", &D);
		if (D == 1) {
			cin>>o1;
			cin>>o2;
		}

		scanf("%d", &N);
		int numop1 = 0, numop2 = 0;

		for (int i = 0; i<N; ++i) {
			cin>>val;

			if (C == 1) {
				if (!values.empty()) {
					if (( (values.back() == c1) && (val == c2)) || ( (values.back() == c2) && (val == c1)) ) {
						if (values.back() == o1)
							numop1--;
						else if (values.back() == o2)
							numop2--;
						values.back() = c3;
						continue;
					}
				}
			}
			if (D == 1) {
				if (val == o1)
					numop1++;
				else if (val == o2)
					numop2++;
				if (numop1 > 0 && numop2 > 0) {
					values.clear();
					numop1 = 0;
					numop2 = 0;
					continue;
				}
			}
			values.push_back(val);
		}

		printf("Case #%d: [", var);
		vector<char>::iterator it;
		for (it = values.begin(); it != values.end(); ++it) {
			if (it != values.begin())
				printf(", ");
			printf("%c", (*it));
		}
		printf("]\n");
	}
	return 0;
}
