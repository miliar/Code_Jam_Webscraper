#include <iostream>
#include <vector>
#include <string>

using namespace std;

#define SIZEA 26
#define MAXL 20
#define MAXD 5010

bool Pat[MAXL][SIZEA];

int L, D, N;
string s[MAXD];

void parsePattern(string p) {
    bool par=false;
    int j=0;
    memset(Pat,0,sizeof(Pat));
     for (int i=0; i<p.length(); ++i) {                        
         if (p[i]=='(') {
                par=true;                
            }
         else if (p[i]==')') {
                par=false;
                ++j;
         } else {
                Pat[j][p[i]-'a']=true;                
                if (!par) {
                    ++j;
                } 
         }
     }
}

bool verify(string s) {
    for (int i=0; i<s.length(); ++i) {
        if (!Pat[i][s[i]-'a']) return false;
    }
    return true;
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int test=0;
    cin >> L >> D >> N;
    for (int i=0; i<D; ++i)
        cin >> s[i];
    
    for (int i=0; i<N; ++i) {
        ++test;
        string p;
        cin >> p;
        
        parsePattern(p);
        
        int cnt=0;
        for (int j=0; j<D; ++j) 
            if (verify(s[j])) ++cnt;
            
        cout << "Case #" << test << ": " << cnt << endl;
    }
    
    return 0;
}
