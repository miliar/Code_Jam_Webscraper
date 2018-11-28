#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>

using namespace std;

const long long INF = 213456789012345 ;

int main()
{
    ifstream bef ;
    ofstream kif ;
    bef.open("be.txt") ;
    kif.open("ki.txt") ;

    int tdb ;
    bef >> tdb ;

    for (int t = 1; t <= tdb; t++)
    {
        int c = 0 ;
        int d = 0 ;
        bef >> c >> d;
        int pontok[200] ;
        int darab[200] ;
        int sum = 0 ;

        for (int i = 0; i < c; i++)
        {
            bef >> pontok[i] >> darab[i] ;
            sum += darab[i] ;
        }

        // Bináris keresés

        double a = 0 ;
        double b = (double)sum * d ;
        while ((b - a) > .0000001) // 10^-7
        {
            double fele = (b + a) / 2 ;
            bool jo = true ;

            double jobbszel = -INF;
            for (int i = 0; i < c; i++)
            {
                if (pontok[i] - jobbszel - d >= fele)
                {
                    jobbszel = pontok[i] - fele - d;
                }
                jobbszel += darab[i] * d ;
                if (jobbszel - pontok[i] > fele)
                {
                    jo = false ;
                    break ;
                }
            }


            if (jo)
            {
                b = fele ;
            }
            else
            {
                a = fele ;
            }
        }

        kif << "Case #" << t << ": " << a ;
        kif << endl ;
    }

    bef.close() ;
    kif.close() ;
    return 0;
}
