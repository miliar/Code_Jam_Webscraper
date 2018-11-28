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

//BEGINTEMPLATE_BY_ALLAN7799
typedef long long int64;

typedef pair<int,int> ipair;
#define MP(X,Y) make_pair(X,Y)
#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))

#define REP(i,a) for(int i=0;i<int(a);++i)
#define REP2(i,n,m) for(int i=n;i<(int)(m);++i)
#define ALL(a) (a).begin(),(a).end()
//ENDEMPLATE_BY_ALLAN7799

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
        int n;
        vector<int>l;
        vector<int>r;
        cin>>n;
        int temp;
        while(n--)
        {
            cin>>temp;
            l.push_back(temp);
            cin>>temp;
            r.push_back(temp);
        }
        int res=0;
        REP(i,l.size()-1)
        {
            for(int j = i+1;j<l.size();j++)
            {
                if(((l[i]-l[j])*(r[i]-r[j]))<0)
                {
                    res++;
                }
            }
        }
        cout<<res;
        //////////////////////////////////////
        cout<<endl;
    }


    return 0;
}
