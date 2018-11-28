#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i=0; i<t; i++) {
        int n;
        cin >> n;
        vector<int> val;
        int sum=0;
        int xorsum=0;
        for(int j=0; j<n; j++) {
            int tmp;
            cin >> tmp;
            val.push_back(tmp);
            sum+=tmp;
            xorsum^=tmp;
        }
        sort(val.begin(),val.end());
        cout << "Case #" << i+1 << ": ";
        if (xorsum==0) {
            cout << sum - val[0];
        } else {
            cout << "NO";
        }
        cout << endl;
    }
    return 0;
}
