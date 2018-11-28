#include <iostream>
#include <string>
using namespace std;
int T, N, C, D, length;
char s[100];
int com[26][26];
int opp[26][26];
char list[100];
FILE *fin = fopen("input.in", "r");
FILE *fout = fopen("output.out", "w");

int main() {
    fscanf(fin, "%d", &T);
    for(int t = 0; t < T; t++) {
        for(int i = 0; i < 26; i++)
            for(int j = 0; j < 26; j++) {
                com[i][j] = 26;
                opp[i][j] = 0;
            }
        fscanf(fin, "%d", &C);
        for(int i = 0; i < C; i++) {
            fscanf(fin, "%s", &s);
            int x = s[0] - 'A', y = s[1] - 'A', z = s[2] - 'A';
            com[x][y] = com[y][x] = z;
        }
        fscanf(fin, "%d", &D);
        for(int i = 0; i < D; i++) {
            fscanf(fin, "%s", &s);
            int x = s[0] - 'A', y = s[1] - 'A';
            opp[x][y] = opp[y][x] = 1;
        }
        fscanf(fin, "%d", &N);
        fscanf(fin, "%s", &s);
        length = 0;
        memset(list, 0, sizeof(list));
        for(int i = 0; i < N; i++) {
            list[length++] = s[i];
            if (length >= 2) {
                if (com[list[length - 2] - 'A'][list[length - 1] - 'A'] < 26) {
                    list[length - 2] = com[list[length - 2] - 'A'][list[length - 1] - 'A'] + 'A';
                    length--;
                }
                for(int j = 0; j < length - 1; j++)
                    if (opp[list[j] - 'A'][list[length - 1] - 'A'] == 1) {
                        length = 0;
                        break;
                    }
            }
        }
        fprintf(fout, "Case #%d: [", t + 1);
        for(int i = 0; i < length - 1; i++)
            fprintf(fout, "%c, ", list[i]);
        if (length > 0)
            fprintf(fout, "%c", list[length - 1]);
        fprintf(fout, "]\n");
    }
}
