#include <cstdio>
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

#define MAX 1<<20

char linha[MAX];
char num[MAX];
set<int> foi;

int is_happy (int n_or, int b) {

    if (n_or<b and n_or==1)
        return 1;

    int n = n_or;
    foi.insert(n);

    int x = 0;
    while (n) {
        int digito = (n % b);
        x += digito * digito;

        n /= b;
    }
    
    if (foi.find(x) != foi.end())
        return 0;

    return is_happy(x, b);
}

int main (void) {

    int casos, caso;
    scanf("%d ", &casos);

    for (caso=1; caso<=casos; ++caso) {
        gets(linha);

        int size = strlen(linha);
        char * pt = linha;

        vector<int> bases;

        while (pt < linha+size) {
            int x;
            sscanf(pt, "%d", &x);
            bases.push_back(x);

            while (isblank(*pt) and pt < linha+size)
                ++pt;
            while (!isblank(*pt) and pt < linha+size)
                ++pt;
        }

        size = bases.size();
        int i, j;
        for (i=2; ; ++i) {
            for (j=0; j<size; ++j) {
                foi.clear();
                if (!is_happy(i, bases[j]))
                    break;
            }
            if (j==size)
                break;
        }

        printf("Case #%d: %d\n", caso, i);
    }

    return 0;
}
