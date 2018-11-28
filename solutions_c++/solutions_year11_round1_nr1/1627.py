#include <iostream>

using namespace std;

int main(){
    int t;
    cin >> t;
    for(int c = 0; c < t;c++){
        int n, pd, pg;
        cin >> n >> pd >> pg;

        bool possible = false;

        int d = 0;
        int i = 0;
        for(i = 1; i <= 100; i++){
            d = pd*i;
            if(d % 100 == 0) {
                possible = true;
                break;
            }
        }
        
        int g;
        int j;
        if(i <= n && i < 101){
            for(j = i; j <= 100*i; j++){
                g = pg*j;
                if(g % 100 == 0) {
                    int lostd = i - (pd*i)/100;
                    int lostg = j - (pg*j)/100;

                    int wind = (pd*i)/100;
                    int wing = (pg*j)/100;

                    if(lostd > lostg) {
                        possible = false;
                        continue;
                    }
                    if(wind > wing) {
                        possible = false;
                        continue;
                    }
                    
                    possible = true;
                    break;
                }
                possible = false;
            }
        }
        else possible = false;

        //cout << "d = " << i << "    g = " << j << endl;

        cout << "Case #" << c+1 << ": ";
        if(possible) cout << "Possible" << endl;
        else cout << "Broken" << endl;
    }
}
