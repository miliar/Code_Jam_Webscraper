/*
ID: mkagenius1
LANG: C++
TASK:
*/

#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<map>
#include<string.h>
#include<string>
#include<vector>
#include<math.h>
#include<set>
#include<queue>

using namespace std;

int isvalid(int a, int b, int c){
    if(a <0 || b < 0 || c < 0) return false;
    int list[] = {a,b,c};
    sort(list, list + 3);
    return (list[2] - list[0]) ;
}
/* Main Code goes Here-after */
int main()
{
    int t; cin >> t;
    int kase = 0;
    while(t--){
        kase ++;
        int n; cin >> n;
        int sur ; cin >> sur;
        int lim; cin >> lim; lim--;
        int sum[n];
        for(int i = 0; i < n; i++){
            cin >> sum[i];
        }
        sort(sum, sum + n);
        reverse(sum, sum + n);
        int surprising[n], notsurprising[n];
        for(int i = 0; i < n; i++){
             int mod = sum[i] % 3;
             if(mod == 2){
                    surprising[i] = sum[i]/3 + 2;
                    notsurprising[i] = surprising[i] - 1;
             }else{
                    surprising[i] = sum[i]/3 + 1;
                    notsurprising[i] = surprising[i] ;
                    if(mod == 0)  notsurprising[i]--;
                    if(sum[i] <= 1) surprising[i] = -1;
             }
        }
        bool done[n];
        int ans = 0;
        memset(done, 0, sizeof done);
        for(int i = 0; i < n; i++){
            if(surprising[i] > lim && notsurprising[i] > lim && !done[i]){
                done[i] = true;
                ans ++;
            }
        }
        int now  = ans;
        for(int i = 0; i < n; i++){
            if(done[i]) continue;
            if(sur <= 0) continue;
            if(sur > 0){
                done[i] = 1;
                sur --;
                if(surprising[i] > lim )ans ++;
            }
        }
        //cout << ans <<"asasa"<< endl;
        for(int i = 0; i < n; i ++){
            if(done[i]) continue;
            //cout << sum[i] << "oooooo===>" << notsurprising[i] << "<====oooooo\n";
            if(notsurprising[i] > lim){
                 ans++;
                 
            }
            done[i] = 1;
        }
        //for(int i = 0; i < n; i++) cout << done[i] << " , " ;
        cout << "Case #"<<kase << ": " << ans << endl;
    }
    return 0;
}
            
                
        
                    
            
            
