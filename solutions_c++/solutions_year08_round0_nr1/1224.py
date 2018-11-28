//---------------------------------------------------------------------------
#include <cstdio>
#include <string>
#include <iostream>
using namespace std;
const int INF=1000000;
int S,Q;
string Przegladarki[100];
string Zapytania[1000];
// tab[s][q]
// oznacza liczbe zmian przy ustawionej przegladarce nr s zaczynajac od
// pytania nr q i kontynujac zapytania az do ostatniego query
int tab[100][1001];
void piszP()
{
    for(int i=0; i<S; i++)
        printf("%s\n", Przegladarki[i].c_str());
}
void piszZ()
{
    for(int i=0; i<Q; i++)
        printf("%s\n", Zapytania[i].c_str());
}
void wczytajDane()
{
    scanf("%d", &S);
    char nazwa[102];
    gets(nazwa); // dla '\n'
    for(int i=0; i<S; i++)
    {
        gets(nazwa);
        Przegladarki[i].assign(nazwa);
    }
    //piszP();
    scanf("%d", &Q);
    gets(nazwa); // dla '\n'
    for(int i=0; i<Q; i++)
    {
        gets(nazwa);
        Zapytania[i].assign(nazwa);
    }
    //piszZ();
    for(int i=0; i<S; i++) for(int j=1; j<=Q; j++) tab[i][j]=-1;
}
int licz(int s, int q)
{
    if(q>Q) return 0;
    if(tab[s][q]!=-1)
        return tab[s][q];

    int zmiany=0;
    int _min=INF;
    if(Przegladarki[s]==Zapytania[q-1])
    {
        zmiany++;
        for(int i=0; i<S; i++)
        {
            if(i==s) continue;
            _min=min(_min, licz(i, q));
        }
        
    }
    else
    {
        _min=licz(s, q+1);
    }
    tab[s][q]=zmiany+_min;
    return tab[s][q];
}
void piszT()
{
    for(int s=0; s<S; s++)
    {
        for(int q=1; q<=Q; q++)
            printf("%d ", tab[s][q]);
        printf("\n");
    }
}
int main()
{
    int N;
    scanf("%d", &N);
    for(int __i=1; __i<=N; __i++)
    {
        wczytajDane();
        if(Q==0)
        {
            printf("Case #%d: 0\n", __i);
            continue;
        }
        int rez=INF;
        for(int i=0; i<S; i++)
            rez=min(rez, licz(i, 1));
        //piszT();
        printf("Case #%d: %d\n", __i, rez);
    }
    //system("pause");
    return 0;
}
//---------------------------------------------------------------------------
 