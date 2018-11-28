#include <cstdio>
#include <iostream>
#include <cmath>
#define MAXN 1001
using namespace std;

long long int T, l,p,c,g,tr,r;

int main(){
    cin >> T;
    for (int t = 1; t <= T; t++){
        cin >> l >> p >> c;
//        cout << l << " " << p << " " << c << endl;
        tr = l;
        g = 0;
        while (tr*c < p){
            g++;
            tr*=c;
        }
        r = 0;
        while (g != 0){
            g = (int)ceil((double)(g-1)/2.0);
            r++;
//            cout << g << endl;
        }
        cout << "Case #" << t << ": " << r << endl;
    }

    return 0;
}
