#include <vector>
#include <cstring>
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
#include <fstream>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


#define SZ size()
#define PB push_back
#define ALL(v) v.begin(),v.end()
#define MP make_pair
#define x first
#define y second

#define LL long long
#define UI unsigned int
#define ULL unsigned long long
#define PI pair<int,int>
#define PD pair<double,double>
#define PLL pair<LL,LL>
#define PULL pair<ULL,ULL>
#define VI vector<int>
#define VD vector<double>
#define VS vector<string>
#define SI set<int>
#define PQ priority_queue
#define VVI vector<vector<int> >
#define IT iterator

#define ABS(x) (((x)>0)?(x):(-(x)))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define sign(a) ((a)>0)-((a)<0)
#define sqr(a) ((a)*(a))
#define Repi(n) for (int i=0; i<(n); i++)
#define Repj(n) for (int j=0; j<(n); j++)
#define Repk(n) for (int k=0; k<(n); k++)
#define F(i,n) for (int i=0;i<(n);i++)

#define INF 2000000000
#define EPS 1e-6

#define Time ((double)clock()/CLOCKS_PER_SEC)
#define pause system("pause")

using namespace std;

int T;
const int MAXN = 1000100;
VI primes;
bool notpr[MAXN];
int D, K;
int s[50];
long long ns[50];
int ten[10];

int prs[MAXN], pc;

void getprs(int dif)
{
    pc = 0;
    for (int i = 0; primes[i] * primes[i] <= dif && dif > 1; i++)
    {
        if (dif % primes[i] == 0)
        {
            prs[pc++] = primes[i];
            while (dif % primes[i] == 0)
            {
                dif /= primes[i];
            }
        }
    }
    if (dif > 1)
        prs[pc++] = dif;
}

const bool dbg = 0;
int minp;

bool works(long long A, long long B, long long P)
{
    for (int i = 1; i < K; i++)
    {
        long long exp = A * (LL)s[i - 1] + B;
        exp %= P;
        if (exp != s[i])
            return 0;
    }
    return 1;
}

void gen(long long S, LL A, LL B, LL P, int K)
{
    for (int i = 0; i < K; i++)
    {
        cout<<S<<" ";
        S = S * A + B;
        S %= P;
    }
}

int bf()
{
    if (K == 1)
        return -1;
    LL ans = -1;
    for (int k = 0; primes[k] <= ten[D]; k++)
    {
        LL P = primes[k];
        if (P < minp) continue;
     //   cout<<P<<"\n";
        for (LL A = 0; A < P; A++)
        {
            LL B = s[1] - s[0] * A;
            B = (B % P + P) % P;
            //if (A == 1 && B == 0)
            //cout<<A<<" "<<B<<" "<<P<<" ("<<ans<<") : \n";
            LL S = s[0];
            bool ok = 1;
            for (int i = 1; i < K; i++)
            {
                S = S * A + B; S %= P;
              //  if (A == 1 && B == 0)
              //  cout<<"     "<<s[i]<<" "<<S<<"\n";
                if (S != s[i])
                {
                    ok = 0;
                    break;
                }
            }
            if (ok)
            {
                LL exp = (s[K - 1] * A + B) % P;
           //    cout<<"     EXP "<<exp<<" at "<<A<<" "<<B<<" "<<P<<"\n";
                if (ans == -1)
                    ans = exp;
                else
                    if (ans != exp)
                    {
                        return -1;
                    }
            }
        }
    }
    return ans;
}

int main()
{
  // gen(1, 0, 4, 13, 5);

    for (int i = 2; i < MAXN; i++)
    {
        if ( i <= MAXN / i )
        {
            for (int j = i * i; j < MAXN; j += i)
            {
                notpr[j] = 1;
            }
        }
        if (!notpr[i])
        {
            primes.PB(i);
        }
    }
    ten[0] = 1;
    for (int i = 1; i <= 6; i++)
        ten[i] = ten[i-1] * 10;

/*
    getprs(1);
    Repi(pc)
        cout<<prs[i]<<" "; cout<<"\n";
        */

    scanf("%d",&T);
    for (int xx = 1; xx <= T; xx++)
     {
        minp = 0;
        long long ans = -1;
        scanf("%d%d", &D, &K);
        Repi(K)
        {
            scanf("%d", &s[i]);
            minp = max(minp, s[i]);
        }
        minp++;
        ns[0] = s[0];
        
        bool allsame = 1;
        Repi(K - 1)
            if (s[i] != s[i + 1])
            {
                allsame = 0;
                break;
            }
        if (allsame && K > 1)
        {
                ans = s[0];
                goto end;
        }
        if (K == 1)
            goto end;
        
        for (long long A = 0; A <= ten[D]; A++)
        {
            long long B = (long long)s[1] - (long long)s[0] * A;
if (dbg)            cout<<"A = "<<A<<" B = "<<B<<": ";
            bool alleq = 1;
            for (int i = 1; i < K; i++)
            {
                ns[i] = ns[i - 1] * A + B;
      if (dbg)          cout<<ns[i]<<" ";
                if (ns[i] != s[i])
                {
                    alleq = 0;
                    if (abs(ns[i] - s[i]) == 1)
                    {
                        break;
                    }
                    getprs(abs(ns[i] - s[i]));
       if (dbg)             cout<<" ->> ";
                    Repj(pc)
                    {
                        if (prs[j] >= minp && prs[j] <= ten[D])
                        {
                            LL nB = (B % prs[j] + prs[j]) % prs[j];
       if (dbg)                     cout<<" try "<<prs[j]<<"  (B = "<<nB<<") ";
                            if (works(A, nB, prs[j]))
                            {
                                LL exp = (LL)s[K - 1] * A + nB;
                                exp %= (LL)prs[j];
         if (dbg)                       cout<<"    works: "<<exp;
                                if (ans == -1)
                                    ans = exp;
                                else
                                 {
                                        if (ans != exp)
                                        {
                                            ans = -1;
                                            goto end;
                                        }
                                    }
                            }
          if (dbg)                  cout<<"\n";
                        }
                    }
      if (dbg)              cout<<"\n";
                    break;
                }
            }
            if (alleq)
            {
                for (int i = 0; primes[i] <= ten[D]; i++)
                if (primes[i] >= minp)
                {
                    LL P = primes[i];
                    LL exp = ((LL)s[K - 1] * A + B) % P;
                    exp += P; exp %= P;
                    if (ans == -1)
                    {
                        ans = exp;
                    }
                    else
                        if (ans != exp)
                            { ans = -1; goto end; }
                }
            }
   if (dbg)         cout<<"\n";
        }
        end:;
        
    /*    cout<<bf()<<" "<<ans<<"\n";
        cout<<"    "<<D<<" "<<K<<"\n";
        assert(bf() == ans); */
        if (ans == -1)
            cout<<"Case #"<<xx<<": I don't know.\n";
        else
            cout<<"Case #"<<xx<<": "<<ans<<"\n";
     }
    return 0;
}
