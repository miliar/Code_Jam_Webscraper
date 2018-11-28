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
    ifstream fin("C-small-attempt0.in");ofstream fout("C-small-attempt0.out");
    //freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
#endif
#ifdef LARGE
    //ifstream fin("A-large-practice.in");ofstream fout("A-large-practice.out");
    ifstream fin("C-large.in");ofstream fout("C-large.out");
    //freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
#endif
    int N;
    fin>>N;
    REP(z,N)
    {

        fout<<"Case #"<<z+1<<": ";
        //////////////////////////////////////
        int A, B;
        fin>>A>>B;
        cout<<z<<" "<<A<<" "<<B<<endl;
        stringstream ss;
        string s;
        ss<<A;
        ss>>s;
        int len = s.length();
        int begin = A;
        set<int>tree;
        set<pair<int, int> >res;
        while(begin <= B)
        {
            if (len < 2)
            {
                break;
            }
            if (tree.find(begin) != tree.end())
            {
                begin++;
                continue;
            }

            vector<int>vec;
            int t = begin;
            vec.push_back(t);
            REP(i, len - 1)
            {
                int e = t / 10;
                int h = t % 10;
                REP(j, len - 1)
                {
                    h *= 10;
                }
                t = e + h;
                tree.insert(t);
                if (h != 0)
                    vec.push_back(t);
            }
            sort(vec.begin(), vec.end());
            for (int k = 0; k != vec.size() - 1; k ++)
            {
                for (int i = k + 1; i != vec.size(); i++)
                {
                    //cout<<vec[k]<<" "<<vec[i]<<endl;
                    if (vec[i] > vec[k] && vec[i] <= B && vec[k] >= A)
                    {
                        if (res.find(make_pair(vec[k], vec[i])) == res.end())
                        {
                            res.insert(make_pair(vec[k], vec[i]));
                            //cout<<vec[k]<<" "<<vec[i]<<endl;
                        }
                    }
                }
            }
            begin++;
        }
        //////////////////////////////////////
        fout<<res.size()<<endl;
    }


    return 0;
}
