#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>

using namespace std;

inline int ChrToInt (char c)
{
    return c - '0';
}

int StrToInt (string s)
{
    int res = 0, factor = 1;
    for (int i = (int) s.length ()-1; i >= 0; i--) {
        res += factor * ChrToInt (s [i]);
        factor *= 10;
    }
    if (s [0] != 0) return res; else return -1;
}

char IntToChr (int x)
{
    return char ('0' + x);
}

string IntToStr (int x)
{
    string res = "";
    if (x == 0) return "0";

    while (x) {
        res = IntToChr (x % 10) + res;
        x /= 10;
    }
    return res;
}

int used [2000000+42];

int main ()
{
    ifstream in ("input.txt");
    ofstream out ("output.txt");
    int T;

    in >> T;
    for (int i=1; i <= T; i++) {
        int a, b;
        //string sa = IntToStr (a), sb = IntToStr (b);
        in >> a >> b;
        int ans = 0;
        for (int i=a; i <= b; i++) {
            for (int j=a; j <= b; j++) used [j] = false;
            string num = IntToStr (i);
            for (size_t j=1; j <= num.length (); j++) {
                rotate (num.begin(), num.end() - 1, num.end());
                int x = StrToInt (num);
                if (a <= i && i < x && x <= b && !used [x]) {
                    used [x] = true;
                    ans++;
                    //out << i << " " << x << endl;
                }
            }
        }

        out << "Case #" << i << ": " << ans << endl;
    }
    return 0;
}
