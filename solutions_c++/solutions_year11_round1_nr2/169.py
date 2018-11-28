#include<algorithm>
#include<cmath>
#include<fstream>
#include<iomanip>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<vector>

using namespace std;

#define forn(i,n) for(int i = 0; i < (n); i++)
#define dforn(i,n) for(int i = (int)(n-1); i >= 0; i--)
#define all(v) v.begin(), v.end()
#define pb push_back

bool coincide(string a, string b, int pos, string orden)
{
    if(a.size()!=b.size())
        return false;
    forn(i,a.size())
    {
        if(a[i]!=b[i])
        {
            forn(j,pos+1)
            if(a[i]==orden[j]||b[i]==orden[j])
                return false;
        }
    }
    return true;
}

bool funca(string a, int pos, string orden, string b)
{
    if(a.size()!=b.size())
        return false;
    forn(i,a.size())
    {
        if(a[i]!=b[i])
        {
            forn(j,pos)
            if(a[i]==orden[j]||b[i]==orden[j])
                return false;
        }
    }
    if(count(all(b),orden[pos])!=0)
        return true;
    return false;
}

string calc(vector<string> vec, string orden)
{
    int res = 0,ganador = 0;
    forn(i,vec.size())
    {
        int t = 0;
        forn(j,orden.size())
        {
            int k = count(all(vec[i]),orden[j]);
            if(k==0)
            {
                bool b = false;
                forn(x,vec.size())
                {
                    if(funca(vec[i],j,orden,vec[x]))
                        b = true;
                }
                if(b==true)
                    t++;
            }
            int cuenta = 0;
            forn(x,vec.size())
            {
                if(coincide(vec[x],vec[i],j,orden))
                    cuenta++;
            }
            if(cuenta==1&&res<t)
            {
                res = t;
                ganador = i;
                break;
            }
        }
    }
    return vec[ganador];
}

int main()
{
    freopen("B-small.in","r",stdin);
    freopen("B-small.out","w",stdout);
    int casos;
    cin >> casos;
    forn(casito,casos)
    {
        int n, m;
        cin >> n >> m;
        vector<string> vec(n);
        forn(i,n)
            cin >> vec[i];
        vector<string> orden(m);
        forn(i,m)
            cin >> orden[i];
        cout << "Case #" << casito+1 << ":";
        forn(x,m)
            cout << " " << calc(vec,orden[x]);
        cout << endl;
    }
}
