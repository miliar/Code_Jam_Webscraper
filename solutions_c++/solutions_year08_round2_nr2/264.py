#include <iostream>
#include <set>
#include <vector>
using namespace std;

#define pb push_back

long long A, B, P;
int label[1005];

vector <int> desc(int X) {
    vector <int> f;
    int oldX = X;
    int i = 2, p;
    while(X > 1 && i * i <= oldX) {
        p = 0;
        while(X % i == 0 && X > 1) {
            X /= i;
            ++p;
        }
        if(p && i >= P)
            f.pb(i);
        ++i;
    }
    if(X > 1 && X >= P)
        f.pb(X);
    return f;
}

bool condition(int i, int j) {
    vector <int> vi = desc(i);
    vector <int> vj = desc(j);
    for(size_t k = 0; k < vi.size(); ++k)
        for(size_t l = 0; l < vj.size(); ++l)
            if(vi[k] == vj[l])
                return true;
    return false;
}


int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int T;
    cin >> T;
    for(int kk = 1; kk <= T; ++kk) {
        cin >> A >> B >> P;
        for(int i = A; i <= B; ++i)
            label[i] = i;
        for(int i = A; i <= B; ++i)
            for(int j = i + 1; j <= B; ++j)
                if(label[i] != label[j] && condition(i, j)) {
                    int old = label[j];
                    for(int k = A; k <= B; ++k) {
                        if(label[k] == old)
                            label[k] = label[i];
                    }
                }
        set <int> S;
        for(int i = A; i <= B; ++i)
            S.insert(label[i]);
        cout << "Case #" << kk << ": " << S.size();
        if(kk < T)
            cout << "\n";
    }
    return 0;
}
