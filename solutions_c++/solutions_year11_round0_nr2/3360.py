#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

struct tcsere
{
    char c1, c2, c3 ;
};

struct thalal
{
    char c1, c2 ;
};

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
        int csereszam ;
        int halalszam ;
        int hossz ;
        string szoveg ;
        vector<tcsere> csere ;
        vector<thalal> halal ;
        vector<char> maradek ;

        bef >> csereszam ;
        for (int i = 0; i < csereszam; i++)
        {
            string cserestr ;
            bef >> cserestr ;
            tcsere cs ;
            cs.c1 = cserestr[0] ;
            cs.c2 = cserestr[1] ;
            cs.c3 = cserestr[2] ;
            csere.push_back(cs) ;
        }

        bef >> halalszam ;
        for (int i = 0; i < halalszam; i++)
        {
            string halalstr ;
            bef >> halalstr ;
            thalal h ;
            h.c1 = halalstr[0] ;
            h.c2 = halalstr[1] ;
            halal.push_back(h) ;
        }

        bef >> hossz ;
        bef >> szoveg ;

        maradek.push_back(' ') ; // Strázsa

        for (int i = 0; i < szoveg.size(); i++)
        {
            bool vege = false ;
            for (int j = 0; j < csere.size(); j++)
            {
                if ((maradek[maradek.size()-1] == csere[j].c1 && szoveg[i] == csere[j].c2) ||
                    (maradek[maradek.size()-1] == csere[j].c2 && szoveg[i] == csere[j].c1))
                {
                    maradek[maradek.size()-1] = csere[j].c3 ;
                    vege = true ;
                    break ; // Nem-bázis elem lesz belőle, az meg nem alkothat már mást.
                }
            }

            if (!vege)
            {
                for (int j = 0; j < halal.size(); j++)
                {
                    for (int k = 0; k < maradek.size(); k++)
                    {
                        if ((maradek[k] == halal[j].c1 && szoveg[i] == halal[j].c2) ||
                            (maradek[k] == halal[j].c2 && szoveg[i] == halal[j].c1))
                        {
                            maradek.clear() ;
                            maradek.push_back(' ') ;
                            vege = true ;
                            break ;
                        }
                    }
                    if (vege)
                    {
                        break ;
                    }
                }
            }
            if (!vege)
            {
                maradek.push_back(szoveg[i]) ;
            }
        }

        kif << "Case #" << t << ": [" ;
        for (int i = 1; i < maradek.size(); i++) // Strázsa miatt
        {
            if (i != maradek.size()-1)
            {
                kif << maradek[i] << ", " ;
            }
            else
            {
                kif << maradek[i] ;
            }
        }
        kif << "]" << endl ;
    }

    bef.close() ;
    kif.close() ;
    return 0;
}
