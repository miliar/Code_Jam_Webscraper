#include <iostream>
#include <algorithm>
using namespace std;


main() {
    int n;
    cin >> n; 
    for (int i=0;i<n;i++) {
        int x, min, m, sum;
        cin >> m >> x;
        min = x;
        sum = x;
        for (int j=1;j<m;j++) {
            int c;
            cin >> c;
            if (min > c) min = c;
            x ^= c;
            sum +=c;
        }
        cout <<"Case #" << i+1 << ": ";
        if (x!=0) cout << "NO";
        else cout << sum - min;
        cout << endl;
    }


}
