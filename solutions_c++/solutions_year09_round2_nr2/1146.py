#include <iostream>
#include <fstream>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <climits>
#include <cstring>

#define print(x) cout << #x" = " << x << endl

using namespace std;

string N;
int digits[30];

bool compare(char a, char b) {
    return a < b;
}

void solve() {
    int j = -1;
    
    for (int i = 0; i < N.size(); i++) {
        digits[i] = N[i] - '0';
    }
    
    for (int i = N.size() - 1; i > 0; i--) {
        if (digits[i] > digits[i - 1]) {
            j = i - 1;
            break;
        }
    }
    
    if (j == -1) {
        sort(digits, digits + N.size());        
        
        int k = 0;
        
        while (digits[k] == 0) {
            k++;
        }
        
        int temp = digits[0];
        digits[0] = digits[k];
        digits[k] = temp;
        
        cout << digits[0] << "0";        
        for (int i = 1; i < N.size(); i++) {
            cout << digits[i];
        }
        cout << endl;
        return;
    }
    
    
    sort(digits + j + 1, digits + N.size());

    int k = j + 1;

    while (digits[k] <= digits[j]) {
        k++;
    }

    int temp = digits[j];
    digits[j] = digits[k];
    digits[k] = temp;
    
    sort(digits + j + 1, digits + N.size());

    for (int i = 0; i < N.size(); i++) {
        cout << digits[i];
    }
    
    cout << endl;
}

int main(void) {
    int t = 1, n;
    
    cin >> n;
    
    while(n--) {
        cin >> N;
        cout << "Case #" << t++ << ": ";
        solve();
    }
    
    return 0;
}
