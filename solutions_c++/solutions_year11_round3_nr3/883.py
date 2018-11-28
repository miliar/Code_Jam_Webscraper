#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int t,n,l,h;
    cin >> t;
        
    for(int i=1; i<=t; i++) {
        cin >> n >> l >> h;        
        vector<int> v(n);
        for(int j=0; j<n; j++) {
            cin >> v[j];
        }
        bool flag=0;
        int ans=-1;
        for(int k=l; k<=h; k++) {
            for(int m=0; m<n; m++) {
                if(!(k%v[m]==0 || v[m]%k==0)) {
                    flag=1;
                    break;
                }   
            }
            if(flag) {
                flag=0;
                continue;
            }
            ans=k;
            break;
        }
        cout << "Case #" << i << ": ";
        if(ans==-1) {
            cout << "NO" << endl;
        }
        else
            cout << ans << endl;           
    }
    return 0;
}
