#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main(){
    int t = 0;
    int count = 1;
    cin >> t;
    while(t > 0){
        vector<pair<char, int> > moves;
        int n;
        cin >> n;

        int po = 1;
        int pb = 1;
        int total = 0;
        int moves_allowed_o = 0;
        int moves_allowed_b = 0;
        for(int i = 0; i < n; i++){
            char c;
            int j;
            cin >> c;
            cin >> j;
            if(c == 'O'){
                int m = po > j ? (po - j) + 1 : (j - po) + 1;
                if(m <= moves_allowed_o){
                    //moves_allowed_o -= m;
                    moves_allowed_o = 0;
                    total++;
                    moves_allowed_b++;
                }
                else{
                    total += m - moves_allowed_o;
                    moves_allowed_b += m - moves_allowed_o;
                    moves_allowed_o = 0;
                }
                po = j;
            }
            if(c == 'B'){
                int m = pb > j ? (pb - j) + 1 : (j - pb) + 1;
                if(m <= moves_allowed_b){
                    //moves_allowed_b -= m;
                    moves_allowed_b = 0;
                    total++;
                    moves_allowed_o++;
                }
                else{
                    total += m - moves_allowed_b;
                    moves_allowed_o += m - moves_allowed_b;
                    moves_allowed_b = 0;
                }
                pb = j;
            }
            //cout << "Move: " << c << " " << j << endl;
            //cout << "Total: " << total << endl;
        }

        cout << "Case #" << count << ": " << total << endl;

        count++;
        t--;
    }
}
