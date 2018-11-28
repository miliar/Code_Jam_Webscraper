#include <iostream>
#include <vector>
using namespace std;

vector<int> tranferToVector(int num) {
    vector<int> ret;
    int tmp = num;
    while (tmp) {
        ret.push_back(tmp % 10);
        tmp /= 10;
    }
    while (num) {
        ret.push_back(num % 10);
        num /= 10;
    }
    reverse(ret.begin(), ret.end());
    return ret;
}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int a, b, tot;
        tot = 0;
        cin >> a >> b;
        for (int num1 = a; num1 <= b; num1++) {
            vector<int> list = tranferToVector(num1);
            for (int i = 1; i < list.size() / 2; i++) {
                int num2 = 0;
                for (int j = 0; j < list.size() / 2 ; j++) {
                    num2 = num2 * 10 + list[i + j];
                }
                if (num2 >= a && num2 <= b && num1 < num2) {
                    //cout << num1 << " " << num2 << endl;
                    tot++;
                }
            }
        }
        cout << "Case #" << i + 1 << ": " << tot << endl;
    }
    return 0;
}
