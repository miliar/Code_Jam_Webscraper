#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int q=1; q<=t; q++) {
        int n;
        cin >> n;
        vector <int> numbers,numbers2;
        for (int i=0; i<n; i++) {
            int x;
            cin >> x;
            numbers.push_back(x);
            numbers2.push_back(x);
        }
        sort(numbers2.begin(),numbers2.end());
        int ans=0;
        for (int i=0; i<n; i++) {
            if (numbers[i]!=numbers2[i]) ans++;
        }
        cout << "Case #" << q <<": ";
        printf("%.6f\n",(float) ans);
    }
    return 0;
}
