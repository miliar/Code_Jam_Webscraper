#include <iostream>
#include <string>
using namespace std;
char fx[26]= {'y'
,'h'
,'e'
,'s'
,'o'
,'c'
,'v'
,'x'
,'d'
,'u'
,'i'
,'g'
,'l'
,'b'
,'k'
,'r'
,'z'
,'t'
,'n'
,'w'
,'j'
,'p'
,'f'
,'m'
,'a'
,'q' };
void loop(int na) {
     string a;
     getline (cin, a);     
     for (int i=0; unsigned(i)<a.size(); i++) {
         if (char(a[i])-'a' >= 0 &&  char(a[i])-'a' <26)
            a[i] = fx[char(a[i])-'a'];
     }
     cout << "Case #" << na << ": " << a << endl;
     return;
}


int main() {
    string tmpin;
    int N;
    cin >> N;
    getline (cin, tmpin);
    for (int i=0; i<N; i++) loop(i+1);
    return 0;
}
