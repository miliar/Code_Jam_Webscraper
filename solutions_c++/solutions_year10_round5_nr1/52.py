#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <complex>

#define mp make_pair
#define pb push_back
#define sqr(x) ((x)*(x))
#define foreach(it,c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;
typedef long long LL;
typedef complex<double> Point;

template<typename T> inline int size(const T &a) { return a.size(); }
template<typename T> inline bool operator<(const int &a,const vector<T> &b) { return a<b.size(); }

int md;
vector<int> primes;
vector<int> arr;

void precalc(void)
{
    primes.pb(2);
    for(int i=3;i<1000000;i+=2)
    {
        bool check = false;
        for(int j=0;j<size(primes);j++)
        {
            if(primes[j]*primes[j] > i) break;
            if( (i % primes[j]) == 0) { check=true; break; }
        }
        if(!check)
        {
            primes.pb(i);
        }
    }
}

bool check(int a,int b,int pri)
{
    for(int i=1;i<size(arr);i++)
    {
        if((arr[i-1]*a+b)%pri != arr[i])
            return false;
    }
    return true;
}

void process(void)
{
    int d,k;
    scanf("%d %d",&d,&k);
    arr.resize(k);
    int maxx = 0;
    for(int i=0;i<k;i++)
    {
        scanf("%d",&arr[i]);
        maxx = max(maxx, arr[i]);
    }
    md=1;
    for(int i=0;i<d;i++) md *= 10;

    int cur = -1;

    if(size(arr) == 1)
    {
        printf("I don't know.\n");
        return;
    }

    for(int i=0;i<size(primes);i++)
    {
        if(primes[i] <= maxx) continue;
        if(primes[i] > md) break;

        for(int a=0;a<primes[i];a++)
        {
            int b = (((arr[1] - arr[0] * a) % primes[i]) + primes[i]) % primes[i];
            if(check(a,b,primes[i]))
            {
                int nex = (arr.back() * a + b) % primes[i];
                if(cur == -1) cur = nex;
                if(cur != nex)
                {
                    printf("I don't know.\n");
                    return;
                }
            }
        }
    }

    cout << cur << endl;
}

int main(void)
{
    precalc();
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        printf("Case #%d: ",i);
        process();
        cerr << i << endl;
    }
	return 0;
}

