#include <fstream>
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
        int megoldas = 0 ;
        int opos=1 ;
        int bpos=1 ;
        int outso = 0;
        int butso = 0 ;
        int darab ;
        bef >> darab ;
        for (int i = 0; i < darab; i++)
        {
            string c ;
            int p ;
            bef >> c >> p ;
            if (c == "O")
            {
                outso += (p > opos) ? p - opos : opos - p ;
                if (outso < butso) outso = butso ;
                outso++ ; // Megnyomja
                opos = p ;
            }
            if (c == "B")
            {
                butso += (p > bpos) ? p - bpos : bpos - p ;
                if (butso < outso) butso = outso ;
                butso++ ; // Megnyomja
                bpos = p ;
            }
        }
        megoldas = (butso > outso) ? butso : outso ;
        kif << "Case #" << t << ": " ;
        kif << megoldas << endl ;
    }

    bef.close() ;
    kif.close() ;
    return 0;
}
