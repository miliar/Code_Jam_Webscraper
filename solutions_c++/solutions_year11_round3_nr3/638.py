#include<vector>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<set>
#include<string.h>
#include<map>
#include<algorithm>
#include<cassert>
#include<cstdio>
#include<cstdlib>
#include<queue>
#include<stack>
#include<ctype.h>
#include<cmath>
#include<fstream>

using namespace std;

#define sz size()
#define st stringstream
#define len length()
#define f(i,p,n) for(int i=p;i<n;i++)
#define sort(v) sort(v.begin(),v.end())
#define pb push_back


int main() {
    
    
    freopen("C-small-attempt1.in","r",stdin);
    freopen("tiles.out","w",stdout);
    
    
    int t, n, l, h;
    int a[100], val, ans = -1;
    
    cin >> t;
    
    f(k,0,t) {
             
        cin >> n >> l >> h;
        f(i,0,n) {
            
            cin >> val;
            a[i] = val;
        }
        bool boo = false;
        for (int i = l; i <= h; i++) {
            boo = false;
            f(j,0,n) {
                if ((a[j] % i != 0) && (i%a[j] != 0)) {
                    
                    boo = true;
                    break;
                }
           }
           if (!boo) {
               ans = i;
               break;
           }
       }
       
       cout << "Case #" << k + 1 << ": ";
       if (ans == -1) cout << "NO" << endl;
       else cout << ans << endl;
       ans = -1;
   }
   return 0;
   system("pause");
   
}                             
             
        
