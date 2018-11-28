#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cmath>

#include <string>
#include <vector>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <algorithm>

#define INFINITO 0x3f3f3f3f

using namespace std;

#define MAX_PAL 5010
#define MAX_LET 16

string pal[MAX_PAL];
int l, d, n;

int main (void) {

    int i, j, k;
    int caso = 1;

    scanf("%d %d %d", &l, &d, &n);

    for (i=0; i<d; ++i)
        cin >> pal[i];

    sort(pal, pal+d);

    for (k=0; k<n; ++k) {
        string linha;
        cin >> linha;

        int size = linha.length();
        int len = 0;
        set<char> q[l];

        for (i=0; i<size; ++i) {
            if (linha[i] == '(') {
                ++i;
                while (linha[i] != ')')
                    q[len].insert(linha[i++]);
            }
            else {
                q[len].insert(linha[i]);
            }
            len++;
        }

        int total=0;
        for (i=0; i<d; ++i) {
            for (j=0; j<l; ++j) {
                if (q[j].find(pal[i][j]) == q[j].end())
                    break;
            }
            if (j==l)
                ++total;
        }

        printf("Case #%d: %d\n", caso++, total);
    }

    return 0;
}
