#include <iostream>
#include <queue>

using namespace std;
int n, k, r;
int g[1001];
int main(){
	    //freopen("input.txt", "r", stdin);
	    //freopen("out.txt", "w", stdout);
      int t, i;
      scanf("%d", &t);
      int cnt = 0;
      while(t--){
			      scanf("%d%d%d", &r, &k, &n);
			      for(i = 0; i < n; i++)
			          scanf("%d", &g[i]);
						queue<int> roll;
						for(i = 0; i < n; i++)
						    roll.push(g[i]);
						int ans = 0;
						int num = 1, s;
						for(i = 1; i <= r; i++){
						      int temp = 0;
						      num = 1;
						      while(num < n && temp + roll.front() <= k){
									      temp = temp + roll.front();
									      s = roll.front();;
									      num++;
									      roll.pop();
									      roll.push(s);
									}
									if(temp + roll.front() <= k){
									      temp = temp + roll.front();
									      s = roll.front();
									      roll.pop();
									      roll.push(s);
									}
									if(temp == 0)  break;
									ans += temp;
						}
						printf("Case #%d: %d\n", ++cnt, ans);
			}
      return 0;
}
