#include <string>
#include <iostream>
using namespace std;

/**
 * 0: above: yes
 
 * 1: above: if strange
 
 * 2: above: no
 */

int categorize (int score, int p){
    //if (score >= 29) return 0;
    if (score >= 3*p -2) return 0;
    if (score >= 3*p -4) return 1;
    //if (score >= 2) return 2;
    return 2;
}

int main (){
    int categories[5];
    int T, S, p, N;
    int temp;
    cin >> T;
    for (int i = 1; i<=T; i++) {
        categories[0]=categories[1]=categories[2]
            =categories[3]=categories[4]=0;
        cin >> N >> S >> p;
        if (p==0) {
            string st;
            getline(cin, st);
            cout << "Case #" << i << ": " << N << '\n'; 
        }
        else if (p==1) {
            int count = 0;
            for (int j = 0; j<N; j++){
                cin >> temp;
                if (temp>=1) count++;     
            }
            cout << "Case #" << i << ": " << count << '\n';
        }
        else {
            for (int j = 0; j<N; j++){
                cin >> temp;
                categories[categorize(temp, p)]++;
            }
            cout << "Case #" << i << ": " 
                 << (categories[0] + min(categories[1], S) ) << '\n'; 
        }
    }
}
