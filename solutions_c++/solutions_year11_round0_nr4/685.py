#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int mainloop=0; mainloop<t; mainloop++) {
        int n;
        cin >> n;
        int count=0;
        for (int i=1; i<=n; i++) {
            int tmp;
            cin >> tmp;
            if (tmp != i)count++;
        }
        cout << "Case #" << mainloop+1 << ": ";
        cout << (double)count;
        cout << endl;
    }
    return 0;
}
