#include <iostream>

#define MAKS=1000

struct Line
{
    int y1,y2;
} tab[1000];

int t,n,wyn;

void Alg()
{
    for (int i=0;i<n;i++)
    {
        for (int j=i+1;j<n;j++)
        {
            if (tab[i].y1>tab[j].y1 && tab[i].y2<tab[j].y2)
                wyn++;
            else if (tab[i].y1<tab[j].y1 && tab[i].y2>tab[j].y2)
                wyn++;
        }
    }
}

int main()
{
    std::cin >> t;
    for (int i=1;i<=t;i++)
    {
        wyn=0;
        std::cin >> n;
        for (int j=0;j<n;j++)
        {
            std::cin >> tab[j].y1 >> tab[j].y2;
        }
        Alg();
        std::cout << "Case #" << i << ": " << wyn << '\n';
    }
}