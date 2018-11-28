#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <vector>
#include <cstring>
using namespace std;

const char welcome[] = "welcome to code jam";
const int welcomeLength = 19;

char line[600];
int linelen;

int main(void) {
    int N;
    scanf("%d", &N);
    gets(line);
    for (int testCase = 1; testCase <= N; testCase++) {
        gets(line);
        linelen = strlen(line);
        vector< vector<int> > ma(welcomeLength+1, vector<int>(linelen+1));
        ma[0] = vector<int>(linelen+1, 1);
        for (int i = 1; i <= welcomeLength; i++) {
            for (int j = 1; j <= linelen; j++) {
                ma[i][j] = ma[i][j-1];
                if (welcome[i-1] == line[j-1]) {
                    ma[i][j] += ma[i-1][j-1];
                    if (ma[i][j] >= 10000)
                        ma[i][j] -= 10000;
                }
            }
        }
        printf("Case #%d: %04d\n", testCase, ma[welcomeLength][linelen]);
    }
    return 0;
}
