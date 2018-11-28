#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>

#include <cstdio>
#include <cstring>
#include <cassert>
#include <cmath>
#include <ctime>

using namespace std;

typedef long long int64;
typedef long double ldouble;

#define PB(a) push_back(a)
#define MP(a, b) make_pair(a, b)

#define PROBLEM "A"

const int MAXN = 128;

struct Command {
	char c;
	int m;
};

#define sign(x) (x == 0 ? 0 : (x < 0 ? (-1) : (+1)))

vector<Command> com, com1, com2;

int main() {
	freopen(PROBLEM ".in", "rt", stdin);
	freopen(PROBLEM ".out", "wt", stdout);

	int T;
	scanf("%d\n", &T);

	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);

		com.clear();
		com1.clear();
		com2.clear();

		int n;
		scanf("%d", &n);
		for (int i = 1; i <= n; i++) {
			Command c;
			scanf(" %c %d", &c.c, &c.m);
			assert(c.c == 'O' || c.c == 'B');
			com.push_back(c);
			if (c.c == 'B') com1.PB(c);
			else com2.PB(c);
		}

		int p1 = 1, p2 = 1;
		int i1 = 0, i2 = 0;
		int ans = 0;

        for (int i = 0; i < com.size(); i++) {
        	Command c = com[i];
        	
        	int mvs = 1;
        	
        	if (c.c == 'B') {
        		while (p1 != c.m) {
        			mvs++;
        			p1 += sign(c.m - p1);
        		}
        		
        		if (i2 < com2.size()) {
        			int snd = mvs;
        			while (snd > 0 && p2 != com2[i2].m) {
        				snd--;
        				p2 += sign(com2[i2].m - p2);
        			}
        		}
        		
        		i1++;
        	}
        	else {
        		while (p2 != c.m) {
        			mvs++;
        			p2 += sign(c.m - p2);
        		}
        		
        		if (i1 < com1.size()) {
        			int snd = mvs;
        			while (snd > 0 && p1 != com1[i1].m) {
        				snd--;
        				p1 += sign(com1[i1].m - p1);
        			}
        		}	
        		
        		i2++;
        	}

        	ans += mvs;
        }

        assert(i1 == com1.size() && i2 == com2.size());

		printf("%d\n", ans);
	}

	return 0;
}
