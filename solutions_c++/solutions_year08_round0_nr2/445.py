#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define forn(i,n) for(int i=0;i<(n);i++)

int resol(vector <int> &salida, vector <int> &llegada)
{
    sort(salida.begin(),salida.end());
    sort(llegada.begin(),llegada.end());
    int trenes = 0;
    int j = 0;
    int disponibles = 0;
    forn(i,salida.size())
    {
       while (j < llegada.size() && llegada[j] <= salida[i])
       {
        disponibles++;
        j++;
       }
       if (disponibles)
        disponibles--;
       else
        trenes++;
    }
    return trenes;
}

int main()
{
    int n;
    cin >> n;
    forn(casos, n)
    {
       int t;
       cin >> t;
       int na,nb;
       cin >> na >> nb;
       vector <int> la,sa,lb,sb;
       la.reserve(nb);
       sa.reserve(na);
       lb.reserve(na);
       sb.reserve(nb);                     
       forn(i,na)
       {
           int h,m, r;
           scanf("%d:%d",&h,&m);
           r = h * 60 + m;
           sa.push_back(r);
           scanf("%d:%d",&h,&m);
           r = h * 60 + m;
           lb.push_back(r + t);
       }
       forn(i,nb)
       {
           int h,m, r;
           scanf("%d:%d",&h,&m);
           r = h * 60 + m;
           sb.push_back(r);
           scanf("%d:%d",&h,&m);
           r = h * 60 + m;
           la.push_back(r+t);
       }
       cout << "Case #" << casos+1 << ": " << resol(sa,la) << " " << resol(sb,lb) << endl;
    }
    return 0;
}
