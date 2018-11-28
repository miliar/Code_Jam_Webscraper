#include <iostream>
#include <cstdio>
#include <fstream>
using namespace std;
int main()
{
    ofstream f("a.txt");
    int t;
    cin >> t;
    int k = 1;
    while (t--) {
        string a, b, c, d;
        cin >> a >> b >> c >> d;
        getchar();
        string ca, cb, cc, cd;
        for (int i = 0; i < 4; i++) {
            if (i == 0) {
                ca.push_back(a[i]);
                ca.push_back(b[i]);
                ca.push_back(c[i]);
                ca.push_back(d[i]);
            } else if (i == 1) {
                cb.push_back(a[i]);
                cb.push_back(b[i]);
                cb.push_back(c[i]);
                cb.push_back(d[i]);
            } else if (i == 2) {
                cc.push_back(a[i]);
                cc.push_back(b[i]);
                cc.push_back(c[i]);
                cc.push_back(d[i]);
            } else if (i == 3) {
                cd.push_back(a[i]);
                cd.push_back(b[i]);
                cd.push_back(c[i]);
                cd.push_back(d[i]);
            }
        }
        string d1, d2;
        d1.push_back(a[0]);
        d1.push_back(b[1]);
        d1.push_back(c[2]);
        d1.push_back(d[3]);
        d2.push_back(a[3]);
        d2.push_back(b[2]);
        d2.push_back(c[1]);
        d2.push_back(d[0]);
        int co;
        int cx;
        int dot = 0;
        int final = 0;
        char w;

        co = 0;
        cx = 0;
        for (int i = 0; i < 4; i++) {
               if (a[i] == 'O' || a[i] == 'T') co++;
               if (a[i] == 'X' || a[i] == 'T') cx++;
               if (a[i] == '.') dot++;
        }
        if (co == 4) {
            final = 1;
            w = 'O';
            goto l;
        } else if (cx == 4) {
            final = 1;
            w = 'X';
            goto l;
        }

        co = 0;
        cx = 0;
        for (int i = 0; i < 4; i++) {
               if (b[i] == 'O' || b[i] == 'T') co++;
               if (b[i] == 'X' || b[i] == 'T') cx++;
               if (b[i] == '.') dot++;
        }
        if (co == 4) {
            final = 1;
            w = 'O';
            goto l;
        } else if (cx == 4) {
            final = 1;
            w = 'X';
            goto l;
        }

        co = 0;
        cx = 0;
        for (int i = 0; i < 4; i++) {
               if (c[i] == 'O' || c[i] == 'T') co++;
               if (c[i] == 'X' || c[i] == 'T') cx++;
               if (c[i] == '.') dot++;
        }
        if (co == 4) {
            final = 1;
            w = 'O';
            goto l;
        } else if (cx == 4) {
            final = 1;
            w = 'X';
            goto l;
        }

        co = 0;
        cx = 0;
        for (int i = 0; i < 4; i++) {
               if (d[i] == 'O' || d[i] == 'T') co++;
               if (d[i] == 'X' || d[i] == 'T') cx++;
               if (d[i] == '.') dot++;
        }
        if (co == 4) {
            final = 1;
            w = 'O';
            goto l;
        } else if (cx == 4) {
            final = 1;
            w = 'X';
            goto l;
        }

        co = 0;
        cx = 0;
        for (int i = 0; i < 4; i++) {
               if (ca[i] == 'O' || ca[i] == 'T') co++;
               if (ca[i] == 'X' || ca[i] == 'T') cx++;
               if (ca[i] == '.') dot++;
        }
        if (co == 4) {
            final = 1;
            w = 'O';
            goto l;
        } else if (cx == 4) {
            final = 1;
            w = 'X';
            goto l;
        }

        co = 0;
        cx = 0;
        for (int i = 0; i < 4; i++) {
               if (cb[i] == 'O' || cb[i] == 'T') co++;
               if (cb[i] == 'X' || cb[i] == 'T') cx++;
               if (cb[i] == '.') dot++;
        }
        if (co == 4) {
            final = 1;
            w = 'O';
            goto l;
        } else if (cx == 4) {
            final = 1;
            w = 'X';
            goto l;
        }

        co = 0;
        cx = 0;
        for (int i = 0; i < 4; i++) {
               if (cc[i] == 'O' || cc[i] == 'T') co++;
               if (cc[i] == 'X' || cc[i] == 'T') cx++;
               if (cc[i] == '.') dot++;
        }
        if (co == 4) {
            final = 1;
            w = 'O';
            goto l;
        } else if (cx == 4) {
            final = 1;
            w = 'X';
            goto l;
        }

        co = 0;
        cx = 0;
        for (int i = 0; i < 4; i++) {
               if (cd[i] == 'O' || cd[i] == 'T') co++;
               if (cd[i] == 'X' || cd[i] == 'T') cx++;
               if (cd[i] == '.') dot++;
        }
        if (co == 4) {
            final = 1;
            w = 'O';
            goto l;
        } else if (cx == 4) {
            final = 1;
            w = 'X';
            goto l;
        }

        co = 0;
        cx = 0;
        for (int i = 0; i < 4; i++) {
               if (d1[i] == 'O' || d1[i] == 'T') co++;
               if (d1[i] == 'X' || d1[i] == 'T') cx++;
               if (d1[i] == '.') dot++;
        }
        if (co == 4) {
            final = 1;
            w = 'O';
            goto l;
        } else if (cx == 4) {
            final = 1;
            w = 'X';
            goto l;
        }

        co = 0;
        cx = 0;

        for (int i = 0; i < 4; i++) {
               if (d2[i] == 'O' || d2[i] == 'T') co++;
               if (d2[i] == 'X' || d2[i] == 'T') cx++;
               if (d2[i] == '.') dot++;
        }
        if (co == 4) {
            final = 1;
            w = 'O';
            goto l;
        } else if (cx == 4) {
            final = 1;
            w = 'X';
            goto l;
        }

        l:
            if (final == 1) {
                cout << "Case #" << k++ << ": " << w << " won" << endl;
                f << "Case #" << k - 1 << ": " << w << " won" << endl;
            } else if (dot != 0) {
                cout << "Case #" << k++ << ": Game has not completed\n";
                f << "Case #" << k - 1 << ": Game has not completed\n";
            } else {
                cout << "Case #" << k++ << ": Draw\n";
                f << "Case #" << k - 1 << ": Draw\n";
            }
            getchar();
    }
    return 0;
}
