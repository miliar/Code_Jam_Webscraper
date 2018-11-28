#include<iostream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>
#include<string>

using namespace std;

int n,m;
int s[1100],f[12],ind[1100];
vector<int> cost[20],mat[20];
bool vis[11][1100];

bool cmp(int A,int B){
  return s[A] < s[B];
}

void solve(){
    memset(vis,false,sizeof(vis));
    for (int i = 0; i < n; i++)
    {
       int k = ind[i];
//       printf("%d\n", k);
       int tot = 0;
//       printf("  %d\n", s[ind[i]]);
       while (tot < m){
          k /= 2;
          if (tot >= s[ind[i]]) 
          {
             vis[tot][k] = true;
          }
          tot++;
       }
    }
    int ans = 0 , k = n / 2;
    for (int i = 0; i < m ; i++)
    {
       for (int j = 0; j < k ; j++)
         if (vis[i][j]) ans++;
//           else printf("%d\n", 555);
       k /= 2;
    }
    printf("%d\n", ans);
}

int main(){
    f[0] = 1;
    for (int i = 1; i < 12 ; i++)
      f[i] = f[i - 1] * 2;
//    freopen("test.txt","r",stdin);
//    freopen("B.out","w",stdout);
    int T;
    scanf("%d", &T);
    for (int p = 1; p <= T ; p++)
    {
       printf("Case #%d: ", p);
       scanf("%d", &n);
       m = n;
       n = f[n];
       for (int i = 0; i < n ; i++)
       {
          scanf("%d", &s[i]);
          ind[i] = i;
       }
       sort(ind , ind + n , cmp);
       int k = n / 2;
       for (int i = 0; i < m ; i++)
       {
          cost[i].clear();
          int u;
          for (int j = 0; j < k ; j++)
          {
              scanf("%d", &u);
              cost[i].push_back(u);
          }
          k /= 2;
       }
       solve();
    }
    return 0;
}
  
