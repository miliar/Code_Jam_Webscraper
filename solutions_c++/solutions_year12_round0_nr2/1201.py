#include <cstdio>
#include <algorithm>
using namespace std;

int main2()
{
    int nb, surprise, mini;
    scanf("%d%d%d", &nb, &surprise, &mini);
    
    int tab[nb];
    for (int i=0; i<nb; i++)
        scanf("%d", &tab[i]);
    sort(tab, tab + nb);
    
    int res = 0;
    for (int i=0; i<nb; i++)
    {
        if (tab[i]/3 + (tab[i]%3 != 0) >= mini)
        {
            res++;
            continue;
        }
        if (tab[i]/3 != 0 && tab[i]%3 == 0 && tab[i]/3 + 1 >= mini && surprise > 0)
        {
            res++;
            surprise--;
            continue;
        }
        if (tab[i]%3 == 2 && tab[i]/3 + 2 >= mini && surprise > 0)
        {
            res++;
            surprise--;
            continue;
        }
    }
    
    printf("%d\n", res);
    return 0;
}

int main()
{
    int N;
    scanf("%d", &N);
    for (int i=0; i<N; i++)
    {
        printf("Case #%d: ", i+1);
        main2();
    }
}
