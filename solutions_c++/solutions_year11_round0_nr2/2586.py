#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>

#include <tr1/unordered_set>
#include <tr1/unordered_map>

#define pb push_back
#define pob pop_back

using namespace std;

using namespace std::tr1;

int t;
unordered_map<string, char> c;
unordered_map<char, char> d;
char n[1000];

void init()
{
	int i, temp;
	char target, temp2;

	c.clear();
	d.clear();

	scanf("%d", &temp);
	for (i = 0; i < temp; i++) {
		scanf("%s", n);
		target = n[2];
		n[2] = '\0';
		c[n] = target;
		temp2 = n[0];
		n[0] = n[1];
		n[1] = temp2;
		c[n] = target;
	}

	scanf("%d", &temp);
	for (i = 0; i < temp; i++) {
		scanf("%s", n);
		d[n[0]] = n[1];
		d[n[1]] = n[0];
	}

	scanf("%d", &temp);
	scanf("%s", n);
}

void done()
{
	int i, j, tag;
	vector<char> ans;
	char buf[3];

	ans.clear();
	for (i = 0; n[i]; i++) {
		ans.pb(n[i]);

		tag = 1;
		while (tag) {
			tag = 0;
			if (ans.size() >= 2) {
				buf[0] = ans[ans.size() - 2];
				buf[1] = ans[ans.size() - 1];
				buf[2] = '\0';
				if (c.find(buf) != c.end()) {
					ans.pob();
					ans.pob();
					ans.pb(c[buf]);
					tag = 1;
				}
			}
		}

		tag = 1;
		while (tag) {
			tag = 0;
			if (ans.size() >= 2 && d.find(ans.back()) != d.end()) {
				for (j = 0; ! tag && j < ans.size() - 1; j++)
					if (ans[j] == d[ans.back()]) {
						ans.clear();
						tag = 1;
					}
			}
		}
	}

	printf("[");
	if (ans.size() > 0)
		printf("%c", ans[0]);
	for (i = 1; i < ans.size(); i++)
		printf(", %c", ans[i]);
	printf("]");
}

int main()
{
	int i;

	scanf("%d", &t);
	for (i = 0; i < t; i++) {
		init();
		printf("Case #%d: ", i + 1);
		done();
		printf("\n");
	}

	return (0);
}


