#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
#include <set>
using namespace std;

int main() {
    string a,b;
    int T;
    char aa[300];

    cin >> T;
    for(int cc=1;cc<=T;cc++) {
        cin >> a;

        set<char> ss;
        aa[a[0]]=1; ss.insert(a[0]);
        int base = 0;
        for(int i=1;i<a.size();i++)
            if(ss.find(a[i])==ss.end()) {
                aa[a[i]]=base++;
                if(base==1) base++;
                ss.insert(a[i]);
            }

        if(base==0) base=2;

        long long res = 0;
        long long t;
        for(int i=a.size()-1, t=1;i>=0;i--,t*=base) {
            res+=(aa[a[i]])*t;
        }

        printf("Case #%d: %lld\n", cc, res);
    }

    return 0;
}
