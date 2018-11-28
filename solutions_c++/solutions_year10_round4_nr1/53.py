
//Tomasz Kulczyński
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
using namespace std;

#define X first
#define Y second
#define MP make_pair
#define PB push_back
typedef long long ll;
typedef double D;
typedef long double ld;
typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))
int cond = 1;
#define db(x) {if(cond){cerr << __LINE__ << " " << #x << " " << x << endl; } }
#define dbv(x) {if(cond){cerr << __LINE__ << " " << #x << ": "; FORE(__i,x) cerr << *__i << " "; cerr << endl;} }

char s[173][177];

inline bool dig(char x) { return x>='0' && x<='9'; }

void test()
{
    int k;
    fgets(s[0],177,stdin);
    sscanf(s[0],"%d",&k);
    int n = k+k-1;
    int ret = 1<<30;
    REP(i,n) REP(j,n) s[i][j] = 0;
    REP(i,n) fgets(s[i],177,stdin);
    REP(i,n) REP(j,n) 
    {
        int ok = 1;
        int odl = 0;
        REP(a,n) REP(b,n)
            if(dig(s[a][b]))
            {

                if(i+i-a>=0 && i+i-a < n && s[a][b] != s[i+i-a][b] && dig(s[i+i-a][b]))
                {
                    ok = 0;
                 //   if(i==2 && j==3) printf("tutaj %d %d\n",a,b);
                }
                if(j+j-b>=0 && j+j-b < n && s[a][b] != s[a][j+j-b] && dig(s[a][j+j-b]))
                {
                    ok = 0;
                  //  if(i==2 && j==3) printf("tutaj* %d %d\n",a,b);
                }
                int x = abs(i-a) + abs(j-b);
            //    printf("     %d %d :: %d %d\n ",a,b,ok,x);
                if(x > odl) odl = x;
            }
       // printf("%d %d :: %d %d\n",i,j,ok,odl);
        odl++;
        if(ok) ret = min(ret, odl);
    }
    printf("%d\n",ret*ret - k*k);
}

int main()
{
    int dd,cas;
    scanf("%d",&dd);
    fgets(s[0],177,stdin);
    FOR(cas,1,dd)
    {
        printf("Case #%d: ",cas);
        test();
    }
    return 0;
}
