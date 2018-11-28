#include<algorithm>
#include<cmath>
#include<iomanip>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>
#include<iostream>
#include<fstream>
#include<string>

using namespace std;

#define forn(i,n) for(int i = 0; i < (n); i++)
#define dforn(i,n) for(int i = (int)(n-1); i >= 0; i--)
#define all(v) v.begin(), v.end()
#define pb push_back

string pals[5000];
set<char> palabras[15];

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    string st;
    int l,d,n;
    fin >> l >> d >> n;
    forn(i,d)
        fin >> pals[i];
    int caso=0;
    forn(j,n)
    {
        forn(i,l)
            palabras[i].clear();
        caso++;
        int res = 0;
        fin >> st;
        int cant = 0;
        bool p = false;
        forn(i,st.size())
        {
            if(st[i]=='(')
            {
                p = true;
            }
            else if(st[i]==')')
            {
                p = false;
                cant++;
            }
            else
            {
                palabras[cant].insert(st[i]);
                if(p==false)
                    cant++;
            }
        }
        forn(i,d)
        {
            bool p = true;
            forn(ii,l)
            {
                if(palabras[ii].find(pals[i][ii])==palabras[ii].end())
                {
                    p = false;
                    break;
                }
            }
            if(p==true)
                res++;
        }
        fout << "Case #" << caso << ": " << res << endl;
    }
}
