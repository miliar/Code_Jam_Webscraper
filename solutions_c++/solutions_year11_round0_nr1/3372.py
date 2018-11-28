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
    freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
#endif
#ifdef LARGE
    //ifstream fin("A-large-practice.in");ofstream fout("A-large-practice.out");
    //ifstream fin("A-large.in");ofstream fout("A-large.out");
    freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
#endif
    int N;
    cin>>N;
    REP(z,N)
    {

        cout<<"Case #"<<z+1<<": ";
        //////////////////////////////////////
        int N;
        int opos = 1;
        int bpos = 1;
        int os = 0;
        int bs = 0;
        string robot;
        int pos;
        int res = 0;
        cin>>N;
        while(N--)
        {
            cin>>robot>>pos;
            if (robot=="O")
            {
                if ((int)abs(pos-opos) > (res - os))
                {
                    res += ((int)abs(pos-opos) - (res - os));


                }
                res++;
                os = res;
                opos = pos;
            }
            else
            {
                if ((int)abs(pos-bpos) > (res - bs))
                {
                    res += ((int)abs(pos-bpos) - (res - bs));
                }
                res++;
                bs = res;
                bpos = pos;
            }
        }
        //////////////////////////////////////
        cout<<res<<endl;
    }


    return 0;
}
