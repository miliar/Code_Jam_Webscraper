#include <iostream>
#include <vector>

using namespace std;

vector<int> construct(int n) {
    vector<int> a(n, 0);
    int count, j = 1;
    for (int i = 1; i <= n; ++i) {
        count = 0;
        for (j;; j = ((j) % n) + 1) {
            if (a[j - 1] != 0)
                continue;

            ++count;
            if (count == i) {
                a[j - 1] = i;
                break;
            }
        }
    }

    return a;
}


int main() {
    int numTestCases;
    int value;
    int size;
    int numIndices;
    cin >> numTestCases;
    for (int i = 0; i < numTestCases; ++i) {
        cin >> size;
        vector<int> a(construct(size));
        cin >> numIndices;
        cout << "Case #" << i + 1 << ":";
        for (int j = 0; j < numIndices; ++j) {
            cin >> value;
            cout << " " << a[value - 1];
        }

        cout << endl;
    }

    return 0;
}
