#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cstdlib>

#include <iostream>
#include <memory>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>

#define TASK "b"

using namespace std;

#define PB(x) push_back(x)
#define MP(x, y) make_pair(x, y)

typedef long long int64;
typedef unsigned long long unt64;

#define MAXLEN 30

int T, n, p[MAXLEN];

int digit[10];

int main()
{
    freopen(TASK ".in", "rt", stdin);
    freopen(TASK ".out", "wt", stdout);

    scanf("%d", &T);
    for (int t = 1; t <= T; t++)
    {
        scanf("\n");
        char ch;
        n = 0;
        while (scanf("%c", &ch) == 1 && ch != '\n')
            p[n++] = ch - (int)'0';
        
        if (!next_permutation(p, p + n))
        {
            memset(digit, 0, sizeof(digit));
            for (int i = 0; i < n; i++)
                digit[p[i]]++;
            int min_number = 0;
            for (int i = 1; i <= 9; i++)
                if (digit[i] > 0)
                   {
                        min_number = i;
                        break;
                   }
            if (min_number == 0)
                cerr << "AAA\n";

            p[0] = min_number;
            digit[min_number]--;
            digit[0]++;

            n = 1;
            for (int i = 0; i <= 9; i++)
                for (int j = 0; j < digit[i]; j++)
                    p[n++] = i;                                    
        }

        printf("Case #%d: ", t);
        for (int i = 0; i < n; i++)
            printf("%d", p[i]);                            
        printf("\n");
    }


    return 0;
}

