#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int c,d,n;
char C[26][26];
int D[26][26];

vector<char> v;

bool f() { //retorna si hi ha canvis o no
    int m = v.size();
    if (m<2) return 0;
    char nc=C[v[m-1]-'A'][v[m-2]-'A'];
    if (nc!='?') {
        v.erase(v.begin()+m-1);
        v[m-2]=nc;
        return 1;
    }
    for (int i=0;i<m-1;++i) if (D[v[m-1]-'A'][v[i]-'A']) {
        v.clear();
        return 1;
    }
    return 0;
}

int main() {
    int t; cin >> t;
    for (int cas=1;cas<=t;++cas) {
        for (int i=0;i<26;++i) for (int j=0;j<26;++j) {
            C[i][j]='?'; //que generen
            D[i][j]=0;//si son incompatibles
        }
        v.clear();
        
        cin >> c;
        for (int i=0;i<c;++i) {
            char c1,c2,c3; cin >> c1>>c2>>c3;
            C[c1-'A'][c2-'A']=C[c2-'A'][c1-'A']=c3;
        }
        cin >> d;
        for (int i=0;i<d;++i) {
            char c1,c2; cin >> c1>>c2;
            D[c1-'A'][c2-'A']=D[c2-'A'][c1-'A']=1;
        }
        cin >> n;
        for (int i=0;i<n;++i) {
            char c1; cin >> c1;
            v.push_back(c1);
            while(f());
        }
        cout << "Case #" << cas << ": ";
        cout <<'[';
        for (int i=0;i<v.size();++i) {
            if (i>0) cout <<", ";
            cout <<v[i];
        }
        cout <<']' << endl;
        
    }
}
