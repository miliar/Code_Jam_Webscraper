#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

#ifdef DEBUG
#define dprintf(args...) printf(args)
#else
#define dprintf(args...)
#endif

char tabwysz[111][111];
char tabzap[1101][111];

int tabdyn[111];

int main(void)
{
    int ipr, npr;
    scanf("%d\n", &npr);
    for (ipr = 0; ipr < npr; ipr++)
    {
        int nWysz, nZap;
        int min = 0;
        scanf("%d\n", &nWysz);
        for (int i = 0; i < nWysz; i++)
        {
            fgets(tabwysz[i], 111, stdin);
            dprintf("wysz: '%s'\n", tabwysz[i]);
        }
        scanf("%d\n", &nZap);
        min = 0;
        memset(tabdyn, 0, sizeof(tabdyn));
        for (int i = 0; i < nZap; i++)
        {
            int j;
            fgets(tabzap[i], 111, stdin);
            dprintf("zap: '%s'\n", tabzap[i]);
            
            for (j = 0; j < nWysz; j++)
            {
                if (strcmp(tabwysz[j], tabzap[i]) == 0)
                {
                    int min = 0x7ffff;
                    for (int k = 0; k < nWysz; k++)
                        if (k != j)
                            min <?= tabdyn[k];
                    tabdyn[j] = min + 1;
                    dprintf("tabdyn[%d] <- %d\n", j, tabdyn[j]);
                    break;
                }
            }            
            if (j == nWysz)
                fprintf(stderr, "Not found!\n");
        }

        min = 0x7ffff;
        for (int j = 0; j < nWysz; j++)
            min <?= tabdyn[j];
        printf("Case #%d: %d\n", ipr+1, min);
    }
    return 0;
}
