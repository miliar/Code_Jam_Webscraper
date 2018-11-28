#include<iostream>
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
    
    freopen("B-small-attempt0.in","r",stdin);
    freopen("tiles.out","w",stdout);
    
    long long int test, l, t, n, c, val, pos, ans = 0;
    long long int C[1000], a[1000];
    cin >> test;
    
    f(k,0,test) {
             
        pos = -1;     
        cin >> l >> t >> n >> c;
        for (int i = 0; i < c; i++) {
            
            cin >> val;C[i] = val*2;
        }
        
        f(i,0,n) {
            
            a[i] = C[i%c];ans += a[i];
        }
        
        long long int sum = 0, j = 0, x = -1;
        
        while (1) {
            
            if (sum + a[j] >= t) {
                    pos = j+1;
                    x = sum + a[j] - t;
                    break;
            }
            sum += a[j];j++;
        }
        long long int first = x, second = -1;
        
        f(i,pos,n) {
             
             if (a[i] >= first){
                      second = first;first = a[i];
             }
             else if (a[i] > second) second = a[i];
        }  
        
        cout << "Case #" << k + 1 << ": ";
        if (l == 1) {
             ans -= (first/2);
        }
        else if (l == 2) {
             ans -= ((first+second)/2);
        }     
        cout << ans << endl;
        ans = 0;
    }
    return 0;
    system("pause");
    
}        
            
                
                    
                    
    
    
