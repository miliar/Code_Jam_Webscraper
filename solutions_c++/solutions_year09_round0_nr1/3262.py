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

vector< vector<char> > parser(string cad)
{
    vector<char> vc;
    vector< vector<char> > vvc;
    int i=0;
    bool par=false;
    while (i<cad.length())
    {
        if (cad[i]=='(')
            par=true;
        else
            if (cad[i]==')')
            {
                par=false;
                vvc.pb(vc);
                vc.clear();

            }
            else //es una letra
            {
                vc.pb(cad[i]);
                if (!par)
                {
                    vvc.pb(vc);
                    vc.clear();
                }
            }
        i++;
    }

    return vvc;
}

bool tieneChar(vector<char> vec, char c)
{
    int i=0;
    while (i<vec.size())
    {
        if (vec[i]==c)
            return true;
        i++;
    }
    return false;
}

bool tieneStr(vector< vector<char> > vc, string cad)
{
    for (int i=0; i<cad.length(); i++)
    {
        if (!tieneChar(vc[i],cad[i]))
            return false;
    }
    return true;
}

bool esta(vector<string> vec, string cad)
{
    int i=0;
    while (i<vec.size())
    {
        if (vec[i]==cad)
            return true;
        i++;
    }
    return false;
}

int main(int argc, char** args) {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    vector<string> vec;
    int l,d,n;
    string cad;
    cin>>l>>d>>n;
    
    for (int x=0; x<d; x++)
    {
        cin>>cad;
        vec.push_back(cad);
    }
    for (int x=0; x<n; x++)
    {
        cin>>cad;
        if (cad.length()==l)
        {
            if (esta(vec,cad))
                cout<<"Case #"<<x+1<<": 1"<<endl;
            else
                cout<<"Case #"<<x+1<<": 0"<<endl;
        }
        else
            if (cad.length()<l)
                cout<<"Case #"<<x+1<<": 0"<<endl;
            else
            {
                int numA=0;

                vector< vector<char> > aux = parser(cad);
                for (int i=0; i<d; i++)
                {
                    if (tieneStr(aux,vec[i]))
                        numA++;
                }

                cout<<"Case #"<<x+1<<": "<<numA<<endl;
            }
    }
    return 0;
}
