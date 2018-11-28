#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <set>
#include <string>

using namespace std;

#define MAXPATH			120

int solve(void)
{
	int N, M, i, len;
	char buf[MAXPATH], *p, *q;
	int answer;
	set<string> dirs;
	set<string>::iterator it;

	scanf("%d %d", &N, &M);

	for (i = 0; i < N; i++) {
		scanf("%s", buf);
		len = strlen(buf);
		if (buf[len - 1] == '/')
			buf[--len] = '\0';
		dirs.insert(string(buf));
	}

	answer = 0;
	for (i = 0; i < M; i++) {
		scanf("%s", buf);
		len = strlen(buf);
		if (buf[len - 1] != '/') {
			buf[len++] = '/';
			buf[len] = '\0';
		}
		for (p = buf + 1; (q = strchr(p, '/')); p = q + 1) {
			*q = '\0';
			if (dirs.find(string(buf)) == dirs.end()) {
				dirs.insert(string(buf));
				answer++;
			}
			*q = '/';
		}
	}

	dirs.erase(dirs.begin(), dirs.end());

	return answer;
}

int main(void)
{
	int T, testno;

	scanf("%d", &T);
	for (testno = 1; testno <= T; testno++)
		printf("Case #%d: %d\n", testno, solve());

	return 0;
}
