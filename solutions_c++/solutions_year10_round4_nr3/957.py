#include <iostream>

using namespace std;

const int MAX = 100;
int CC;
int RR;
bool b[MAX+1][MAX+1];
int XX1;
int XX2;
int YY1;
int YY2;
int count;
int answer;

int main() {
    cin >> CC;
    for (int z = 1; z <= CC; z++) {
        count = 0;
        answer = 0;
        for (int j = 1; j <= MAX; j++) {
            for (int k = 1; k <= MAX; k++) {
                b[j][k] = false;
            }
        }
        cin >> RR;
        for (int i = 0; i < RR; i++) {
            cin >> XX1 >> YY1 >> XX2 >> YY2;
            for (int j = XX1; j <= XX2; j++) {
                for (int k = YY1; k <= YY2; k++) {
                    if (not b[j][k]) {
                        b[j][k] = true;
                        count++;
                    }
                }
            }
        }
        while (count > 0) {
            answer++;
            for (int j = MAX; j > 0; j--) {
                for (int k = MAX; k > 0; k--) {
                    if (b[j-1][k] and b[j][k-1] and (not b[j][k])) {
                        b[j][k] = true;
                        count++;
                    }
                    if ((not b[j-1][k]) and (not b[j][k-1]) and b[j][k]) {
                        b[j][k] = false;
                        count--;
                    }
                }
            }
        }
        cout << "Case #" << z << ": " << answer << endl;
        
    }
}