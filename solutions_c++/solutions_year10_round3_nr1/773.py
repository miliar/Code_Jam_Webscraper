#include<iostream>

using namespace std;

int main() {
    int first[1005];
    int second[1005];
    int T;
    cin >> T;
    for(int kase = 0; kase < T; kase++) {
        int n;
        cin >> n;
        for(int i = 0; i < n; i++) {
            cin >> first[i] >> second[i];
        }
        int count = 0;
        for(int i = 0; i < n; i++) {
            for(int j = i+1; j < n; j++) {
                if(first[i] < first[j]) {
                    if(second[i] > second[j]) {
                        count++;
                    }
                } else {
                    if(second[i] < second[j]) {
                        count++;
                    }
                }
            }
        }

        cout << "Case #" << (kase +1) << ": " << count << endl;
    }
}
