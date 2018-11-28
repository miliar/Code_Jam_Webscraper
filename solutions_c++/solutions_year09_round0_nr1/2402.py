#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <utility>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

#define fori(i, n) for ( int i = 0; i < (n); ++i )
#define forr(i, a, b) for ( int i = (a); i <= (b); ++i )
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define printv(v) fori(i,v.sz) cout << v[i] << " "; cout << endl;
#define printm(m) fori(j,m.sz) {printv(m[j]);}

template<class T> string a2s(T x) { ostringstream o; o << x; return o.str(); }
template<class T> T s2a(string s) { istringstream i(s); T x; i >> x; return x; }

const double EPS = 1e-9;

int cmp(double x, double y = 0, double tol = EPS)
{
    return ( x <= y + tol ) ? ( x + tol < y ) ? -1 : 0 : 1;
}

vector<string> dic(5010);
int l, d, n, ind, r;
string s;
bool word, par;

int main()
{
    cin >> l >> d >> n;
    for(int i=0; i<d; i++)
    {
        cin >> dic[i];
    }

    for(int i=0; i<n; i++)
    {
        vector< vector<int> > txt(500, vector<int> (30,0));
        cin >> s;
        ind = 0;
        for(int j=0; j<s.size(); j++)
        {
            if(s[j]=='(')
            {
                par=true;
            }
            else if(s[j]==')')
            {
                ind++;
                par=false;
            }
            else if(par==false)
            {
                txt[ind][s[j]-'a'] = 1;
                ind++;
            }
            else
            {
                txt[ind][s[j]-'a'] = 1;
            }
        }

        r=0;
        for(int j=0; j<d; j++)
        {
            word=true;
            for(int k=0; k<l && word; k++)
            {
                if(txt[k][dic[j][k]-'a']==0) word=false;
            }
            if(word) r++;
        }

        cout << "Case #" << i+1 << ": " << r << endl;
    }
}
