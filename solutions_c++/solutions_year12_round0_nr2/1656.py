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
    freopen("B-small-attempt2.in","r",stdin);freopen("B-small-attempt2.out","w",stdout);
#endif
#ifdef LARGE
    //ifstream fin("A-large-practice.in");ofstream fout("A-large-practice.out");
    //ifstream fin("A-large.in");ofstream fout("A-large.out");
    freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
#endif
    int N;
    int t, s, p;
    int ti[100];
    cin>>N;
    REP(z,N)
    {

        cout<<"Case #"<<z+1<<": ";
        //////////////////////////////////////
        cin>>t>>s>>p;
        REP(i, t)
        {
            cin>>ti[i];
        }
        int res = 0;
        REP(i , t)
        {
            int a;
            switch(ti[i]%3)
            {
                case 0:
                {
                    a = ti[i]/3;
                    if (a >= p)
                    {
                        res += 1;
                    }
                    else if (a + 1 >= p && a > 0 && s > 0)
                    {
                        res += 1;
                        s -= 1;
                    }
                    break;
                }
                case 1:
                {
                    a = ti[i]/3 + 1;
                    if (a >= p)
                    {
                        res ++;
                    }
                    break;
                }
                case 2:
                {
                    a = ti[i]/3 + 1;
                    if (a >= p)
                    {
                        res += 1;
                    }
                    else if (a + 1 == p && a - 1 >= 0 && s > 0)
                    {
                        res += 1;
                        s -= 1;
                    }
                    break;
                }
            }
        }
        //////////////////////////////////////
        cout<<res<<endl;
    }


    return 0;
}
