
#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int T, C;
    cin >> T;
    for(C = 1; C <= T; C++) {
        string number, onumber, res;
        cin >> number;
        onumber = number;
        int i = number.length()-1;

        int minj = -1;
        while( i >= 0 && minj == -1 ) {
            char hold = number[i];
            char min = '9'+1;
            for(int j = i+1; j < number.length(); j++) {
                char c = number[j];
                if( c > hold && c < min ) {
                    min = c;
                    minj = j;
                }
            }

            i--;
        }

        if( minj == -1 ) {
            number.push_back('0');

            char hold = '0';
            char min = '9'+1;
            for(int j = i+1; j < number.length(); j++) {
                char c = number[j];
                if( c > hold && c < min ) {
                    min = c;
                    minj = j;
                }
            }
        }

            i++;
            char hold = number[i];
            number[i] = number[minj];
            number[minj] = hold;

            for(int j = i+2; j < number.length(); j++) {
                int k = j-1;
                char jhold = number[j];
                while( k >= i+1 && number[k] > jhold) {
                    number[k+1] = number[k];
                    k--;
                }
                number[k+1] = jhold;
            }

        cout << "Case #" << C << ": " << number << endl;
    }

    return 0;
}

