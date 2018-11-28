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
#include <float.h>

using namespace std;

// prewritten code

#define sz(x) (int)(x).size()
#define all(c) (c).begin(),(c).end()
#define Fill(a,b) memset(&a,b,sizeof(a))
#define Min(a,b) ((a)<(b)?(a):(b))
#define Max(a,b) ((a)>(b)?(a):(b))
#define pb push_back

#define GDB 1
#define DBG(x) if(GDB){cerr << #x <<" = "<< x << endl;}
#define DBGA(x) if(GDB){cerr << #x <<": "; for (int i=0; i<(int)sizeof(x)/(int)sizeof(x[0]); ++i) cerr<<x[i]<<' '; cerr<<endl;}
#define DBGV(x) if(GDB){cerr << #x <<": "; for (int i=0; i<(int)Size(x); ++i) cerr<<x[i]<<' '; cerr<<endl;}

// real code
string problem_name="c";
void init(){
    freopen( (problem_name+".in").c_str(),"rt",stdin);
    freopen( (problem_name+".out").c_str(),"wt",stdout);
}
#define MAXN 601
#define MAXM 19
string p="welcome to code jam";
int dp[MAXN][MAXM];
int main(){
    init();
    int n;
    int tt;
    int ret;
    int i,j,ii,k;
    string s;
    for(i=0;i<MAXN;i++) for(j=0;j<MAXM;j++) dp[i][j]=0;
    scanf("%d\n",&n);
    for(tt=0;tt<n;tt++){
        for(i=0;i<MAXN;i++) for(j=0;j<MAXM;j++) dp[i][j]=0;
        getline(cin,s);
        for(j=0;j<sz(s);j++){
            if(s[j]==p[0]) dp[j][0]=1;
            for(k=1;k<MAXM;k++){
                if(s[j]==p[k]){
                    for(ii=0;ii<j;ii++) dp[j][k]=(dp[j][k]+dp[ii][k-1])%10000;
                }
            }
        }
        ret=0;
        for(j=0;j<sz(s);j++) ret=(ret+dp[j][MAXM-1])%10000;
        printf("Case #%d: %d%d%d%d\n",tt+1,ret/1000,(ret/100)%10,(ret/10)%10,ret%10);
    }
    return 0;
}
