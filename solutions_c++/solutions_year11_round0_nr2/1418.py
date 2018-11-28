#include <stdio.h>
#include <iostream>
#include <string>


using namespace std;

int ntest, lntest, combine[256][256], oppose[256][256], c, d, n;
string s;

void open_file() {
    freopen("B-large.in", "r",stdin);
    freopen("B.outs", "w", stdout);    
}

void process(string &s, int &n) {
    string s2 = "";
    int d = 0;
    for (int i = 0; i < n; i++) {
        if (!d) {
            s2 = s2 + s[i];
            d = 1;
            continue;   
        }
        if (combine[s2[d - 1]][s[i]] > 0) {
            s2[d - 1] = combine[s2[d - 1]][s[i]];
            continue;
        }
        for (int j = 0; j < d; j++) 
            if (oppose[s2[j]][s[i]]) {
                s2 = "";
                d = 0;       
                continue;         
            }
        if (d) {
            d++;
            s2 = s2 + s[i];   
        }
    }    
    s = s2;
    n = d;
}

void output(string s, int n) {
    cout << "Case #" << lntest - ntest << ": ";
    cout << '[';
    if (n) {
        cout << s[0];
        for (int i = 1; i <n; i++) cout << ", " << s[i];
    }
    cout << ']';    
    cout << endl;
}

int main () {
    open_file();
    cin >> ntest;
    lntest = ntest;
    while (ntest--) {
        cin >> c;
        
        memset(combine, 0, sizeof(combine));
        memset(oppose, 0, sizeof(oppose));  
              
        for (int i = 0; i < c; i++) {
            cin >> s;
            combine[s[0]][s[1]] = s[2];
            combine[s[1]][s[0]] = s[2];            
        }
        
        cin >> d;
        for (int i = 0; i < d; i++) {
            cin >> s;
            oppose[s[0]][s[1]] = 1;
            oppose[s[1]][s[0]] = 1;                        
        }        
        
        cin >> n >> s;
        process(s, n);
        output(s, n);
    }
    return 0;   
}
