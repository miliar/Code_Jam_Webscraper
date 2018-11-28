#include <string>
#include <cstring>
#include <cstdio>
#include <iostream>
#include <map>
using namespace std;
string next_shift(string a){
    string n = a[a.length() - 1] + a;
    n.resize(a.size());
    return n;
}
map<pair<string, string> , int > mms;
int main() {
    freopen("in", "r", stdin);
    int N, cou, nnn;
    cin >> N;
    string a,b,s,m,p;
    int i=0;
    char ma[8];
    while(N){
        mms.clear();
        cou=0;
        int A, B;
        cin >> A >> B;
        sprintf(ma, "%d", A);
        a = ma;
        nnn=a.length();
        sprintf(ma, "%d", B);
        b = ma;
        for(int ii=A;ii<=B;ii++){
            sprintf(ma, "%d", ii);
            s = ma;
            p = s;
            for(int iii=0;iii<nnn;iii++){
            m = next_shift(p);
            p = m;
            if(a<=s && s<m && m<=b){
                if(mms[make_pair(s, p)])continue;
                else mms[make_pair(s, p)] = ++cou;
                }
            }
        }
        cout << "Case #" << ++i << ": "  << cou << endl;
        N--;
    }
    return 0;
}
