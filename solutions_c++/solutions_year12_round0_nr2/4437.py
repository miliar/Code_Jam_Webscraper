#include<iostream>
#include<algorithm>
using namespace std;

int n,s,p,ans;
int val[100];

void dfs(int now, int res, int cnt){
   if(cnt > s )return;
   if(now==n){
      ans = max(ans, res);
      return;
   }
   for(int i = 0 ; i <= 10 ; i++){
      for(int j = i ; j <= 10 ; j++){
	 for(int k = j ; k <= 10 ; k++){
	    if(i+j+k==val[now] && k>=p){
	       if(k-i==2)dfs(now+1, res+1, cnt+1);
	       else if(k-i < 2)dfs(now+1, res+1, cnt);
	    }
	 }
      }
   }
   dfs(now+1,res,cnt);
}

int main(){
   int T;
   cin >> T;
   for(int k = 1 ; k <= T ; k++){
      cin >> n >> s >> p;
      for(int j = 0 ; j < n ; j++)cin >> val[j];
      ans = 0;
      dfs(0,0,0);
      cout << "Case #" << k << ": " << ans << endl;
   }
   return 0;
}
