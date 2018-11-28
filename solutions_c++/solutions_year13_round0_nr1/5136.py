#include <iostream>
#include <string>
using namespace std;

char a[16];

bool z(int p, char x) {
    return (a[p]==x) || (a[p]=='T');
}

bool y(int p, int q, char x) {
    for(int i=p;i<p+4*q;i+=q)
        if (!z(i,x)) return false;
    return true;
}

bool won(char x) {
    for(int i=0;i<4;i++) if (y(i,4,x)) return true;
    for(int i=0;i<16;i+=4) if (y(i,1,x)) return true;
    if (y(0,5,x)) return true;
    if (y(3,3,x)) return true;
    return false;
}

bool full() {
    for(int i=0;i<16;i++) if (a[i]=='.') return false;
    return true;
}
    

int main() {
    int TT;
    cin>>TT;
    for(int T=1;T<=TT;T++) {
        for(int i=0;i<16;i++) cin>>a[i];
        cout<<"Case #"<<T<<": ";
        if (won('X')) cout<<"X won";
        else if (won('O')) cout<<"O won";
        else if (full()) cout<<"Draw";
        else cout<<"Game has not completed";
        cout<<endl;
    }
    return 0;
}