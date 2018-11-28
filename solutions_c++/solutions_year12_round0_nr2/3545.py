#include <iostream>
#include <cstring>
#include <cstdio>
#include <sstream>
#include <numeric>
#include <iterator>
#include <queue>
#include <set>
#include <map>
#include <vector>

#define mp make_pair
#define pb push_back
#define sqr(x) ((x)*(x))
#define foreach(it,c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;

template<typename T> int size(const T &a) { return a.size(); } 

    /* process input */
    /*
    int n,a,b;
    vector<int> vec;

    scanf("%d %d",&n, &a);
    vec.reserve(a);

    for(int i=0; i < n ; ++i)
    {
        scanf("%d", &vec[i]);
    }
    */

int getMinTotal(int p)
{
    if(p == 0) return 0;
    else if (p == 1)    return 1;
    else
    {
        return (p - 2) * 3 + 2;
    }
}

void process(void)
{
    /* process input */
    int nGoo = 0;
    int nSup = 0;
    int p = 0;
    VI totals; 
    
    scanf("%d %d %d", &nGoo, &nSup, &p);
    totals.resize(nGoo);

    for(int i = 0; i < nGoo; ++i)
    {
        scanf("%d", &totals[i]);
    }

    /* main logic */
    int64_t sol =0 ;    
    int surprise = 0;

    int minTotal = getMinTotal(p);

    if(p == 0)
    {
        cout << nGoo << endl;
        return;
    }

    if(p == 1)
    {
        for(int i = 0; i < nGoo; ++i)
        {
            if(totals[i] != 0) ++sol;
        }
        cout << sol << endl;
        return;
    }

    for(int i = 0; i < nGoo; ++i)
    {
        //cout << "MinTotal: " << minTotal << ", comparing: " << totals[i] << endl;
        if(totals[i] >= minTotal)
        {
            ++sol;
            if(totals[i] - minTotal < 2)
            {
                ++surprise;
            }
        }
    }
    
    if (surprise > nSup)
    {
        sol = sol - (surprise - nSup);    
    }

    /* print solution */
    cout << sol << endl;
}


int main(void)
{
    int testcase = 0;
    scanf("%d", &testcase);
    for(int i = 1; i <= testcase ; ++i)
    {
        printf("Case #%d: ",i);
        process();
        //cerr << i << endl;
    }
}
