#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int cnt=1;cnt<=t;cnt++) {
        int n;
        cin >> n;
        vector<int> a(n), b(n);
        for(int i=0;i<n;i++) {
            cin >> a[i] >> b[i];
        }
        int ans = 0;
        for(int i=0;i<n;i++) {
            for(int j=i+1;j<n;j++) {
                if((a[i]-a[j])*(b[i]-b[j]) < 0) {
                    ans++;
                }
            }
        }
        cout << "Case #" << cnt << ": " << ans << endl;
    }
    
    return 0;
}
