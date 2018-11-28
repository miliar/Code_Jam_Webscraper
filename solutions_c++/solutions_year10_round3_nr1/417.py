#include <iostream>
#include <map>

using namespace std;

typedef map<int, int> intmap;

void doCase(int caseNum) {
    int N;

    cin >> N;

    intmap AB;
    for (int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;

        AB[a] = b;
    }

    int intersections = 0;
    for (intmap::const_iterator it1 = AB.begin(); it1 != AB.end(); it1++) {
        int b1 = (*it1).second;

        for (intmap::const_iterator it2 = it1; it2 != AB.end(); it2++) {
            int b2 = (*it2).second;

            if (b2 < b1) {
                intersections++;
            }
        }
    }

    cout << "Case #" << caseNum << ": " << intersections << endl;
}

int main() {
    int T;

    cin >> T;

    for (int i = 0; i < T; i++) {
        doCase(i+1);
    }
}
