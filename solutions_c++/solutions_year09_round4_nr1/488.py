#include <iostream>
#include <string>
using namespace std;

int n;
string s[100];
int a[100];

void outout() {
     for (int i = 0; i < n; ++i){for (int j = 0; j < n; ++j) {
         cout << s[i][j] ;
         }cout << endl;
         }
     }
void done() {
    int ret= 0;
    for (int i = 0; i < n; ++i) {
        int j;
        for (j = i; j < n; ++j) {
            if (a[j] <= i) break;
        }
        //if (j == n)      cout << j << "xx"<<endl;//   outout();
        ret += (j-i);
        int t = a[j];
        for (int k = j;k >i; --k) a[k] = a[k-1];
        a[i] = t;
        
       // for (int j = 0; j < n; ++j) cout << a[j] << " "; cout<< endl;
    }
    cout << ret << endl;
        
}
int main() {
    int as;
    cin >> as;
    for (int kk=0; kk < as; ++kk) {
        cout << "Case #" << kk+1 << ": ";
        cin >> n;
        for (int i = 0; i < n; ++i) cin >> s[i];
        for (int i = 0; i < n; ++i) a[i] = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j)
                if (s[i][j] == '1') a[i] = j;
        }
        done();
    }
    return 0;
}
