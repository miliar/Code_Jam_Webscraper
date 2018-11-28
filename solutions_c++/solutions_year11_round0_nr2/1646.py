#include <cstdio>
#include <cmath>
#include <map>
#include <vector>
using namespace std;

map<pair<char,char>, char> imap;
vector<char> opp[50];

char buf[500];

void test() {
	int C, D, N;
	imap.clear();
	for (int i=0;i<40;i++) opp[i].clear();
	scanf("%d ", &C);
	while (C--) {
		scanf("%s ", buf);
		imap[make_pair(buf[0],buf[1])] = buf[2];
	}
	scanf("%d ", &D);
	while (D--) {
		scanf("%s ", buf);
		opp[buf[0]-'A'].push_back(buf[1]);
		opp[buf[1]-'A'].push_back(buf[0]);
	}
	scanf("%d %s ", &N, buf);
	vector<char> v;
	v.push_back(buf[0]);
	int k = 2;
	char next = buf[1];
	while (next) {
		int a = v.back(), b = next;

		char action = 0;
		if (imap.find(make_pair(a,b)) != imap.end())
			action = imap[make_pair(a,b)];
		else if (imap.find(make_pair(b,a)) != imap.end())
			action = imap[make_pair(b,a)];
		if (action <= 'Z' && action >= 'A') {
			v.pop_back();
			next = action;
		}
		else {
			bool cleared = false;
			for (int i=0;i<opp[next-'A'].size();i++) {
				for (int j=0;j<v.size();j++) if (v[j] == opp[next-'A'][i]) {
					cleared = true;
					v.clear();
				}
			}
			if (!cleared) {
				v.push_back(next);
			}
			next = buf[k++];
		}
	}
	printf("[");
	for (int i=0;i<v.size();i++) printf("%s%c", i==0?"":", ", v[i]);
	printf("]\n");
}

main() {
	int z;
	scanf("%d", &z);
	for (int c = 0; c<z;c++) {
		printf("Case #%d: ", c+1);
		test();
	}
}

