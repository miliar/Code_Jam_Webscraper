#include <iostream>
#include <string>
using namespace std;
const int D = 5000;

int l;
string w[D];
bool s[256][256];

void read_word() {
    string t; cin >> t;
    int it = 0;
    for(int i=0;i<l;i++,it++) {
        for (char c='a'; c<='z'; c++) s[i][c]=0;
        if (t[it]!='(') {
            s[i][t[it]]=1;
            continue;
        }
        it++;
        while (t[it]!=')') {
            s[i][t[it]]=1;
            it++;
        }
    }
}

int main() {
    int d,n;
    cin >> l >> d >> n;
    for(int i=0;i<d;i++) cin >> w[i];
    for(int i=1;i<=n;i++) {
        read_word();
        int c=0;
        for(int j=0;j<d;j++) {
            bool ok = 1;
            for(int k=0;k<l;k++) if (!s[k][w[j][k]]) {ok=0;break;}
            if (ok) c++;
        }
        cout << "Case #"<<i<<": "<<c<<endl;
    }
    return 0;
}


