#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <map>

using namespace std;

#define TESTING

#define MIN(x, y) ((x) < (y)) ? (x) : (y)

int main()
{
#ifdef TESTING
    FILE *f = freopen("sample.in", "r", stdin);
    FILE *fout = freopen("result.out", "w", stdout);
#endif

    int num_case;
    scanf("%d", &num_case);

    int s[20];

    map<int, int> m;
    int n_count;
    for (int i = 0 ; i < num_case ; ++i)
    {
        scanf("%d", &n_count);
        m.clear();

        for (int j = 0 ; j < 20 ; ++j)
        {
            scanf("%d", &s[j]);
        }
        
        int shift = 0;
        for (int shift = 0 ; shift <= 0xfffff ; ++shift)
        {
            int sum = 0;
            for (int j = 0 ; j < 20 ; ++j)
            {
                int tmp = 1 << j;
                if (shift & tmp)
                {
                    sum += s[j];
                }
            }

            if (m.find(sum) == m.end())
            {
                m[sum] = shift;
            }
            else
            {
                int o_shift = m[sum];
                if ((shift & o_shift) == 0)
                {
                    printf("Case #%d:\n", (i+1));

                    for (int j = 0 ; j < 20 ; ++j)
                    {
                        int tmp = 1 << j;
                        if (shift & tmp)
                        {
                            printf("%d ", s[j]);
                        }
                    }
                    printf("\n");

                    for (int j = 0 ; j < 20 ; ++j)
                    {
                        int tmp = 1 << j;
                        if (o_shift & tmp)
                        {
                            printf("%d ", s[j]);
                        }
                    }
                    printf("\n");


                    goto exit;
                }
            }
        }

        printf("Case #%d: Impossible\n", (i+1));
exit:
        int a = 10;
    }

#ifdef TESTING
    fclose(f);
    fclose(fout);
#endif

    return 0;
}