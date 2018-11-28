#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

char mrc[20], charmander[100], s[20];
vector<char> v;
set<int> se;

void charizard(vector<char> v) {
	int i;
	for (i = 0; i < (int) v.size(); i++) {
		charmander[i] = v[i];
	}
	charmander[i] = '\0';
}

void bt(int x) {
	if (x == (int) strlen(s)) {
		charizard(v);
		se.insert(atoi(charmander));
		return;
	}
	
	vector<char> jf;
	for (int i = 0; i < (int) strlen(s); i++) {
		if (!mrc[i] && find(jf.begin(), jf.end(), s[i]) == jf.end()) {
			jf.push_back(s[i]);

			v.push_back(s[i]);
			mrc[i] = 1;
			bt(x + 1);
			mrc[i] = 0;
			v.pop_back();
		}
	}
}

int main(void)
{
	int tc;
	scanf("%d ", &tc);

	for (int t = 1; t <= tc; t++) {
		gets(s);
		
		v.clear();
		se.clear();
		memset(mrc, 0, sizeof(mrc));
		vector<char> jf;
		jf.clear();

		for (int i = 0; i < (int) strlen(s); i++) {
			if (find(jf.begin(), jf.end(), s[i]) == jf.end()) {
				jf.push_back(s[i]);

				v.push_back(s[i]);
				mrc[i] = 1;
				bt(1);
				mrc[i] = 0;
				v.pop_back();
			}
		}
		
		printf("Case #%d: ", t);
		set<int>::iterator it = se.find(atoi(s));
		if (++it == se.end()) { //ultimo

			char str[200];
			sprintf(str, "%d", *(se.begin()));
			printf("%c", str[0]);

			int i;
			for (i = 0; i < strlen(s) - strlen(str) + 1; i++) {
				printf("0");
			}

			for (i = 1; i < (int) strlen(str); i++) {
				printf("%c", str[i]);
			}
			
			printf("\n");

		} else {
			printf("%d\n", *it);
		}
	}
	
	return 0;
}
