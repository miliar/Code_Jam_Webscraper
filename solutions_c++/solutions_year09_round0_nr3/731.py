#include <queue>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <cstdio>
#include <complex>
#include <stack>
#include <cctype>
#include <cstdlib>
#include <iostream>

#define X real()
#define Y imag()
#define FR(i,n) for( long long i = 0; i < n; i ++ )
#define FOR(i,a,n) for(long long i = a; i < n; i ++)
#define FREACH(it,v) for( typeof(v.end()) it = v.begin(); it != v.end(); it ++ )
#define EPS 1e-12
#define EPS2 1e-3

using namespace std;

typedef long long ll;
typedef long double ld;
char s[600];
int dp[600][19];
char wel[20]="welcome to code jam";
int main()
{
   // cout << wel << endl;
    int n;

    scanf("%d\n",&n);
    FR(i,n)
    {
        gets(s);
     //   cout << s << endl;
        int len=strlen(s);
        memset(dp,0,sizeof(dp));
        FR(i,len)
            FR(j,19)
            {
                if(s[i]==wel[j])
                {
                //    if(j==0) cout << "i: " << i << endl;
                    if(j!=0)
                        FOR(k,0,i) 
                        {
                        //    cout << i << " " << j << " " << k << endl;
                            dp[i][j]+=dp[k][j-1];
                         //   if(j-1==0) cout << k << " " << j-1 << " "  << dp[k][j-1] << endl;
                            while(dp[i][j]>=10000) dp[i][j]-=10000;
                        }
                    else
                        dp[i][0]=1;
                }
            }
        
        int res=0;
        FR(i,len)
        {
          //  FR(j,19) cout << dp[i][j] << " ";
          //  cout << endl;
            res+=dp[i][18];
            while(res>=10000) res-=10000;
        }
        
       // cout << "res: " << res << endl;
        printf("Case #%d: ",i+1);
        cout.fill('0');
        cout.width(4);
        cout << res << endl;
    }
}