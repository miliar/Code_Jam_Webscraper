#include<cassert>
#include<cstdio>
#include<cstdlib>
#include<queue>
#include<stack>
#include<ctype.h>
#include<cmath>
#include<fstream>
#include<iostream>

using namespace std;

#define sz size()
#define st stringstream
#define len length()
#define f(i,p,n) for(int i=p;i<n;i++)
#define sort(v) sort(v.begin(),v.end())
#define pb push_back

int main() {
    
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    
    int test, value, sum = 0, minimum;
    int n;
    int a[100];
    cin >> test;
    
    f(k,0,test) {
        cin >> n;
        cin >> value;
        a[0] = value;
        minimum = value;
        sum = value;
        f(i,1,n) {
            cin >> value;
            sum += value;
            a[i] = value;
            if (value < minimum) minimum = value;
        }
        //f(i,0,n) cout << a[i] << " ";
        long long int xo = a[0];
        f(i,1,n) {
            
            xo ^= a[i];
        }
        //cout << xo << endl;
        if (xo == 0) {
                cout << "Case #" << k+1 << ": " << (sum-minimum) << endl;
        }
        else cout << "Case #" << k+1 << ": " << "NO" << endl;
    }
    return 0;
    system("pause");
    
}        
        
        
