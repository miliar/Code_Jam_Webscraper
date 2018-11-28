#include <iostream>
#include <string>
using namespace std;


string b = "welcome to code jam";
int n = b.size();
int a[100];
string s;

void done() {
     memset(a, 0, sizeof(a));
     for (int i =0; i < s.size(); ++i) {
         for (int j = b.size() - 1; j >=1; --j) {
            if (s[i] == b[j]) {
                a[j] = (a[j]+a[j-1]) %10000;
            }
         }
         if (s[i] == b[0]) a[0]++;
     }
     int r = a[b.size() -1];
     cout << r/1000 << r/100%10 << r/10%10 << r%10 << endl;
}
     
int main() {
    int T;
    char cc[1000];
    cin >> T;
    cin.getline(cc, 1000);
    for (int i = 0; i < T; ++i) {
       cout << "Case #" << i + 1 << ": ";
       cin.getline(cc, 1000);
       s = cc;
       done();
    }
    return 0;
}
     
