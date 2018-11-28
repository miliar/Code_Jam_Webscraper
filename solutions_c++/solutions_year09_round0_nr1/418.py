#include <iostream>
using namespace std;

const int max_word = 5000;
const int max_len = 20;

int l, d, n;

char word[max_word][max_len];
int m[max_len][26];

int main() {
    scanf("%d%d%d", &l, &d, &n);
    for (int i = 0; i < d; ++i) {
        scanf("%s", word[i]);
    }
    
    int ca = 1;
    for (int i = 0; i < n; ++i) {
        char buf[1000];
        scanf("%s", buf);
        
        memset(m, 0, sizeof(m));
        int p = 0;
        for (int j = 0; j < l; ++j) {
            if (buf[p] == '(') {
                ++p;
                while (buf[p] != ')') {
                    m[j][buf[p] - 'a'] = 1;
                    ++p;
                }
                ++p;
            } else {
                m[j][buf[p] - 'a'] = 1;
                ++p;
            }
        }
        
        int cnt = 0;
        for (int j = 0; j < d; ++j) {
            bool flag = true;
            for (int k = 0; k < l; ++k) {
                if (m[k][word[j][k] - 'a'] != 1) {
                    flag = false;
                }
            }
            if (flag)
                ++cnt;
        }
        
        printf("Case #%d: %d\n", ca++, cnt);
    }

    return 0;
}
