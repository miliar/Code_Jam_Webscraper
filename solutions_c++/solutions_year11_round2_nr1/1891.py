#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;
#define MAX 110
typedef struct
{
    double win;
    double play;
    double owp;
    double wp;
    double oowp;
}tipotab;
int g,n,t;
char mat[MAX][MAX];
tipotab tab[MAX];
void calcula()
{
    //calcular las victorias de todos
    for (int i=1; i<=n; i++)
    {
        for (int j=1; j<=n; j++)
        {
            if (mat[i][j]=='1')
            {
                tab[i].play++;
                tab[i].win++;
            }
            if (mat[i][j]=='0')
                tab[i].play++;
        }
    }
    //calcular por cada uno su OWP
    for (int i=1; i<=n; i++)
    {
        double owp=0;
        int us=0;
        for (int j=1; j<=n; j++)
        {
            if (mat[i][j]=='1')
            {
                us++;
                owp+=(tab[j].win/(tab[j].play-1));
            }
            else
            {
                if (mat[i][j]=='0')
                {
                    us++;
                    owp+=((tab[j].win-1)/(tab[j].play-1));
                }
            }
        }
        owp/=us;
        tab[i].owp=owp;
    }
    //calcular el OOWP
    for (int i=1; i<=n; i++)
    {
        double oowp=0;
        int us=0;
        for (int j=1; j<=n; j++)
        {
            if (mat[i][j]!='.')
            {
                us++;
                oowp+=(tab[j].owp);
            }
        }
        oowp/=us;
        tab[i].oowp=oowp;
    }
    double rpi;
    for (int i=1; i<=n; i++)
    {
        tab[i].wp=tab[i].win/tab[i].play;
        rpi=(.25*tab[i].wp)+(.50*tab[i].owp)+(.25*tab[i].oowp);
        //printf("%.7lf\n",rpi);
        cout<<rpi;
        printf("\n");
    }
}
int main()
{
    scanf("%d",&t);
    for (int g=1; g<=t; g++)
    {
        memset(tab,0,sizeof(tab));
        scanf("%d\n",&n);
        for (int i=1; i<=n; i++)
        {
            for (int j=1; j<=n; j++)
            {
                scanf("%c",&mat[i][j]);
            }
            scanf("\n");
        }
        printf("Case #%d:\n",g);
        calcula();
    }
}
