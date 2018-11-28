#include <iostream>
#include <cstdio>

using namespace std;
int power[101];
int state[101];
int n, k;
int main(){
	      freopen("input.txt", "r", stdin);
	      freopen("out.txt", "w", stdout);
				int t, i, j;
				int cnt = 0;
				scanf("%d", &t);
				while(t--){
				     scanf("%d%d", &n, &k);
				     for(i = 1; i <= n; i++){
				         power[i] = 0;
				         state[i] = 0;
				     }
				     power[1] = 1;
				     for(i = 1; i <= k; i++){
						     state[1] = 1 - state[1];
						     for(j = 2; j <= n; j++)
						         if(power[j]) state[j] = 1 - state[j];
								 for(j = 1; j <= n; j ++){
								     if(state[j]) power[j+1] = 1;
								     else break;
								 }
								 for(++j;j <= n; j++)
								    power[j] = 0;
								//cout<<power[2]<<" "<<state[2]<<endl;
						 }
//						 for(i = 1; i <= n; i++)
//						     cout<<state[i]<<" ";
//						cout<<endl;
						 if(power[n]&&state[n])
						     printf("Case #%d: ON\n", ++cnt);
						 else
						     printf("Case #%d: OFF\n", ++cnt);
				}
        return 0;
}
