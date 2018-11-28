#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <ctime>

using namespace std;

//BEGINTEMPLATE_BY_SCORPIOLIU
const double PI  = acos(-1.0);
const double EPS = 1e-11;
const double INF  = 1E200;

typedef long long int64;
typedef unsigned long long uint64;

typedef pair<int,int> ipair;
#define MP(X,Y) make_pair(X,Y)
#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))

#define REP(i,a) for(int i=0;i<int(a);++i)
#define REP2(i,n,m) for(int i=n;i<(int)(m);++i)
#define FORE(it,a) for (typeof((a).begin()) it=(a).begin();it!=(a).end();++it)
#define ALL(a) (a).begin(),(a).end()
//ENDEMPLATE_BY_SCORPIOLIU

//#define SMALL
#define LARGE

int main()
{
#ifdef SMALL
    //ifstream fin("A-small-practice.in");ofstream fout("A-small-practice.out");
    //ifstream fin("A-small-attempt0.in");ofstream fout("A-small-attempt0.out");
    freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
#endif
#ifdef LARGE
    //ifstream fin("A-large-practice.in");ofstream fout("A-large-practice.out");
    //ifstream fin("A-large.in");ofstream fout("A-large.out");
    freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
#endif
    int Z;
    cin>>Z;
    REP(z,Z)
    {

        cout<<"Case #"<<z+1<<": "<<endl;
        //////////////////////////////////////
        int R,C;
        cin>>R>>C;
        vector<string>v;
        string str;
        REP(i, R)
        {
            cin>>str;
            v.push_back(str);
        }

        bool flag = false;
        REP(i, R)
        {
            REP(j, C)
            {
                if (v[i][j] == '#')
                {
                    if (i+1>=R || j+1>=C)
                    {
                        flag = true;
                        goto here;
                    }
                    else if (v[i+1][j] != '#' || v[i+1][j+1] != '#' || v[i][j+1] != '#')
                    {
                        flag = true;
                        goto here;
                    }
                    else
                    {
                        v[i][j] = '/';
                        v[i+1][j] = '\\';
                        v[i][j+1] = '\\';
                        v[i+1][j+1] = '/';
                    }
                }
            }
        }
        here: if (flag)
        {
            cout<<"Impossible"<<endl;
        }
        else
        {
            REP(i, R)
            {
                cout<<v[i]<<endl;
            }
        }
        //////////////////////////////////////
    }
    return 0;
    return 0;
}
