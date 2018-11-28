#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>

using namespace std;

ifstream fi("a.in");
ofstream fo("a.out");
#define cin fi
#define cout fo

#define FOREACH(it,c) for( __typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define FOR(i,a,b) for( long i=(a),_b=(b);i<=_b;i++) 
#define DOW(i,b,a) for( long i=(b),_a=(a);i>=_a;i--)
#define REP(i,n) FOR(i,0,(n)-1)
#define DEP(i,n) DOW(i,(n)-1,0)
#define all(a) (a).begin() , (a).end()

typedef vector<int> VI ;
typedef vector<string> VS ;
template<class T> inline int size(const T&c) { return c.size(); }  

long stest;
long n, result;
long tatca;
long s[100];

main()
{
    REP(i, (1<<15)-1);
    cin>>stest;
    REP(kk, stest)
    {
        result=-1;
        tatca=0;
        cin>>n;
        REP(i, n) cin>>s[i];
        REP(i, n) tatca+=s[i];
        REP(i, (1<<n)-1)
        {
            long sum1=0, sum2=0, suma=0, sumb=0;
            REP(j, n)
                if ((i>>j)^1) {sum1+=s[j]; suma^=s[j];} else
                {sum2+=s[j]; sumb^=s[j];}
           if (suma==sumb && sum2!=0 && sum1!=0)
               if (result<sum1) result=sum1;
        }
        if (result==-1) cout<<"Case #"<<kk+1<<": NO"<<endl; else
            cout<<"Case #"<<kk+1<<": "<<result<<endl;
    }    
    return 0;
}