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

int t, h, w, ind, mini, res;
vector< vector<int> > m(110, vector<int> (100)), r(110, vector<int> (100,-1)), sink(110, vector<int> (100,0));
vector< vector< vector<int> > > p(110, vector< vector<int> >(110, vector<int> (4,0)) );

void marca(int i, int j)
{
    if(p[i][j][0]==1 && r[i+1][j]<0) r[i+1][j] = r[i][j];
    if(p[i][j][1]==1 && r[i][j+1]<0) r[i][j+1] = r[i][j];
    if(p[i][j][2]==1 && r[i][j-1]<0) r[i][j-1] = r[i][j];
    if(p[i][j][3]==1 && r[i-1][j]<0) r[i-1][j] = r[i][j];

    if(p[i][j][0]==1) marca(i+1,j);
    if(p[i][j][1]==1) marca(i,j+1);
    if(p[i][j][2]==1) marca(i,j-1);
    if(p[i][j][3]==1) marca(i-1,j);

    return;
}

int main()
{
    cin >> t;
    for(int I=1; I<=t; I++)
    {
        vector< vector< vector<int> > > p0(110, vector< vector<int> >(110, vector<int> (4,0)) );
        vector< vector<int> > r0(110, vector<int> (100,-1)), sink0(110, vector<int> (100,0));
        p = p0;
        r = r0;
        sink = sink0;

        cout << "Case #" << I << ":" << endl;

        cin >> h >> w;
        for(int i=0; i<h; i++)
        {
            for(int j=0; j<w; j++)
            {
                cin >> m[i][j];
            }
        }

        res = 0;
        for(int i=0; i<h; i++)
        {
            for(int j=0; j<w; j++)
            {
                if( (i-1>=0 && m[i-1][j]<m[i][j])  ||
                    (j-1>=0 && m[i][j-1]<m[i][j])  ||
                    ((j+1)<w && m[i][j+1]<m[i][j]) ||
                    ((i+1)<h && m[i+1][j]<m[i][j]) )
                {
                    mini = 10010;
                    ind = 0;
                    if(i-1>=0 && m[i-1][j]<mini)
                    {
                        ind = 1;
                        mini = m[i-1][j];
                    }
                    if(j-1>=0 && m[i][j-1]<mini)
                    {
                        ind = 2;
                        mini = m[i][j-1];
                    }
                    if(j+1<w && m[i][j+1]<mini)
                    {
                        ind = 3;
                        mini = m[i][j+1];
                    }
                    if(i+1<h && m[i+1][j]<mini)
                    {
                        ind = 4;
                        mini = m[i+1][j];
                    }

                    if(ind==1) p[i-1][j][0]=1;
                    else if(ind==2) p[i][j-1][1]=1;
                    else if(ind==3) p[i][j+1][2]=1;
                    else if(ind==4) p[i+1][j][3]=1;
                }
                else
                {
                    r[i][j] = res;
                    sink[i][j] = 1;
                    res++;
                }
            }
        }

        for(int i=0; i<h; i++)
        {
            for(int j=0; j<w; j++)
            {
                if(sink[i][j]>0) marca(i,j);
            }
        }

        vector<int> leters(26,-1);
        int current_leter = 0;
        for(int i=0; i<h; i++)
        {
            for(int j=0; j<w; j++)
            {
                if(leters[r[i][j]]<0)
                {
                    leters[r[i][j]] = current_leter;
                    current_leter++;
                }
                if(j==0) printf("%c",leters[r[i][j]]+'a');
                else printf(" %c",leters[r[i][j]]+'a');

            }
            cout << endl;
        }
    }
}
