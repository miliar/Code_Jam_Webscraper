#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>

using namespace std;

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
        int csapatszam ;
        bef >> csapatszam ;
        int meccsek[100][100] ;
        double wp[100] ;
        double owp[100] ;
        double oowp[100] ;
        int jatszott[100] ;
        for (int i = 0; i < csapatszam; i++)
        {
            int win = 0 ;
            jatszott[i] = 0 ;
            for (int j = 0; j < csapatszam; j++)
            {
                char be ;
                bef >> be ;
//                cout << i << ":" << j << " = " << be << endl ;
                switch(be)
                {
                    case '0' : meccsek[i][j] = 0 ; jatszott[i]++ ; break ;
                    case '1' : meccsek[i][j] = 1 ; win++ ; jatszott[i]++ ; break ;
                    case '.' : meccsek[i][j] = 2 ; break ;
                }
            }
            wp[i] = (double)win/jatszott[i] ;
        }

        for (int i = 0; i < csapatszam; i++)
        {
            double sum = 0;
            int db = 0;
            for (int j = 0; j < csapatszam; j++)
            {
                if (meccsek[i][j] != 2)
                {
                    db++ ;
                    if (meccsek[i][j] == 1)
                    {
                        sum += wp[j]*jatszott[j]/(jatszott[j]-1) ;
                    }
                    else
                    {
                        sum += (wp[j]*jatszott[j]-1)/(jatszott[j]-1) ;
                    }
                }
            }
            owp[i] = sum / db ;
        }

        for (int i = 0; i < csapatszam; i++)
        {
            double sum = 0;
            int db = 0;
            for (int j = 0; j < csapatszam; j++)
            {
                if (meccsek[i][j] != 2)
                {
                    db++ ;
                    sum += owp[j] ;
                }
            }
            oowp[i] = sum / db ;
        }




        kif << "Case #" << t << ":" << endl ;
        for (int i = 0; i < csapatszam; i++)
        {
            kif << (wp[i] * .25 + .5*owp[i] + .25*oowp[i]) << endl ;
        }
    }

    bef.close() ;
    kif.close() ;
    return 0;
}
