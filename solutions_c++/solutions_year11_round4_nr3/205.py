#include<algorithm>
#include<cmath>
#include<fstream>
#include<iomanip>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<vector>

using namespace std;

#define forn(i,n) for(int i = 0; i < (n); i++)
#define dforn(i,n) for(int i = (int)(n-1); i >= 0; i--)
#define all(v) v.begin(), v.end()
#define pb push_back
#define MAX 2000000
vector<long long> sonPot;
vector<long long> primes;
bool primos[MAX];

void criba()
{
    forn(i,MAX)
        primos[i] = (i>1);
    forn(i,MAX)
    if(primos[i]==true)
    {
        primes.push_back((long long)i);
        for(int k=i*2;k<MAX;k+=i)
            primos[k] = false;
    }
    return;
}

void calcPot()
{
    sonPot.push_back(1);
    forn(i,primes.size())
    {
        long long k = primes[i]*primes[i];
        while(k<1000000000010LL)
        {
            sonPot.push_back(k);
            k*=primes[i];
        }
    }
    sort(all(sonPot));
}
int main()
{
	freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int casos;
    cin >> casos;
    criba();
    calcPot();
    forn(casito,casos)
    {
        long long n;
        cin >> n;
        long long res = 0;
        while(res<sonPot.size()&&sonPot[res]<=n)
            res++;
        if(n==1)
            res = 0;
        cout << "Case #" << casito+1 << ": " << res << endl;
    }
}
