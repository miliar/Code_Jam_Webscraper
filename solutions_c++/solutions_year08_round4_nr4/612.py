#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

#define forn(i,n) for(int i=0;i<(n);i++)

int coste(string &s)
{
    char ulti = '#';
    int cuenta = 0;
    forn(i,s.size())
     if (s[i] != ulti)
     {
       ulti = s[i];
       cuenta++;
     }
    return cuenta;
}

int main()
{
    int N;
    cin >> N;
    forn(casos,N)
    {
       int k;
       string s;
       cin >> k >> s;
       vector <int> v(k);
       int minimo = s.size();
       forn(i,k)
         v[i] = i;
       do
       {
         string r;
         r.resize(s.size());
         forn(i,s.size()/k)
         {
            int base = i*k;
            forn(j,k)
             r[base+j] = s[base+v[j]];
         }
         minimo = min(minimo,coste(r));
       }
       while (next_permutation(v.begin(),v.end()));
       cout << "Case #" << casos+1<<": " << minimo << endl;
    }
    return 0;
}
