#include <iostream>

using namespace std;

int main() {
    int t;
    cin>>t;
    for (int i=0;i<t;i++) {
        int n;
        cin>>n;
        int val = 0;
        int mval = 10000000;
        int sum = 0;
        for (int j = 0;j<n;j++) {
            int tt;
            cin>>tt;
            val = val ^ tt;
            mval <?= tt;
            sum+= tt;
        }
        cout<<"Case #"<<(i+1)<<": ";
        if (val) cout<<"NO"<<endl;
        else {
            cout<<(sum - mval)<<endl;
        }
    }
    return 0;
}
