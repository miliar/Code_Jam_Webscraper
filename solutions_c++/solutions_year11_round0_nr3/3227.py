#include <iostream>

using namespace std;

int main()
{
    int t,n;
    cin >> t;
    long long mini;
    long long c;

    for(int i=1; i<=t; i++) {
        cin >> n;        
        cin >> mini;
        cout << "Case #" << i << ": ";        
        long long x=mini;
        long long sum=mini;                
        
        for(int j=1; j<n; j++) {
            cin >> c;
            sum+=c;
            x=x^c;
            if(c<mini)
                mini=c;
        }
        
        if(x==0) {
            cout << sum-mini << endl;
        }
        else
            cout << "NO" << endl;
    }
    
    return 0;
}
