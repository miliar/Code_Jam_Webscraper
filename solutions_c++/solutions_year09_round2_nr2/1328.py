#include <string>
#include <iostream>
#include <vector>
#include <map>
using namespace std;
vector<int> appear;
int isOk(int _z) {
    int z = _z;
    vector<int> copy = appear;
    while (z) {
        copy[z%10]--;
        z/=10;
    }
    for (int x = 1; x<10; x++) {
        if (copy[x]) return 0;
    }
    return 1;
}
int next(int t) {
    int tt=t;
    appear.clear();
    for (int x = 0; x < 10; x++) appear.push_back(0);
    while (tt) {
       appear[tt%10]++;
       tt/=10;
    }

    for (int z = t+1; ; z++) {
         if (isOk(z)) return z;
    }
}
int main() {
    int c, t;
    cin >> c;
    for (int x = 0; x < c; x++) {
        cin >> t;
        cout << "Case #" << x+1 << ": " << next(t) << endl;
    }
}

