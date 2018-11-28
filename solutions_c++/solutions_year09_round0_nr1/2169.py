#include <iostream>
#include <iomanip>
using namespace std;

int const L=17, D=5002, N=502;
string s[D];
char w[L][128];

int main () {
    freopen ("in.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);
    int l, d, n;
    cin >> l >> d >> n;
    for (int i=0; i<d; i++)
        cin >> s[i];
    for (int i=0; i<n; i++) {
        string p;
        cin >> p;
        int k=0;
        memset(w, 0, sizeof w);
        for (int j=0; j<l; j++)
            if (p[k]=='(') {
                for (k++; p[k]!=')';)
                    w[j][p[k++]]=1;
                k++;
            }
            else w[j][p[k++]]=1;
        int res=0;
        for (int j=0; j<d; j++) {
            int f=1;
            for (int x=0; x<l; x++)
                if (!w[x][s[j][x]])
                    f=0;
            res+=f;
        }
        cout << "Case #" << i+1 << ": " << res << endl;

    }
    return 0;
}

