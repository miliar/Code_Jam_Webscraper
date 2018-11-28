#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int main() {
    int N;
    cin >> N;
    for (int n = 0; n < N; n++) {
        string num;
        cin >> num;

        string buf = num;
        bool worked = next_permutation(buf.begin(), buf.end());
        cout << "Case #" << n + 1 << ": ";
        if (worked)
            cout << buf;
        else {
            sort(num.begin(), num.end());
            int i = num.rfind('0');
            cout << num[i+1];
            for (int j = 0; j <= i; j++)
                 cout << '0';
            cout << '0';
            cout << num.substr(i+2);
        }
        cout << '\n';
    }
}
