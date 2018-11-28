#include <iostream>
#include <string>
using namespace std;

char pre(char x) {
    if (x=='a') return 'y';
    if (x=='b') return 'h';
    if (x=='c') return 'e';
    if (x=='d') return 's';
    if (x=='e') return 'o';
    if (x=='f') return 'c';
    if (x=='g') return 'v';
    if (x=='h') return 'x';
    if (x=='i') return 'd';
    if (x=='j') return 'u';
    if (x=='k') return 'i';
    if (x=='l') return 'g';
    if (x=='m') return 'l';
    if (x=='n') return 'b';
    if (x=='o') return 'k';
    if (x=='p') return 'r';
    if (x=='q') return 'z';
    if (x=='r') return 't';
    if (x=='s') return 'n';
    if (x=='t') return 'w';
    if (x=='u') return 'j';
    if (x=='v') return 'p';
    if (x=='w') return 'f';
    if (x=='x') return 'm';
    if (x=='y') return 'a';
    if (x=='z') return 'q';
}

int main() {
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t=0;
    cin >> t;
    cin.ignore(256,'\n');
    for (int i=0; i<t; i++) {
        string st;
        string ans("");
        getline(cin,st);
        for (int j=0; j<st.size(); j++) {
            if (st[j]==' ') ans+=' ';
            else ans+=pre(st[j]);
        }
        cout << "Case #" << i+1 << ": " << ans << endl;
    }
    return 0;
}
