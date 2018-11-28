#include <cstdio>
#include <math.h>
#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <iomanip>
using namespace std;

int TC = 1, T, N, L, H;
int main ()
{
    FILE * p;

  p = fopen ("3Csource.txt","r+");
  std::ofstream os("3C.txt");
    for (fscanf (p,"%d", &T); TC <= T; TC++)
    {
        //Input
        fscanf (p,"%d %d %d", &N, &L, &H);
        int freqs[N];
        for (int i=0;i<N;i++)
        {
            int zahl;
            fscanf(p,"%d", &zahl);
            freqs[i]=zahl;
        }
        os<<"Case #"<<TC<<": ";
        //Berechnen
        bool gefunden=true;
        for (int i=L;i<=H;i++)
        {
            gefunden=true;
            for (int j=0;j<N;j++)
            {
                if (!(freqs[j]%i==0||i%freqs[j]==0)){gefunden=false;break;}
            }
            if (gefunden){os<<i<<"\n";break;}
        }
        if (!gefunden)os<<"NO\n";
        //Ausgabe
    }
    getch();
    return 0;
}
