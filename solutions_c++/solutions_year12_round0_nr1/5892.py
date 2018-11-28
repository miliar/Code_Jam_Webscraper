#include <string>
#include <cstring>
#include <cstdio>
#include <iostream>
#include <map>
using namespace std;

int main() {
    freopen("in", "r", stdin);
    string mmm = "yhesocvxduiglbkrztnwjpfmaq";
    int N, cou, nnn, i=0;
    cin >> N;
    string s;
    char innn[128];
    getchar();
//    cout << mmm << endl;
    while(N){
        cin.getline(innn, 128);
        s=innn;
//        cout << s << endl;
        cout << "Case #" << ++i << ": "  ;
        cou = s.size();
        for(int iiii=0;iiii<cou;iiii++)cout << ((s[iiii]==' ') ? ' ': mmm[s[iiii]-'a']);
        cout << endl;
        N--;
    }
    return 0;
}
