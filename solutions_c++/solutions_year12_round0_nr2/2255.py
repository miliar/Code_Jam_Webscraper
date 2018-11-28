#include <iostream>
#include <vector>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int cas = 1; cas <= t; ++cas) {
        int n, s, p; cin >> n >> s >> p;
        int ans = 0; //arriben a p
        int mans = 0;//si fossin "surprising" podrien arribar a p
        for (int i = 0;i < n;++i) {
            int x; cin >> x;
            if (int(x/3+(x%3>=1)) >= p) ++ans; //el tercer es el maxim
            else if (int(x/3+(x%3==2)) >= p-1 and x > 1) ++mans; //el tercer es el maxim
            
//            cerr << x/3 << " " << int(x/3+(x%3==2))  << " " << int(x/3 + (x%3>=1)) << endl;
        }
//        cerr << "ans = " << ans << ", " << "mans = " << mans << endl;
        cout << "Case #" << cas << ": " << ans+min(mans,s) << endl;
    }
}

/*
6 2 8
29 20 8 18 18 21
*/
