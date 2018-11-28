#include <iostream>
using namespace std;

int main() {
    int t,n,h,l;
    int tab[10005];
    cin >> t;
    for(int w=1; w<=t; w++) {
        cin >> n >> l >> h;
        for(int i=0; i<n; i++)
            cin >> tab[i];


        int val = -1;
        bool  flag = false;

        for(int i=l; i<=h && !flag ; i++) {
            flag = true;
            for(int j=0; j<n && flag; j++) {
                if( tab[j]%i != 0 && i%tab[j] != 0)  {
                    flag = false;
                }
            }
            if(flag) {
                val = i;
            }
        }

        cout << "Case #" << w << ": ";
        if( val == -1 ) cout << "NO\n";
        else cout << val << "\n";

    }
}
