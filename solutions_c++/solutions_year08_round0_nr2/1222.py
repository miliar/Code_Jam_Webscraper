//---------------------------------------------------------------------------
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <iostream>
using namespace std;
typedef pair<int,int> Godzina;
// zwrocic uwage, ze moge stworzyc "next day"
// zauwazyc, ze "next day" wystapic moze tylko
// przy obliczeniu gotowosci do nastepnego wyjazdu
ostream& operator<<(ostream& o, const Godzina& g)
{
    return o<<g.first<<":"<<g.second;
}
void DodajMinuty(Godzina& g, int minuty)
{
    int min=g.second+minuty;
    g.second=min%60;
    g.first+=(min/60);
}
void wczytajGodzine(Godzina& g)
{
    /*int h1, h2, m1,m2;
    scanf("%d%d:%d%d", &h1,&h2,&m1,&m2);
    g.first=h1*10+h2;
    g.second=h1*10+h2;
    */
    int h,m;
    scanf("%d:%d", &h,&m);
    g.first=h;
    g.second=m;
}
struct Zdarzenie
{
    int ileAodjazd;
    int ileAprzyjazd;
    int ileBodjazd;
    int ileBprzyjazd;

    Zdarzenie()
    {
        ileAodjazd=ileAprzyjazd=ileBodjazd=ileBprzyjazd=0;
    }
};
int T, NA, NB;
map<Godzina, Zdarzenie> zdarzenia;
void wczytaj()
{
    scanf("%d%d%d", &T, &NA, &NB);
    zdarzenia.clear();
    for(int i=0; i<NA; i++)
    {
        Godzina g1, g2;
        wczytajGodzine(g1);
        wczytajGodzine(g2);
        zdarzenia[g1].ileAodjazd++;
        zdarzenia[g2].ileBprzyjazd++;
    }
    for(int i=0; i<NB; i++)
    {
        Godzina g1,g2;
        wczytajGodzine(g1);
        wczytajGodzine(g2);
        zdarzenia[g1].ileBodjazd++;
        zdarzenia[g2].ileAprzyjazd++;
    }

}
int main(int argc, char* argv[])
{
    int N;
    scanf("%d", &N);
    for(int __n=1; __n<=N; __n++)
    {
        wczytaj();
        multiset<Godzina> pociagiA, pociagiB;

        int rezA=0, rezB=0;
        map<Godzina,Zdarzenie>::iterator it=zdarzenia.begin();
        for(; it!=zdarzenia.end(); ++it)
        {
            /*
            cout<<it->first<<"||"<<it->second.ileAodjazd<<' '<<it->second.ileAprzyjazd
                <<' '<<it->second.ileBodjazd<<' '<<it->second.ileBprzyjazd<<endl;
            */
            int __aPrzyj=it->second.ileAprzyjazd;
            
            for(int i=0; i<__aPrzyj; i++)
            {
                Godzina g=it->first;
                DodajMinuty(g, T);
                pociagiA.insert(g);
            }
            if(it->second.ileAodjazd>0)
            {
                // zalozenie: jestli multizbior jest pusty, to: .begin()==.end()
                multiset<Godzina>::iterator itA=pociagiA.begin();
                while(itA!=pociagiA.end() && *(itA)<=it->first && it->second.ileAodjazd>0)
                {
                    it->second.ileAodjazd--;
                    multiset<Godzina>::iterator temp=itA;
                    ++itA;
                    pociagiA.erase(temp);
                }
                rezA+=it->second.ileAodjazd;

            }
            
            ////////////////////////////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////
            int __bPrzyj=it->second.ileBprzyjazd;
            for(int i=0; i<__bPrzyj; i++)
            {
                Godzina g=it->first;
                DodajMinuty(g,T);
                pociagiB.insert(g);
            }
            if(it->second.ileBodjazd>0)
            {
                // zalozenie: jestli multizbior jest pusty, to: .begin()==.end()
                multiset<Godzina>::iterator itB=pociagiB.begin();
                while(itB!=pociagiB.end() && *(itB)<=it->first && it->second.ileBodjazd>0)
                {
                    it->second.ileBodjazd--;
                    multiset<Godzina>::iterator temp=itB;
                    ++itB;
                    pociagiB.erase(temp);
                }
                rezB+=it->second.ileBodjazd;
            }
            
        }
        printf("Case #%d: %d %d\n", __n, rezA, rezB);
    }
    //system("pause");
    return 0;
}
//---------------------------------------------------------------------------
 