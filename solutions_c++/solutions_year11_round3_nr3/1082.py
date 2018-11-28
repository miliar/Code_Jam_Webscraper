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

#define SMALL
//#define LARGE

int main()
{
#ifdef SMALL
    //ifstream fin("C-small-practice.in");ofstream fout("C-small-practice.out");
    //ifstream fin("C-small-attempt0.in");ofstream fout("C-small-attempt0.out");
    freopen("C-small-attempt1.in","r",stdin);freopen("C-small-attempt1.out","w",stdout);
#endif
#ifdef LARGE
    //ifstream fin("C-large-practice.in");ofstream fout("C-large-practice.out");
    //ifstream fin("C-large.in");ofstream fout("C-large.out");
    freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
#endif
    int Z;
    cin>>Z;
    REP(z,Z)
    {

        cout<<"Case #"<<z+1<<": ";
        //////////////////////////////////////
        int N,L,H;
        cin>>N>>L>>H;
        int n;
        vector<int>v;
        REP(i, N)
        {
            cin>>n;

            v.push_back(n);
        }
        int res = -1;
        bool flag  = false;
        for (int i = L; i<=H; i++)
        {
            flag = false;
            REP(j, N)
            {
                int temp1 = max(v[j], i);
                int temp2 = min(v[j], i);
                if (temp1%temp2 == 0)
                {
                    continue;
                }
                else
                {
                    flag = true;
                }
            }

            if (!flag)
            {
                res = i;
                break;
            }
        }
        here: if (res == -1)
        {
            cout<<"NO";
        }
        else
        {
            cout<<res;
        }


        //////////////////////////////////////
        cout<<endl;
    }
    return 0;
}
