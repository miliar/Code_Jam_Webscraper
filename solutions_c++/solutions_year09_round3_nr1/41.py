#include <iostream>
#include <string>
using namespace std;

void done(string &s) {
     int a[100];
     memset(a, 0xff, sizeof(a));
     int m[255];
     memset(m ,0xff, sizeof(m));
     m[s[0]] = 1;
     int now = 0;
     for (int i =0; i < s.size(); ++i) {
         if (m[s[i]] < 0) {
            m[s[i]] = now;
            if (now == 0) now=2;
            else now++;
         }
     }
     if (now < 2) now = 2;
     //cout << now << "-";
     long long ret = 0;
     for (int i = 0; i < s.size(); ++i) {
         a[i] = m[s[i]];
         ret = ret * now + a[i];
     }
     cout << ret << endl;
}
int main() {
    int as;
    cin >> as;
    for (int kk=0; kk < as; ++kk) {
        cout << "Case #" << kk+1 << ": ";
        string s;
        cin >> s;
        done(s);
    }
    return 0;
}
