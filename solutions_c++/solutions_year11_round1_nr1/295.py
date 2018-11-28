#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cmath>
#include <cstdio>

#define all(v) (v).begin(), (v).end()

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T;
    cin>>T;
    
    for(int caso=1; caso<=T; caso++)
    {
        cout<<"Case #"<<caso<<": ";
        
        long long N, Pd, Pg;
        cin>>N>>Pd>>Pg;
        
        int a = Pd, b = 100 - Pd, k = __gcd(a, b);
        a /= k;
        b /= k;
        
        int A = Pg, B = 100 - Pg, K = __gcd(A, B);
        A /= K;
        B /= K;
        
        if(a + b > N) cout<<"Broken"<<endl;
        else
        {
            if(A == 0 && a != 0) cout<<"Broken"<<endl;
            else if(B == 0 && b != 0) cout<<"Broken"<<endl;
            else cout<<"Possible"<<endl;
        }
    }
    
    return 0;
}
