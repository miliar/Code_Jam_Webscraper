// Problem B
// Problem's source: Google Code Jam - Round 1C
// Program by Plamen Petrov (C) 2008
// http://digitalphysics.org/~ppetrov

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
#include <cstring>
#include <vector>
#include <sstream>
#include <iterator>
#include <cmath>
#include <cstdlib>
#include <cassert>
using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<n; ++i)
#define FOR(var,pocz,koniec) for (int var=pocz; var<=koniec; ++var)
#define FORD(var,pocz,koniec) for (int var=pocz; var>=koniec; --var)
#define FOREACH(it, X) for(__typeof(X.begin()) it = X.begin(); it != X.end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()

char g[64];

inline bool ugly(LL x){ return (x%2==0) || (x%3==0) || (x%5==0) || (x%7==0);}

LL atoll(char s[64], int first, int last)
{
    LL l=0, j=1;
    int i;
    
    for(i=last; i>=first; i--)
    {
        l+= (LL(s[i]-'0'))*j;
        j*=10;
    }
    
    return l;
}

bool incg(int places)
{
    int i;
    for(i=places; i>0; i--)
    {
        g[i]++;
        if(g[i]>2) g[i]=0;
        else break;
    }
    return i>0;
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);

    int test, tests, i, j, lens;
    char s[64];
    LL res, d[64], n, m;
    

    cin >> tests;
    for(test=1; test<=tests; test++)
    {
        res=0;
        
        cin >> s;
        lens=strlen(s);
        for(i=0; i<lens; i++) { d[i]=LL(s[i]-'0'); }
        
        for(i=0; i<lens-1; i++) g[i]=0;
        
        if(ugly(atoll(s, 0, lens-1))) res=1;
        
        while(incg(lens-1)) 
        {
            n=0; m=0;
            i=0; j=1;
            do
            {
                while(j<lens && g[j]==0) j++; //find spaces
                              
                m=atoll(s, i, j-1);
                
                //cout << n << " " <<  (int) g[i] << " " << m << endl;
                
                if(g[i]==1) n-=m;
                if(g[i]==2) n+=m;     
                if(g[i]==0) n=m;

                i=j;
                j++;
            }while(j<=lens);
            
            //cout << "n=" << n << endl;
            if(ugly(n)) res++;
        }
        
        
        
        cout << "Case #" << test << ": " << res << endl;
    }

    return 0;
}
