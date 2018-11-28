#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdlib>
using namespace std;

unsigned char combined[256][256];
bool opposed[256][256];
int present[256];

void solve(int CASE)
{
    int c, d, n;
    char c1, c2, c3;
    unsigned char list[300];
    int nlist = 0;

    memset(combined, 0, sizeof(combined));
    memset(opposed, 0, sizeof(opposed));
    memset(present, 0, sizeof(present));

    cin >> c;
    for (int i = 0; i < c; i++)
    {
        cin >> c1 >> c2 >> c3;
        combined[c1][c2] = combined[c2][c1] = c3;
    }

    cin >> d;
    for (int i = 0; i < d; i++)
    {
        cin >> c1 >> c2;
        opposed[c1][c2] = opposed[c2][c1] = true;
    }

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> c1;
        if (nlist == 0) {
            list[nlist++] = c1;
            present[c1]++;
            //printf("put %c\n", c1);
            continue;
        } 

        c2 = list[nlist - 1];
        if ((c3 = combined[c1][c2])) {
            present[c2]--;
            list[nlist - 1] = c3;
            present[c3]++;
            continue;
        }

        bool cleared = false;
        for (int j = 0; j < 256; j++)
            if (opposed[c1][j] && present[j]) {
                memset(present, 0, sizeof(present));
                nlist = 0;
                cleared = true;
                break;
            }

        if (!cleared) {
            list[nlist++] = c1;
            present[c1]++;
            //printf("put %c\n", c1);
        }
    }

    printf("Case #%d: [", CASE);
    for (int i = 0; i < nlist; i++)
        printf("%c%s", list[i], i + 1 == nlist ? "" : ", ");
    puts("]");
}

int main()
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++)
        solve(i);

    return 0;
}
