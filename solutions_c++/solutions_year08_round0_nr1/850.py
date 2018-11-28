#include <iostream>
#include <algorithm>
#include <cstdio>
#include <map>
#include <string>

using namespace std;

const int MaxLine = 1024;
const int MaxNum = 1000000000;

int aux[2][MaxLine];
char buf[MaxLine];
map<string, int> dict;
int n;
int s;
int q;

int main()
{
    fgets(buf, MaxLine, stdin);
    n = atoi(buf);
    for (int index = 1; index <= n; ++index)
    {
        fgets(buf, MaxLine, stdin);
        s = atoi(buf);
        dict.clear();
        for (int i = 0; i < s; ++i)
        {
            fgets(buf, MaxLine, stdin);
            buf[strlen(buf)-1] = '\0';
            dict[buf] = i;
        }

        fgets(buf, MaxLine, stdin);
        q = atoi(buf);
        
        int *x = aux[0];
        int *y = aux[1];
        fill_n(x, s, 0);
        for (int i = 1; i <= q; ++i)
        {
            fgets(buf, MaxLine, stdin);
            buf[strlen(buf)-1] = '\0';
            int id = dict[buf];

            for (int j = 0; j < s; ++j)
            {
                y[j] = MaxNum;

                if (j == id)
                    continue;

                for (int k = 0; k < s; ++k)
                {
                    int tmp = x[k] + (j != k);
                    if (tmp < y[j])
                        y[j] = tmp;
                }
            }

            swap(x, y);
        }

        printf("Case #%d: %d\n", index, *min_element(x, x + s));
    }

    return 0;
}