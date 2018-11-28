#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int main(int argc, char** argv) {
    int N;
    cin >> N >> ws;
    string welcome = "welcome to code jam";
    
    for (int i = 0; i < N; i++) {
        string input;
        int count = 0;
        getline(cin, input);
        int indexes[19];
        int k = 0;
        int length = input.length();
        indexes[0] = 0;
        while (k > -1) {
            while (indexes[k] < length && welcome[k] != input[indexes[k]]) {
                indexes[k]++;
            }
            if (indexes[k] == length) {
                k--;
                indexes[k]++;
            }
            else {
                k++;
                if (k == 19) {
                    count++;
                    k--;
                    indexes[k]++;
                }
                else {
                    indexes[k] = indexes[k-1] + 1;
                }
            }
        }
        cout << "Case #"
             << i + 1 << ": "
             << setfill('0') << setw(4) << count % 10000
             << endl;
    }
    return 0;
}