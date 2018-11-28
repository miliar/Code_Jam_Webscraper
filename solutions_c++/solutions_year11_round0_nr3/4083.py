#include <cstdio>
#include <math.h>
#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
using namespace std;

int TC = 1, T, N;
int seanadd(int a, int b);
int main ()
{
 std::ofstream os("C.txt");
    for (scanf ("%d", &T); TC <= T; TC++)
    {
        scanf ("%d", &N);
        int zahlen[N];
        for (int i=0;i<N;i++)
        {
            int zahl;
            scanf("%d", &zahl);
            zahlen[i]=zahl;
            }
        os<<"Case #"<<TC<<": ";
        //printf ("Case #%d: ", TC);
        //puts ((K + 1) % (1 << N) == 0 ? "ON" : "OFF");
    int ergebnis=0;
    int hoch=0;
    for (int i=0;i<N;i++)
    {
        ergebnis^=zahlen[i];
    }
    if (ergebnis!=0)os<<"NO\n";
    else
    {
        for (int i=1;i<pow(2,N)-1;i++)
        {
            int ergebnis1=0;
            int ergebnis2=0;
            int summe1=0;
            int summe=0;
            for (int j=0;j<N;j++)
            {
                if ((i>>j)%2==1){ergebnis1^=zahlen[j];summe1+=zahlen[j];}
                else ergebnis2^=zahlen[j];
                summe+=zahlen[j];
            }
            if (ergebnis1==ergebnis2){
                                     if(summe1>hoch)hoch=summe1;else if (summe-summe1>hoch)hoch=summe-summe1;
                                     }
            
        }
        ergebnis=hoch;
        if (ergebnis==0)os<<"NO\n";
        else os<<ergebnis<<"\n";
        //cout<<hoch;
        //printf("%d",ergebnis);
    }
}
    getch();
    return 0;
}
