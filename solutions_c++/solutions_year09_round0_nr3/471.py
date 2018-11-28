#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> mi;

int main() {
    int N;
    cin >> N;
    string txt = "welcome to code jam";
    const char* cstr = txt.c_str();
    const int txt_size = txt.size();
    const int buflen = 501;
    const int mod = 10000;
    char buf[buflen];
    cin.getline(buf, buflen);
    for (int i=0; i<N; ++i) {
        cin.getline(buf, buflen);
        int slen = strlen(buf);
        mi m(txt_size+1, vi(slen+1, 1));
        for (int j=0; j<txt_size; ++j) {
            m[j+1][0] = 0;
            for (int k=0; k<slen; ++k) {
                if (cstr[j] != buf[k]) m[j+1][k+1] = 0;
            }
        }

        for (int j=1; j<=txt_size; ++j) {
            for (int k=1; k<=slen; ++k)
                m[j][k] = (m[j][k-1] + (m[j][k]*m[j-1][k-1])%mod)%mod;
        }
        cout << "Case #" << i+1 << ": " << setfill('0') << setw(4) << m[txt_size][slen] << "\n";
    }
}
