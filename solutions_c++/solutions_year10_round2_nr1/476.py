#include <stdio.h>
#include <set>
#include <string>

using namespace std;

int T, t, N, M, i, j, ans;
char path[128], sub[128];
set<string> dir;
pair<set<string>::iterator, bool> ret;

int main(void) {
	FILE* fin;
	FILE* fout;
	fin = fopen("A-large.in", "r");
	fout = fopen("output.txt", "w");

	fscanf(fin, "%d", &T);
	for(t = 1; t <= T; t++) {
		dir.clear();
		dir.insert("/");
		ans = 0;
		fscanf(fin, "%d%d", &N, &M);
		for(i = 0; i < N; i++) {
			fscanf(fin, "%s", path);
			dir.insert(path);
		}
		for(i = 0; i < M; i++) {
			fscanf(fin, "%s", path);
			sub[0] = '/';
			for(j = 1; j <= strlen(path); j++) {
				if(path[j] == '/' || path[j] == '\0') {
					sub[j] = '\0';

					ret = dir.insert(sub);
					if(ret.second) ans++;

					sub[j] = '/';
				}else {
					sub[j] = path[j];
				}
			}
		}
	
		fprintf(fout, "Case #%d: %d\n", t, ans);
	}

	fclose(fout);
	fclose(fin);
	return 0;
}
