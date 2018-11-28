#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream fin("file.in");
    if(!fin) {
        return -1;
    }
    ofstream fout("file.out");
    cout << endl;
    int l, d, n;
    fin >> l >> d >> n;
    string s[d], t;
    for(int i=0; i<d; i++) {
        fin >> s[i];
    }
    for(int i=0; i<n; i++) {
        fin >> t;
        int o=0;
        for(int j=0; j<d; j++) {
            bool par=false;
            int a=0, c=0;
            for(int m=0; m<t.length(); m++) {
                if(t[m]=='(')
                    par = true;
                if(t[m]==')')
                    par = false;
                if(t[m]==s[j][a])
                    c++;
                if(!par)
                    a++;
            }
            if(c==l)
                o++;
        }
        fout << "Case #" << i+1 << ": " << o << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
