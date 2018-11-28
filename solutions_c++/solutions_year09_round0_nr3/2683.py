#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <cstdio>
#include <sstream>
#include <algorithm>
#include <cassert>
#include <cctype>
#include <cstdlib>
#include <cstring>
using namespace std;


#define forn(i,n) for (int i = 0; i < (int)(n); i++)
#define forsn(i,a,b) for (int i = (int)(a); i < (int)(b); i++)
#define dforsn(i,a,b) for (int i = (int)(b)-1; i >= (int)(a); i--)
#define si(c) ((int)(c).size())
#define decl(a,b) typeof b a = b
#define forall(it,c) for (decl(it,(c).begin()); it != (c).end(); it++)
#define dforall(it,c) for (decl(it,(c).rbegin()); it != (c).rend(); it++)
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define pb push_back
#define mp make_pair

typedef long long tint;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;
typedef vector<tint> vt;
typedef vector<vt> vvt;

void init() {
}

int b2(string cadena, string linea)
{
    if (cadena.length()>1)
    {
        if (linea.length()==1)
            return 0;
        else
            if (cadena[0]==linea[0])
            {
                return b2(cadena.substr(1,cadena.length()-1),linea.substr(1,linea.length()-1))+
                        b2(cadena,linea.substr(1,linea.length()-1));
            }
            else
                return b2(cadena,linea.substr(1,linea.length()-1));
    }
    else
    {
        if (cadena[0]==linea[0])
        {
            if (linea.length()==1)
                return 1;
            else
                return 1+ b2(cadena,linea.substr(1,linea.length()-1));
        }
        else
        {
            if (linea.length()==1)
                return 0;
            else
                return b2(cadena,linea.substr(1,linea.length()-1));
        }
    }
}

int buscar(string cadena)
{
    return b2("welcome to code jam",cadena);
}

void imprimir(int num, int ind)
{
    if (ind!=4)
    {
        int n=num%10;
        imprimir(num/10,ind+1);
        cout<<n;
    }
}


int main(int argc, char** args) {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int n;
    string cad;

    cin>>n;
    getline(cin,cad);

    for (int i=0; i<n; i++)
    {
        int num;
        getline(cin,cad);
        num=buscar(cad);
        cout<<"Case #"<<i+1<<": ";
        imprimir(num,0);
        cout<<endl;
    }

    return 0;
}