#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int i=0;i<t;i++) {
        int n;
        cin >> n;
        vector<int> x(n), y(n);
        for(int j=0;j<n;j++)
            cin >> x[j];
        for(int j=0;j<n;j++)
            cin >> y[j];
        sort(x.begin(), x.end(), less<int>());
        sort(y.begin(), y.end(), greater<int>());
        int sum = 0;
        for(int j=0;j<n;j++) {
            sum += x[j]*y[j];
        }
        cout << "Case #" << i+1 << ": " << sum << endl;
    }

    return 0;
}
