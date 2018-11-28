#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<math.h>
#include<string>
#include<map>
using namespace std;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
#define For(i,a,b) for(i=a;i!=b;i++)
#define Rep(i,n) For(i,0,n)
#define GI ({int t;scanf("%d",&t);t;})
#define pb push_back
#define set(a,c) memset(a,c,sizeof(a))
#define INF (int)1e8
int dp[110][1010];
vector<string> S;
vector<string> Q;
char c;
int main() {
    int t = GI;
    int i,j,k;
    int test;
    Rep (test,t) {
          int s = GI;
          S.clear();
          c = getchar();
          Rep(i,s)
          {
                  string tmp="";
                  while ((c=getchar()) != '\n')
                        tmp += c;
                  S.pb(tmp);
          }
          int q = GI;
          Q.clear();
          c = getchar();
          Rep(i,q)
          {
                  string tmp="";
                  while ((c=getchar()) != '\n')
                        tmp += c;
                  Q.pb(tmp);
          }
          For(j,1,q+1)
          {
           For(i,1,s+1)
           {
                   dp[i][j] = INF;
                   if (S[i-1] == Q[j-1])
                      continue;
                   if (j == 1) {
                         dp[i][j] = 0;
                   } else {
                          For(k,1,s+1) {
                              if (k == i)
                                 dp[i][j] <?= dp[k][j-1];
                              else
                                  dp[i][j] <?= dp[k][j-1] + 1;
                          }
                   }
           }
          }
          int mn = INF;
          For(i,1,s+1)
              mn <?= dp[i][q];
          cout << "Case #" << test+1 << ": " << mn << endl;
    }
    system("pause");
}
