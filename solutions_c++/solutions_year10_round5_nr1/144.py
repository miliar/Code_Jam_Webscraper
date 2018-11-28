#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;

#define sz(a) (LL)a.size()
#define all(a) a.begin(), a.end()
#define pb push_back
#define LL long long
#define INF 1000000
typedef vector <int> vi;
typedef vector <string> vs;
typedef pair<LL, LL> pii;

const int MAX = 1000100;
vi prime;
int d, k, maxd, mind;
int ans;
int num[22];

pii extended_gcd(LL A, LL B)
{
    if (A % B == 0)
    {
        return pii(0, 1);
    }
    else
    {
        pii w = extended_gcd(B, A % B);
        return pii(w.second, w.first - w.second * (A / B));
    }
}

void init()
{
    bool b[1000100];
    memset(b, true, sizeof(b));
    b[0]=b[1]=false;
    int i, j;
    for (i=2; i<MAX; i++) if (b[i])
    {
        for (j=i+i; j<MAX; j+=i) b[j]=false;
        prime.pb(i);
    }
}

void go(LL A, LL B, int P)
{
    int i;
    for (i=0; i<k-1; i++)
        if ((A*num[i]+B)%P!=num[i+1])
            return;
    int nextD = (A*num[k-1]+B)%P;
    if (ans!=-2)
    {
        if (ans!=nextD) ans=-1;
        return;
    }
    ans=nextD;
}


LL findX(LL a, LL b, LL n)
{
    //If the greatest common divisor d = gcd(a, n) divides b, then we can find a solution x to the congruence as follows:
    //the extended Euclidean algorithm yields integers r and s such ra + sn = d.
    //Then x = rb/d is a solution. The other solutions are the numbers congruent to x modulo n/d.
    while (a<0) a+=n;
    while (b<0) b+=n;
    pii w = extended_gcd(a, n);
    LL r = w.first;
    LL s = w.second;
    while (r<0) r+=n;
    while (s<0) s+=n;
    return (r*b) % n;
}

void compute(int P)
{
    LL A, B;
    if (k==2)
    {
        for (A=0; A<P; A++)
        {
    //        if (k==2 || (A*(num[1]-num[0])+P-(num[2]-num[1]))%P==0)
            B = P - ((A*num[0]+P-num[1])%P);
            go(A, B, P);
        }
    }
    else
    {
        A = findX((num[1]-num[0]), (num[2]-num[1]), P);
        B = P - ((A*num[0]+P-num[1])%P);
        go(A, B, P);
    }
}


void process()
{
    if (k==1) return;
    //if (k==2)
    //{
    //   if (num[0]==0 && num[1]==0) ans=0;
    //    return;
    //}
    maxd = 1;
    int i;
    for (i=0; i<d; i++) maxd *= 10;
    for (i=0; i<sz(prime); i++)
    {
        int p = prime[i];
        if (p>maxd) break;
        if (p<mind) continue;
        compute(p);
        if (ans==-1) break;
    }
}

int main()
{
    //freopen("inp.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
	
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small-attempt0c.out", "w", stdout);

    //freopen("A-small-attempt1.in", "r", stdin);
    //freopen("A-small-attempt1a.out", "w", stdout);

    //freopen("A-small-attempt2.in", "r", stdin);
    //freopen("A-small-attempt2b.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

    init();

	int numtest, test, i;
	cin >> numtest;

	for (test=1; test<=numtest; test++)
	{
        ans = -2;
        mind = 0;
        cin >> d >> k;
        for (i=0; i<k; i++)
        {
            cin >> num[i];
            mind = max(mind, num[i]+1);
        }

        process();
        if (ans<0)
		    cout << "Case #" << (test) << ": " << "I don't know." << endl;
        else
            cout << "Case #" << (test) << ": " << (ans) << endl;
	}
	return 0;
}
