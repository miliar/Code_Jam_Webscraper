#include <iostream>
#include <vector>

using namespace std;

#define forn(i,n) for(int i=0;i<(n);i++)
#define forab(i,a,b) for(int i=(a);i<(b);i++)

vector<int> ar;
vector<int> cam;
int m,tope;

int tabla[11000][2][2];

int mini(int n,int v);

int minifijo(int n,int v, int c)
{
    if (tabla[n][v][c] != 0)
      return tabla[n][v][c]-1;
    int mm = 1000000000;
    if (ar[n] == 1)
    {
        if (v == 0)
        {
              mm = min(mm,mini(2*n,0) + mini(2*n+1,0));
              mm = min(mm,mini(2*n,1) + mini(2*n+1,0));
              mm = min(mm,mini(2*n,0) + mini(2*n+1,1));
        }
        else
        {
              mm = min(mm,mini(2*n,1) + mini(2*n+1,1));
        }
    }
    else
    {
        if (v == 0)
        {
              mm = min(mm,mini(2*n,0) + mini(2*n+1,0));
        }
        else
        {
              mm = min(mm,mini(2*n,1) + mini(2*n+1,0));
              mm = min(mm,mini(2*n,0) + mini(2*n+1,1));
              mm = min(mm,mini(2*n,1) + mini(2*n+1,1));
        }
    }
//    cout << n << " " << v <<" " << c << " " << mm << endl;
    tabla[n][v][c] = mm+1;
    return mm;
}

int mini(int n,int v)
{
    if (n >= tope)
    {
//      cout <<"HOJA " << n << " " << v << " " << ((ar[n] == v)?(0):(1000000000)) << endl;
      return (ar[n] == v)?(0):(1000000000);
    }
    int mm = 1000000000;
    mm = min(mm,minifijo(n,v,0));
    if (cam[n] == 1)
    {
      ar[n] = 1 - ar[n];
      mm = min(mm,1+minifijo(n,v,1));
      ar[n] = 1 - ar[n];      
    }
    return mm;
}

int main()
{
    int N;
    cin >> N;
    forn(casos,N)
    {
        memset(tabla,0,sizeof(tabla));                 
        int v;
        cin >> m >> v;
        ar  = vector<int>(m+1);
        cam = vector<int>(m+1);        
        forn(i,(m-1)/2)
          cin >> ar[i+1] >> cam[i+1];
        tope = (m-1)/2+1;
        forab(i,tope,m+1)
          cin >> ar[i];
        int minimo = mini(1,v);
        cout << "Case #" << casos+1<<": ";
        if (minimo < 1000000000)
          cout << minimo;
        else
          cout << "IMPOSSIBLE";
        cout << endl;
    }
    return 0;
}
