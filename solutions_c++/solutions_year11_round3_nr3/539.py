#include <iostream>
#include <cstdio>

using namespace std;

int nbTest, nbFreq;
int freqs[10000];
int low, high;

int main()
{
    freopen("small.in", "r", stdin);
    freopen("small.out", "w", stdout);

    scanf("%d", &nbTest);
    bool trouve, divise;


    for (int test = 1; test <= nbTest; test++)
    {
        scanf("%d", &nbFreq);
        scanf("%d %d", &low, &high);

        for (int k = 0; k < nbFreq; k++)
            scanf("%d", &freqs[k]);

        trouve = false;

        for (int i = low; i <= high && !trouve; i++)
        {
            divise = true;
            for (int k = 0; k < nbFreq && divise; k++)
                if (i%freqs[k] != 0 && freqs[k]%i != 0)
                    divise = false;

            trouve = divise;
            if (divise)
                printf("Case #%d: %d\n", test, i);
        }

        if (!trouve)
                printf("Case #%d: NO\n", test);


    }


    return 0;
}
