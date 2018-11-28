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


//how to get digit number?
int getNumDigit(int n)
{
    int nDigit = 0;
    while(n > 0)
    {
        ++nDigit;        
        n = n / 10;
    }
    return nDigit;
}

// power of 10
int pow10(int n)
{
    return (int)pow(10.0,n);
}

void process(void)
{
    /* process input */
    int min = 0;
    int max = 0;

    scanf("%d %d",&min, &max);

    /* main logic */
    int64_t sol = 0;    

    int nDigit = 0;
    nDigit = getNumDigit(min);
    for(int n = min; n < max; ++n)
    {
        if (nDigit < 2)
            continue;
        
        vector<int> preM;
        for(int i = nDigit - 1; i > 0 ; --i)
        {
            if((n % pow10(i)) / pow10(i-1) == 0)
                continue;

            int m = (n % pow10(i)) * pow10(nDigit - i) + n / pow10(i);

            vector<int>::const_iterator location = find(preM.begin(), preM.end(), m);

       
            if (location == preM.end())
            {
                preM.push_back(m);
         
                if (m <= max && n < m)
                {
                    ++sol;
                }
            }
        }       
    }

    /* print solution */
    cout << sol << endl;
}

int main(void)
{
    int testcase;
    scanf("%d", &testcase);
    for(int i = 1; i <= testcase ; ++i)
    {
        printf("Case #%d: ",i);
        process();
        //cerr << i << endl;
    }
}
