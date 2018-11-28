#include <iostream>
#include <vector>

using namespace std;

typedef vector<int> vi;
typedef vector<char> vc;

int main() {
    int L, D, N;
    cin >> L >> D >> N;
    char* const arr = new char[L*D];
    for (int i=0; i<D; ++i) {
        char* f = arr + i;
        for (int j=0; j<L; ++j) {
            char c;
            cin >> c;
            *f = c;
            f += D;
        }
    }

    for (int i=0; i<N; ++i) {
        // init
        vi b(D, 0);
        string p;
        cin >> p;
        const char* ps = p.c_str();
        const char* f = arr;
        for (int l=0; l<L; ++l, f += D) {
            vc cs;
            char c;
            if ((c = *ps++) == '(')
                while ((c = *ps++) != ')')
                    cs.push_back(c);
            else
                cs.push_back(c);

            for (int j=0; j<int(cs.size()); ++j) {
                char csj = cs[j];
                for (int k=0; k<D; ++k)
                    if (f[k] == csj) ++b[k];
            }
        }
        int cnt = 0;
        for (int j=0; j<D; ++j)
            if (b[j] == L) ++cnt;
        cout << "Case #" << i+1 << ": " << cnt << "\n";
    }

    delete [] arr;
}
