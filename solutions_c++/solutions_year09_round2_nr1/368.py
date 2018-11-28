#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cfloat>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <deque>
#include <list>

#define loop(a, b) for(a = 0; a < b; ++a)
#define iter(a, b, c) for(a = b; a < c; ++a)

using namespace std;

struct V {
	double p;
	char s[1024];
	int x, y;
};

#define MAX (1024)

V v[MAX];

int numVertices;

void rec(int a) {
	char c;
	scanf(" %lf ", &v[a].p);

//	printf("%d %.2f\n", a , v[a].p);
	
	scanf(" %c", &c);
	if (c == ')')
		return;
	v[a].s[0] = c;
	int i;
	for(i = 1;;) {
		scanf("%c", &c);
		if (!isspace(c))
			v[a].s[i++] = c;
		else
			break;
	}
	v[a].s[i] = '\0';
	scanf(" %*c ");

	numVertices += 2;
	v[a].x = numVertices-2;
	v[a].y = numVertices-1;

	rec(v[a].x);
	scanf(" %*c ");
	rec(v[a].y);

	scanf(" %*c ");
}

set<string> fs;

char f[1024];

double rec2(int a, double p) {
	if (v[a].s[0] == '\0')
		return p*v[a].p;
//	printf("%s\n", v[a].s);
	if (fs.find(v[a].s) != fs.end())
		return rec2(v[a].x, p*v[a].p);
	else
		return rec2(v[a].y, p*v[a].p);
}

int main(void) {
	int ds, i, n, m, tc = 1;
	scanf("%d", &ds);
	while(ds--) {
		loop(i, MAX) {
			v[i].x = v[i].y = -1;
			v[i].s[0] = '\0';
		}
		numVertices = 1;
		scanf(" %*d %*c ");
		rec(0);

		scanf(" %d", &n);
		printf("Case #%d:\n", tc++);
		while(n--) {
			fs.clear();
			scanf("%*s %d", &m);
			while(m--) {
				scanf("%s", f);
				fs.insert(f);
			}

			printf("%.7f\n", rec2(0, 1));
		}
	}
	return 0;
}
