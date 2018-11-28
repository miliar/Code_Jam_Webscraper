#include <iostream>
using namespace std;

/*
class Big {
public:
    int digits[9];
    int length;

    Big(int A) {
        length = 0;
        while (A > 0) {
            digits[length++] = A % 10;
            A /= 10;
        }
        for (int i = length; i < 9; ++i) {
            digits[i] = 0;
        }
    }

    int& operator[](int n) {
        return digits[n];
    }

    Big& operator++() {
        int i = 0;
        while (digits[i] == 9) {
            digits[i++] = 0;
        }
        digits[i] += 1;
        if (i == length) {
            ++length;
        }
    }

    bool operator==(const Big& A) const {
        if (length != A.length) {
            return false;
        }
        for (int i = 0; i < length; ++i) {
            if (digits[i] != A[i]) {
                return false;
            }
        }
        return true;
    }


};

ostream& operator<<(ostream& out, Big A) {
    for (int i = 0; i < A.length; ++i) {
        out << A[i] << ' ';
    }
    return out;
}
*/
int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int A, B, count = 0;
        cin >> A >> B;
        for (int n = A; n <= B; ++n) {
            int digits[20];
            int l = 0;
            for (int m = n; m > 0; m /= 10) {
                digits[l++] = m % 10;
            }
            for (int i = 0; i < l; ++i) {
                digits[2*l-1-i] = digits[i];
            }
            for (int i = 0; i < l; ++i) {
                digits[i] = digits[l+i];
            }
            for (int shift = 1; shift < l; ++shift) {
                int m = 0;
                for (int i = 0; i < l; ++i) {
                    m *= 10;
                    m += digits[shift + i];
                }
                if (m == n) {
                    break;
                }
                if (m >= A && m <= B) {
                    ++count;
                }
            }
        }
        cout << "Case #" << t << ": " << count / 2 << endl;
    }
}