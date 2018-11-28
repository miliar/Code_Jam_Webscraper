#include <iostream>
#include <stdio.h>

using namespace std;

int main() {
    freopen("in.txt" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    int t,n,s,p;
    cin >> t;
    for(int i = 1; i<= t; i++) {
        cin >> n >> s >> p;
        int res = 0;
        int temp,num,mod;
        for(int j = 0; j < n; j++) {
            cin >> num;
            if( num == 0 ) {
                if ( p == 0 ) {
                    res ++;
                }
                continue;
            }
            temp = num / 3;
            mod = num % 3;
            if(temp >= p) {
                res++;
            } else {
                if(temp == p - 1) {
                    if( mod >=  1 ) {
                        res++; 
                    } else if ( mod == 0 ) {
                        if( s > 0 ) {
                            res++;
                            s--;
                        }
                    }
                } else if(temp == p - 2)  {
                    if( mod >= 2) {
                        if(s > 0) {
                            res++;
                            s--;
                        }
                    } 
                }
            }
        }
        cout << "Case #" << i << ": " << res << endl;
    }

    return 0;
}
