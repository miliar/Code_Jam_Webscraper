#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <cassert>

#define BUFFER_SIZE 1024
#define MAXN 128
#define INF 2000000000

using namespace std;

int f[MAXN];
char buffer[BUFFER_SIZE];
vector <string> engines;
vector <int> queries;

int getID(const string &name) {
    for (unsigned i = 0; i < engines.size(); i++) {
        if (engines[i] == name) {
            return i;
        }
    }
    return -1;
}

int greedy() {
    int result = 0;
    set <int> used;
    for (unsigned i = 0; i < queries.size(); i++) {
        used.insert(queries[i]);
        if (used.size() == engines.size()) {
            result ++;
            used.clear();
            used.insert(queries[i]);
        }
    }
    return result;
}

int dynamic() {
    memset(f, 0, sizeof(f));

    for (unsigned i = 0; i < queries.size(); i++) {
        int tmp = INF;
        for (unsigned j = 0; j < engines.size(); j++) {
            if (i == 0 || j != queries[i - 1]) tmp = min(f[j] + 1, tmp);
        }

        for (unsigned j = 0; j < engines.size(); j++) {
            if (j != queries[i]) f[j] = min(f[j], tmp);
            else f[j] = INF;
        }
    }

    int result = INF;
    for (unsigned i = 0; i < engines.size(); i++) {
        result = min(f[i], result);
    }
    return result;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int test = 0; test < T; test++) {
        engines.clear();
        queries.clear();
        int n, m;
        scanf("%d", &n);
        fgets(buffer, BUFFER_SIZE, stdin);
        for (int i = 0; i < n; i++) {
            gets(buffer);
            engines.push_back(buffer);
        }

        scanf("%d", &m);
        fgets(buffer, BUFFER_SIZE, stdin);
        for (int i = 0; i < m; i++) {
            gets(buffer);
            queries.push_back(getID(buffer));
        }

        assert (dynamic() == greedy());
        printf ("Case #%d: %d\n", test + 1, greedy());
    }
}
