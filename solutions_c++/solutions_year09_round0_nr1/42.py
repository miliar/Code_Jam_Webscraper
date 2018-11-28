#include <cstdio>
#include <cstring>

using namespace std;

int hash[16][26];
char name[5000][16];
char line[100000000];
int L, D, N;

int main() {
    scanf("%d%d%d", &L, &D, &N);
    for (int i = 0; i < D; i++)
        scanf("%s", name[i]);
    for (int caseSize = 0; caseSize < N; caseSize++) {
        scanf("%s", line);
        for (int i = 0, pos = 0; i < L; i++) {
            memset(hash[i], false, sizeof(hash[i]));
            if (line[pos] != '(') hash[i][line[pos++] - 'a'] = true;
            else {
                pos++;
                while (line[pos] != ')')
                    hash[i][line[pos++] - 'a'] = true;
                pos++;
            }
        }
        int result = 0;
        for (int i = 0; i < D; i++) {
            bool found = true;
            for (int j = 0; found && j < L; j++)
                if (!hash[j][name[i][j] - 'a']) found = false;
            if (found) result++;
        }
        printf("Case #%d: %d\n", caseSize + 1, result);
    }
    return 0;
}
