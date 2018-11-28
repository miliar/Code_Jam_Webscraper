#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

int get_no_digits(int n) {
    int res = 0;
    while (n != 0) {
        ++res;
        n /= 10;
    }
    return res;
}

int rotate_lsd(int n, const int no_digits) {
    if (n == 0) return n;
    int n1 = n;
    int lsd = n1 % 10;
    int b = 10;
    /*
    int b = 1;
    int lsd = 0;
    while (lsd == 0) {
        lsd = n1 % 10;
        n1 /= 10;
        b *= 10;
    }
    */
    int a = 1;
    for (int i = 1; i < no_digits; ++i)
        a *= 10;
    return (lsd * a) + (n / b);
}

bool is_palindrome(int n) {
    stringstream ss;
    ss << n;
    string s = ss.str();
    string rev = string(s.rbegin(), s.rend());
    if (rev.compare(s) == 0) return true;
    return false;
}

int main () {

    //ifstream ifs ( "pA.txt" , ifstream::in );

    int lc = 1;
    int T = 0;
    cin >> T;
    cin.get();
    while (!cin.eof()) {
        if (lc > T) break;

        int A, B;
        int res = 0;
        cin >> A >> B;

        int n, m, nd, mnd;
        for (n = A; n <= B; ++n) {
            m = n;
            nd = get_no_digits(m);
            if (is_palindrome(m)) mnd = (nd + 1) / 2;
            else mnd = nd - 1;
            for (int j = 0; j < mnd; ++j) {
                int mm = rotate_lsd(m, nd);
                if (mm != m) {
                    m = mm;
                    if (A <= m && n < m && m <= B) {
                        //cout << "( " << n << ", " << m << " )\n";
                        ++res;
                    }
                }
            }
        }
        cout << "Case #" << lc << ": " << res << endl;

        cin.get();
        ++lc;
    }

    //ifs.close();

    return 0;
}

