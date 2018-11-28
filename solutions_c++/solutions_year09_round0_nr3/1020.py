#include <iostream>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <complex>
#include <cmath>
#include <deque>
#include <stack>
#include <queue>
#include <ctime>
#include <list>
#include <map>
#include <set>
using namespace std;

typedef long long ll;

const int INF=0x3C3C3C3C;
#define mset(a,x) memset(a,x,sizeof(a))
#define Abs(a) ((a) >= 0 ? (a) : -(a))
#define dbg(x) cerr<<#x<<" : "<<x<<endl
#define For(I,N) for(int I=0;I<(N);I++)
#define For2(I,A,B) for(int I=(A); (A)<=(B)?(I<=(B)):(I>=(B)); (A)<=(B)?(I++):(I--))
#define ArrSize(x) (sizeof(x)/sizeof(x[0]))

template<class T> void In(T& x){cin>>x;}
template<class T> void In(T arr[], int n){for(int i=0;i<n;i++)cin>>arr[i];}
template<class T> void Out(T arr[], int n){ if(n>0) { cout<<arr[0]; for(int i=1;i<n;i++)cout<<" "<<arr[i];  cout<<endl;} }
ll gcd(ll a,ll b){ll r;while(b){r=a%b;a=b;b=r;}return a;}

int dp[505][20];

void Init()
{
    mset(dp,0);
}

char buf[1024];

const char* WELCOME = "welcome to code jam";

int main()
{
    int kcase = 0;
    int T;
    In(T);
    gets(buf);
    while(T--)
    {
        Init();
        gets(buf);
        for(int i = 0;buf[i];i++)
        {
            for(int j=0;j<=i && j<19;j++)
            {
                if(i!=0)
                {
                    dp[i][j] = dp[i-1][j];
                }
                else
                {
                    dp[i][j] = 0;
                }
                if(buf[i]==WELCOME[j])
                {
                    if(j!=0)
                    {
                        dp[i][j] += dp[i-1][j-1];
                    }
                    else
                    {
                        dp[i][j] += 1;
                    }
                    dp[i][j]%=10000;
                }
            }
        }
        printf("Case #%d: %.4d\n",++kcase,dp[strlen(buf)-1][18]%10000);
    }
}
