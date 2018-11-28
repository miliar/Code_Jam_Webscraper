#include <iostream>
#include <string>
#include <set>
#include <cstring>

using namespace std;

char dir[200];
string temp;
set<string> kump;
set<string>::iterator ps;

int main()
{
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);
	int tc, nc, i, j;
	int dpt, len, res;
	int udah, blum;
	scanf("%d", &tc);
	for (nc = 1; nc <= tc; nc++) {
			kump.clear();
		res = 0;
		scanf("%d%d", &udah, &blum);
		for (i = 0; i < udah; i++) {
			scanf("%s", dir);
			strcat(dir, "/");
			len = strlen(dir);
			temp = "";
			for (j = 1; j < len; j++) {
				if (dir[j] == '/')
					kump.insert(temp);
				else
					temp += dir[j];
			}
		}
		for (i = 0; i < blum; i++) {
			scanf("%s", dir);
			strcat(dir, "/");
			len = strlen(dir);
			temp = "";
			for (j = 1; j < len; j++) {
				if (dir[j] == '/') {
					ps = kump.find(temp);
					if (ps == kump.end()) {
						kump.insert(temp);
						res++;
					}
				}
				else
					temp += dir[j];
			}
		}
		printf("Case #%d: %d\n", nc, res);
	}
}
