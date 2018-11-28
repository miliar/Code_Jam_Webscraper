#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;
#define INF 2000000000
int tc;
vector<int> pri;
int ncell,npris,a;
int dp[505][505];
int min(int a, int b){if (a < b) return a; return b;}

int process(int left, int right){
 if (right <= left) return 0;
 if (dp[left][right] != -1) return dp[left][right];
 int res = INF;
 for (int i = left+1; i <= right-1; i++){
     res = min(res,process(left,i)+process(i,right)+(pri[i]-pri[left]-1)+(pri[right]-pri[i]-1));
 }    
 if (res == INF) res = 0;
 dp[left][right] = res;
 return res;
}


int main(){
  scanf("%d",&tc);
  for (int ti = 1; ti <= tc; ti++){
      scanf("%d %d",&ncell, &npris);
      memset(dp,-1,sizeof(dp));
      pri.clear();
      for (int i = 0; i < npris; i++){
          scanf("%d",&a);
          pri.push_back(a);  
      }
      pri.push_back(0); pri.push_back(ncell+1);
      sort(pri.begin(),pri.end());
      int res = INF;
      for (int i = 1; i < pri.size()-1; i++){
          res = min(res,process(0,i)+process(i,pri.size()-1)+(pri[i]-pri[0]-1)+(pri[pri.size()-1]-pri[i]-1));    
      }

      if (res == INF) res = 0;
      printf("Case #%d: %d\n",ti,res);
  }
     
}
