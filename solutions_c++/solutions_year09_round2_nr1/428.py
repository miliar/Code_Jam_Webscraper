#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

istringstream buff;
vector<string> attr;

void getprob(bool flag, double &p) {
    char ch1, ch2; double val;
    string word;
    buff >> ch1 >> val >> ch2;
    //cerr << "ch1 = " << ch1 << " ch2 = " << ch2 << " val = " << val << " p = " << p << '\n';
    if (ch2 == ')') {
        if (flag)
            p *= val;
    } else {
        buff.putback(ch2);
        buff >> word;
        if (!flag) {
            getprob(false, p);
            getprob(false, p);
        } else {
            p *= val;
            if (binary_search(attr.begin(), attr.end(), word)) {
                getprob(true, p);
                getprob(false, p);
            } else {
                getprob(false, p);
                getprob(true, p);
            }
        }
        buff >> ch2;
    }
}

int main() {
    int t; cin >> t;
    cout.precision(7);
    cout << fixed;
    for (int c = 1; c <= t; c++) {
        int l; cin >> l; cin.ignore();
        string lines;
        for (int i = 0; i < l; i++) {
            string line; getline(cin, line);
            lines += line + " ";
        }
        lines += " ";
        buff.str(lines);
        //cerr << buff.str() << '\n';
        int a; cin >> a;
        cout << "Case #" << c << ":\n";
        for (int i = 0; i < a; i++) {
            string name; int n;
            cin >> name >> n;
            //cerr << "name = " << name << '\n';
            attr.resize(n);
            for (int j = 0; j < n; j++)
                cin >> attr[j];
            sort(attr.begin(), attr.end());
            buff.seekg(0);
            double prob = 1.0;
            getprob(true, prob);
            cout << prob << '\n';
        }
    }
    return 0;
}
