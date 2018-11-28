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

int checkequal(vector<int>c, int k)
{
    int res = -1;
    int n1, n2;
    int res1,res2;
    int temp;
    /*for (int i = 1; i < c.size()-1; i++)
    {

        res1 = n1 = c[0]; n2 = res2 = c[i];
        for(int j = 0; j < c.size() - 1; j++)
        {
            if (i<j)
            {
                res1 += c[j];
                n1 ^= c[j];
            }
            else
            {
                res2 += c[j+1];
                n2 ^= c[j+1];
            }
        }
        if (n1 != n2)
            return -1;
        cout<<res<<" "<<res1<<" "<<res2<<endl;
        temp = max(res1, res2);
        res = max(temp,res);
    }*/

    for (int i = 0; i < c.size(); i++)
    {
        res1 = n1 = c[i]; n2 = -1;res2 = 0;
        for (int j = 0; j < c.size(); j++)
        {
            if (i == j)
            {
                continue;
            }
            else
            {
                res2 += c[j];
                if (n2 == -1)
                    n2 = c[j];
                else
                    n2 ^= c[j];
            }
        }
        if (n1 != n2)
        return -1;
        temp = max(res1, res2);
        res = max(temp,res);
    }

    return res;
}

int main()
{
#ifdef SMALL
    //ifstream fin("C-small-practice.in");ofstream fout("C-small-practice.out");
    //ifstream fin("C-small-attempt0.in");ofstream fout("C-small-attempt0.out");
    freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
#endif
#ifdef LARGE
    //ifstream fin("C-large-practice.in");ofstream fout("C-large-practice.out");
    //ifstream fin("C-large.in");ofstream fout("C-large.out");
    freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
#endif
    int N;
    cin>>N;
    REP(z,N)
    {

        cout<<"Case #"<<z+1<<": ";
        //////////////////////////////////////
        int n;
        int sum = 0;
        int p;
        int res = -1;
        int temp;
        vector<int>c;
        cin>>n;
        c.reserve(n);
        REP(i, n)
        {
            cin>>p;
            c.push_back(p);
        }
        //for (int k = 1; k < n/2+1; k++)
        {
            temp = checkequal(c, 1);
            res = max(res, temp);
        }


        //////////////////////////////////////
        if (-1 == res)
            cout<<"NO"<<endl;
        else
            cout<<res<<endl;
    }


    return 0;
}
