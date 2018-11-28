#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <vector>

using namespace std;

int L, D, N;
char words[5020][20];
char line[1024 * 32];
bool present[128];
int cursor;

vector<int> new_valid(const vector<int>& old_valid) {
    vector<int> ret;
    for (int i = 0; i < old_valid.size(); ++i) {
        if (present[words[old_valid[i]][cursor] - 'a']) {
            ret.push_back(old_valid[i]);
        }
    }
    ++cursor;
    memset(present, 0, sizeof(present));
    return ret;
}

int main() {
    FILE *f = fopen("a.in", "r");
    fscanf(f, "%d %d %d\n", &L, &D, &N);
    for (int i = 0; i < D; ++i) {
        fscanf(f, "%s\n", words[i]);
    }
    for (int i = 0; i < N; ++i) {
        fgets(line, 1024 * 32, f);
        int len = strlen(line);
        while (len > 0 && line[len - 1] == '\n') {
            line[--len] = 0;
        }
        bool open = false;
        vector<int> valid;
        memset(present, 0, sizeof(present));
        cursor = 0;
        for (int j = 0; j < D; ++j) valid.push_back(j);
        for (int j = 0; j < len; ++j) {
            if (line[j] == '(') {
                open = true;
            } else if (line[j] == ')') {
                valid = new_valid(valid);
                open = false;
            } else {
                present[line[j] - 'a'] = 1;
                if (!open) {
                    valid = new_valid(valid);
                }
            }
        }
        assert(L == cursor);
        printf("Case #%d: %d\n", i + 1, valid.size());
    }
}
