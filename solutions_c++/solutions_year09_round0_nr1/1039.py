#include <cstdio>
#include <cassert>

#include <vector>
#include <string>

using namespace std;

int main() {
    // freopen("input.txt", "r", stdin);
    // freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int l;
    int d;
    int n;

    scanf("%d%d%d\n", &l, &d, &n);
    vector<string> words;
    for (size_t i = 0; i < d; ++i) {
        char line[1000];
        gets(line);
        assert(strlen(line) == l);
        words.push_back(line);
    }

    for (size_t nT = 0; nT < n; ++nT) {
        char line[1000];
        gets(line);
        
        bool mask[20][27];
        memset(mask, 0, sizeof(mask));
        int pos = 0;
        for (size_t i = 0; i < l; ++i) {
            if (line[pos] == '(') {
                ++pos;
                while (line[pos] != ')') {
                    mask[i][line[pos] - 'a'] = true;
                    ++pos;
                }
                ++pos;
            } else {
                mask[i][line[pos] - 'a'] = true;
                ++pos;
            }
        }
        assert(pos == strlen(line));

        int res = 0;
        for (size_t i = 0; i < words.size(); ++i) {
            int pos = 0;
            while ( (pos < l) && mask[pos][words[i][pos] - 'a'] )
                ++pos;
            res += pos == l;
        }
        printf("Case #%d: %d\n", nT + 1, res);
    }
    
    return 0;
}
