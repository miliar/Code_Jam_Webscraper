#include <iostream>

using namespace std;

const int MAX_A = 1000000;
const int MAX_B = 1000000;

bool check(int A, int B) {
    if (B > A) {
        return check (B, A);
    }
    if (B == 0) {
        return false;
    }
    if (A == 0) {
        return false;
    }
    if (A == B) {
        return false;
    }
    if (A % B == 0) {
        return true;
    }
    bool temp1 = check(B, A%B);
    if (temp1 == false) {
        return true;
    }
    if (A > 2*B) {
        bool temp2 = check((A%B)+B, B);
        if (temp2 == false) {
            return true;
        }
    }
    return false;
}

int main() {
    int TT;
    int AA_1;
    int AA_2;
    int BB_1;
    int BB_2;
    int count = 0;
    cin >> TT;
    for (int z = 1; z <= TT; z++) {
        count = 0;
        cin >> AA_1 >> AA_2 >> BB_1 >> BB_2;
        for (int i = AA_1; i <= AA_2; i++) {
            for (int j = BB_1; j <= BB_2; j++) {
                if (check(i,j)) {
                    count++;
                }
            }
        }
        cout << "Case #" << z << ": " << count << endl; 
    }
}