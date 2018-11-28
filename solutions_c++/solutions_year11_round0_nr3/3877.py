#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

string makebin(int n) {
    char s[65];
    s[64] = 0;
    int i = 63;
    while(0 < n) {
        s[i--] = (n&1) ? '1' : '0';
        n>>=1;
    }
    return string(s+i+1, 63-i);
}

int makeint(string b) {
    int result = 0;
    for(int i = 0 ; i < b.length() ; i++ ){
        result <<= 1;
        result += b[i] == '1' ? 1 : 0;
    }
    return result;
}

string patrick_add_bin(string a, string b) {
    char s[65];
    s[64] = 0;
    int i = 0;
    for(; i < int(a.length()) || i < int(b.length()) ; i++) {
        int ac = 0;
        if( i < int(a.length()) ) {
            ac = a[a.length() - 1 - i] == '1' ? 1 : 0;
        }
        int bc = 0;
        if( i < int(b.length()) ) {
            bc = b[b.length() - 1 - i] == '1' ? 1 : 0;
        }
        int k = (ac + bc) & 1;
        
        s[63-i] = k ? '1' : '0';
    }
    return string(s+64-i, i);
}

int patrick_add(int a, int b) {
    return makeint(patrick_add_bin(makebin(a),makebin(b)));
}

template <class It>
int foo(int sean_real, int sean_patrick, int patrick, It b, It e) {
    //cerr << "foo: sean_real = " << sean_real << ", sean_patrick = " << sean_patrick << ", patrick = " << patrick << ", remain = " << (e - b) << endl;
    if( b == e ) {
        if( patrick != 0 && sean_patrick == patrick ) { return sean_real; }
        return 0;
    }
    int k0 = foo(sean_real + *b, patrick_add(sean_patrick, *b), patrick, b+1, e);
    int k1 = foo(sean_real, sean_patrick, patrick_add(patrick, *b), b+1, e);
    if(k0 > k1) { return k0; }
    return k1;
}

int main(int argc, char *argv[]) {
#if 0
    cout << makebin(3) << ", " << makeint( makebin(3)) << endl;
    cout << makebin(4) << ", " << makeint( makebin(4)) << endl;
    cout << makebin(7) << ", " << makeint( makebin(7)) << endl;
    cout << makebin(16) << ", " << makeint( makebin(16)) << endl;
    cout << patrick(5, 6) << endl;
#else
    int T;
    cin >> T;
    for (int i = 0 ; i < T ; ++i) {
        int N;
        cin >> N; 
        vector<int> data;
        for (int j = 0 ; j < N ; ++j) {
            int C;
            cin >> C;
            data.push_back(C);
        }
        int k = foo(0, 0, 0, data.begin(), data.end());
        cout << "Case #" << (i+1) << ": ";
        if( k == 0 ) { cout << "NO"; } else { cout << k; }
        cout << endl;
    }
    
#endif
    return 0;
}


