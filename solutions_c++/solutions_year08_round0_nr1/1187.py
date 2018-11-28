#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

#define REP(i,n) for (int i = 0; i < (n); ++i)
#define VS vector < string >
#define VI vector < int >

string czytaj()
{
        char x[200];
        string s = "";
        gets(x);
        int poz = 0;
        while (x[poz] != '\0' && x[poz] != '\n')
        {
                s += x[poz++];
        }
        return s;
}

int tab[100][1000];
int kol[1000];

int wylicz(VI& x, VI& y)
{
        REP(i,x.size()) REP(j,y.size()) tab[i][j] = 0;
        REP(i,x.size())
        {
                int nast  = y.size();
                for (int j = y.size()-1; j >= 0; --j)
                {
                        if (y[j] == i) nast = j;
                        tab[i][j] = nast;
                }
                //REP(j,y.size()) printf("%d ", tab[i][j]); printf("\n");
        }
        //printf("\n");
        REP(j,y.size())
        {
                kol[j] = 0;
                int poz = -1;
                REP(i,x.size())
                {
                        if (tab[i][j] > poz)
                        {
                                poz = tab[i][j];
                                kol[j] = i;
                        }
                }
                //printf("%d ", kol[j]);
        }
        //printf("\n");
        int wyn = 0;
        int poz = tab[kol[0]][0];
        while (poz < y.size())
        {
                wyn++;
                poz = tab[kol[poz]][poz];
        }
        return wyn;
}

int main()
{
        int nnn;
        scanf("%d", &nnn);
        REP(iii,nnn)
        {
                int n, m;
                scanf("%d\n", &n);
                VS x, y;
                VI xx, yy;
                x.resize(n);
                xx.resize(n);
                REP(i,n)
                {
                        x[i] = czytaj();
                        xx[i] = i;
                        //printf("%s %d\n", x[i].c_str(), xx[i]);
                }
                scanf("%d\n", &m);
                y.resize(m);
                yy.resize(m);
                REP(i,m)
                {
                        y[i] = czytaj();
                        REP(j,n)
                        {
                                if (x[j] == y[i])
                                {
                                        yy[i] = j;
                                        break;
                                }
                        }
                        //printf("%s %d\n", y[i].c_str(), yy[i]);
                }
                printf("Case #%d: %d\n", iii+1, wylicz(xx,yy));
        }
        return 0;
};
