#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

#define forn(i,n) for(int i=0;i<(n);i++)

int main()
{
    map <string,int> m;    
    int n;
    cin >> n;
    forn(casos,n)
    {
        m.clear();
        int s,q;
        cin >> s;
        string cad;
        getline(cin,cad);
        int numero = 0;
        forn(i,s)
        {
           getline(cin,cad);
           m[cad] = numero;
           numero++;
        }
        vector <bool> v(s,false);
        int libres = s, coste = 0;
        cin >> q;
        getline(cin,cad);
        forn(i,q)
        {
            getline(cin,cad);
            numero = m[cad];
            if (!v[numero])
            {
               libres--;
               if (libres == 0)
               {
                  coste++;
                  libres = s - 1;
                  v = vector<bool>(s,false);
               }
               v[numero] = true;               
            }
        }
        cout << "Case #" << casos+1 << ": " << coste << endl;
    }
    return 0;
}
