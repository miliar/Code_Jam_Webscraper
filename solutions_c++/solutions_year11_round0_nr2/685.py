#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i=0; i<t; i++) {
        map<char,map<char,char> > comb;
        map<char,map<char,int> > oppose;
        string r; 
        int c,d,n;
        string cstr,dstr,nstr,ctmp,dtmp;
        cin >> c;
        for(int j=0; j<c; j++){
            cin >> ctmp;
            cstr+=ctmp;
        }
        cin >> d;
        for(int j=0; j<d; j++){
            cin >>dtmp;
            dstr+=dtmp;
        }
        cin >> n;
        if (n>0)cin >> nstr;
        for (int j=0; j<c; j++) {
            comb[cstr[j*3]][cstr[j*3+1]]=cstr[j*3+2];
            comb[cstr[j*3+1]][cstr[j*3]]=cstr[j*3+2];
        }
        for (int j=0; j<d; j++) {
            oppose[dstr[j*2]][dstr[j*2+1]]=1;
            oppose[dstr[j*2+1]][dstr[j*2]]=1;
        }
        for (int j=0; j<n; j++) {
            if (r.size()>=1) {
                //comb
                if (comb[r[r.size()-1]][nstr[j]] != 0) {
                    r[r.size()-1] = comb[r[r.size()-1]][nstr[j]];
                    continue;
                }
                //oppose
                for (int k=0; k<r.size(); k++) {
                    if (oppose[r[k]][nstr[j]] == 1) {
                        r="";
                        break;
                    }
                }
                if (r=="")continue;
            }
            r+=nstr[j];
        }
        cout << "Case #" << i+1 << ": [";
        for (int j=0; j<r.size(); j++) {
            cout << r[j];
            if (j!=r.size()-1)cout << ", ";
        }
        cout << "]" << endl;
    }
    return 0;
}
