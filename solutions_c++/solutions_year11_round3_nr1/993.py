#include <cstdio>
#include <math.h>
#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <iomanip>
using namespace std;

int TC = 1, T, R, C;
int main ()
{
    FILE * p;

  p = fopen ("3Asource.txt","r+");
  std::ofstream os("3A.txt");
    for (fscanf (p,"%d", &T); TC <= T; TC++)
    {
        //Input
        fscanf (p,"%d %d", &R, &C);
        char zeichen[R][C];
        for (int i=0;i<R;i++)
        {
            char zeichen1[C];
            fscanf(p,"%s", &zeichen1);
            for (int j=0;j<C;j++)
            {
                zeichen[i][j]=zeichen1[j];
            }
        }
        os<<"Case #"<<TC<<":\n";
        //Berechnen
        for (int i=0;i<R-1;i++)
        {
            for (int j=0;j<C-1;j++)
            {
                if (zeichen[i][j]=='#'&&zeichen[i+1][j]=='#'&&zeichen[i][j+1]=='#'&&zeichen[i+1][j+1]=='#')
                {
                   zeichen[i][j]='/';
                   zeichen[i+1][j]='\\';
                   zeichen[i][j+1]='\\';
                   zeichen[i+1][j+1]='/';
                }
            }
        }
        bool geloest=true;
        for (int i=0;i<R;i++)
        {
          for (int j=0;j<C;j++)
          {
            if (zeichen[i][j]=='#'){geloest=false;break;}
          }
          if (geloest==false){break;}
        }
        if (geloest==false)os<<"Impossible\n";    
        else
        {
        //Ausgabe
                 for (int i=0;i<R;i++)
                 {
                  for (int j=0;j<C;j++)
                  {
                   os<<zeichen[i][j];
                   }
                   os<<"\n";
                   }
        }
    }
    getch();
    return 0;
}
