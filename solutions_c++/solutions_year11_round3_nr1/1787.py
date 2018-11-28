//Data Structure includes
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>


//Other Includes
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>

using namespace std;

#define FOR(i,a,b)					for(int i=a;i<b;i++)
#define REP(i,n)					FOR(i,0,n)
#define pb						 	push_back
#define mp						 	make_pair
#define s(n)						scanf("%d",&n)
#define sl(n) 						scanf("%lld",&n)
#define sf(n) 						scanf("%lf",&n)
#define ss(n) 						scanf("%s",n)
#define fill(a,v) 					memset(a, v, sizeof a)
#define sz							size()
#define INF							(int)1e9
#define EPS							1e-9
#define bitcount					__builtin_popcount
#define all(x)						x.begin(), x.end()
#define gcd							__gcd
#define maX(a,b)					(a>b?a:b)
#define miN(a,b)					(a<b?a:b)

typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef long long LL;
typedef pair<int, int > PII;
typedef pair<LL, LL > PLL;

int main()
{
    int t;cin >> t;
    int kase=0;
    while(t--)
    {
              int m,n;cin >> n >> m;
              kase++;
              char arr[100][100];
              REP(i,n)
              {
                      REP(j,m)
                      {
                              cin >> arr[i][j];
                      
                      }
              }
              int fl =0;
              REP(i,n)
              {
                      REP(j,m)
                      {
                              if(arr[i][j] == '#')
                              {
                                           arr[i][j] = '/';
                                           if(i+1 < n && arr[i+1][j]=='#')
                                           arr[i+1][j]= '\\';
                                           else fl=1;
                                           if(j+1 < m && arr[i][j+1]=='#')
                                           arr[i][j+1]='\\';
                                           else fl=1;
                                           if(i+1 < n && j+1 < m && arr[i+1][j+1] == '#')
                                           arr[i+1][j+1]='/';
                                           else fl=1;
                              }
                      }
              }
              
              cout << "Case #"<<kase<<":\n" ;
              if(fl) cout<< "Impossible" << endl;
              else 
              {
                   REP(i,n)
                   {
                   REP(j,m)
                   cout << arr[i][j];
                   cout <<"\n";
                   }
              }
    }
    return 0;
}
                      
