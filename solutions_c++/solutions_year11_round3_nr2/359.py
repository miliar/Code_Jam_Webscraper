#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <climits>
using namespace std;

#define REP(i,n) for (int i=0; i<(int)(n); ++i)
#define REPS(p,s) for (char * p = s; *p ; p++)
#define FOR(var,start,end) for (int var=(start); var<=(int)(end); ++var)
#define FORD(var,start,end) for (int var=(start); var>=(int)(end); --var) 
#define PB push_back
#define PF push_front
#define BP pop_back
#define FP pop_front
#define BN begin()
#define RN rbegin()
#define RD rend()
#define ED end()
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define IT(X) __typeof((X).BN)
#define RIT(X) __typeof((X).RN) 
#define REF(X) __typeof(__typeof(X)::reference) 
#define FORIT(it, X) for(IT(X) it = (X).BN; it != (X).ED; ++it)
#define FORITR(it, X) for(RIT(X) it = (X).RN; it != (X).RD; ++it) 
#define VV(X) vector < vector< X > >
#define PIB(X)  pair<IT(X),bool >  

typedef long long LL;
typedef unsigned long long ULL;
typedef istringstream ISS;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector< PII > VPII;	

int main()
{
    int cases,count;
    cin >> cases;
    count=1;
    while (cases>0) {
        /* code */
        long long l,t,n,c,ip,sum,tot;
        multiset<long long> s;
        multiset<long long>::reverse_iterator si;
        VI kc,kk;
        cin>>l>>t>>n>>c;
        sum=0;
        REP(i,c)
        {
            cin >> ip;
            kc.PB(ip);
        }
        tot=0;
        for(long long i=0;i<n;i++)
        {
                kk.PB((kc[i%c]));
        }
        for(long long i=0;i<kk.size();i++)
        {
            if((sum+(kk[i]*2))<t)
            {
                sum+=kk[i]*2;
                kk[i]=0;
            }
            else
            {
                kk[i]=kk[i]-((t-sum + 1)/2);
                sum+=(t-sum);
                break;
            }
        }
        for(long long i=0;i<kk.size();i++)
        {
            if(kk[i]==0)
                continue;
            else
            {
                s.insert(kk[i]);
            }
        }
        for(si=s.rbegin();si!=s.rend();si++)
        {
            if(l>0)
            {
                sum+=*si;
                l--;
            }
            else
            {
                sum+=(*si)*2;
            }
        }
        printf("Case #%d: ",count);
        cout << sum << endl;
        cases--;
        count++;
    }
    return 0;
}
