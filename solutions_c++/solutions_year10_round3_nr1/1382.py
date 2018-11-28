#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

#define ecrire(a) cout<<a<<endl;
#define FOR(a,c,b) for(int a=c;a<b;a++)
#define ALL(c) (c).begin(), (c).end()

typedef struct paire
{
    float a,b;
}paire;

bool pas_dans_tableau(float a,vector <paire> tab,int longueur)
{
    FOR(c,0,longueur)
    {
        if(abs(tab[c].a-a)<=0.01&&tab[c].b!=0)
        {
            return false;
        }
    }
    return true;
}

bool pas_dans_tableau2(float a,float b, vector <paire> tab,int longueur)
{
    FOR(c,0,longueur)
    {
        if((a==tab[c].a&&b==tab[c].b)||(b==tab[c].a&&a==tab[c].b))
        {
            return false;
        }
    }
return true;
}

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");
    int nb_cas;
    in>>nb_cas;

    int nb_wires;
    float A,B;
    vector<paire> tab;
    vector<paire> tab2;
    paire p,p2;

    int total;
    //cout<<nb_cas<<endl;
    FOR(c,0,nb_cas)
    {
        in>>nb_wires;
        total=0;
        tab.resize(0);
        tab2.resize(0);
        FOR(c2,0,nb_wires)
        {
            in>>A>>B;
            if(tab.size()==0)
            { p.a=A;
                p.b=B;
                p2.a=A/B;
                p2.b=0;
                tab.push_back(p2);
                tab2.push_back(p);
            }
            else if(pas_dans_tableau2(A,B,tab2,tab2.size()))
            {
                p.a=A;
                p.b=B;
                tab2.push_back(p);
                if(pas_dans_tableau((A+B)/2,tab,tab.size()))
            {
                 p2.a=A/B;
                p2.b=0;
                tab.push_back(p2);
                FOR(c3,0,(tab2.size()-1))
                {
                    if(((tab2[c3].a<A&&tab2[c3].b>B)||(tab2[c3].a>A&&tab2[c3].b<B)))
                    {

                        tab[tab.size()-1].b=1;
                        tab[c3].b=1;
                        total++;
                    }
                }
            }
            }
        }
        out<<"Case #"<<c+1<<": "<<total<<endl;
    }
    return 0;
}
