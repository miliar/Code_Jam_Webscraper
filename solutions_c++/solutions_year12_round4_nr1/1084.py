#include <cstring>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>
using namespace std;

int N, D;
int d[10000], l[10000], h[10000], s[10000], t[10000];

queue<int> q;

bool bfs() {
    if (d[0] + d[0] >= D) return true;
    q.push(0);
    h[0] = d[0];
    s[0] = 0;
    t[0] = 0;
    for (int i = 1; i < N; ++i) {
        h[i] = 0;
        s[i] = 0;
        t[i] = 0;
    }
    while (!q.empty()) {
        int vine = q.front();
        q.pop();
        for (int i = t[vine] + 1; i < N && d[i] <= d[vine] + h[vine]; ++i) {
            int newh = min(d[i] - d[vine], l[i]);
            if (newh > h[i]) {
                h[i] = newh;
                if (d[i] + newh >= D) return true;
                q.push(i);
            }
            t[vine] = i;
        }
        for (int i = s[vine] - 1; i >= 0 && d[i] >= d[vine] - h[vine]; --i) {
            int newh = min(d[vine] - d[i], l[i]);
            if (newh > h[i]) {
                h[i] = newh;
                if (d[i] + newh >= D) return true;
                q.push(i);
            }
            s[vine] = i;
        }
    }
    return false;
}

int main() {
	FILE *fin = fopen("A-large.in", "r");
	FILE *fout = fopen("out.txt", "w");
	int t;
	fscanf(fin, "%d", &t);
	for (int i = 1; i <= t; ++i) {
        fscanf(fin, "%d", &N);
        for (int j = 0; j < N; ++j)
            fscanf(fin, "%d%d", &d[j], &l[j]);
        fscanf(fin, "%d", &D);
		fprintf(fout, "Case #%d: ", i);
        if (bfs()) fprintf(fout, "YES\n");
        else fprintf(fout, "NO\n");
	}
	fclose(fout);
	fclose(fin);
	return 0;
}
