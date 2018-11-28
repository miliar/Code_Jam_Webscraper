#include <iostream>

using namespace std;

void doCase(int caseNum) {
    int N, K;

    cin >> N >> K;

    bool isOn = (K % (1<<N)) == ((1<<N)-1);

    cout << "Case #" << caseNum << ": " << (isOn ? "ON" : "OFF") << endl;
}

int main() {
    int T;

    cin >> T;

    for (int i = 0; i < T; i++) {
        doCase(i+1);
    }
}
