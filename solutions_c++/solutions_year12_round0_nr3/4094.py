#include <iostream>
#include <fstream>
#include <set>
#include <math.h>
using namespace std;

int nbpos(int a) { if (a==0)return 1 ;else {int digits = 0;while (a != 0) { a /= 10; digits++; } return digits ; } } ;
int main()
{
    freopen("a.in", "rt", stdin);
    freopen("a.out", "wt", stdout);
    int T, A, B, sauvi, nb, res ;
    set<int> mySet;

    cin >>T;
    for(int indice=1; indice<=T; indice++){
        cin >> A >> B;
        res =0 ;
        nb =nbpos(A) ;

        for (int i=A; i<=B; i++) {
            mySet.clear();
            sauvi =i;
            mySet.insert(sauvi) ;
            for (int j=0; j<nb-1; j++) {
                sauvi = sauvi/10 + (sauvi%10) * pow(10, nb-1) ;
                if ( mySet.find(sauvi)==mySet.end() ) {
                    if (nbpos(sauvi) == nb  && sauvi != i && sauvi>=A && sauvi <=B && i < sauvi )
                        res++ ;
                }
                mySet.insert(sauvi) ;
            }
        }

        cout <<"Case #" << indice<< ": " <<  res << endl ;
    }
    return 0;
}
