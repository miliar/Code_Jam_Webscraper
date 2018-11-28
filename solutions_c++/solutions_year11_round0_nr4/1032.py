#include <iostream>

using namespace std;

int main(){
    int t;
    cin >> t;

    for(int c = 0; c < t; c++){
        int n;
        cin >> n;

        int incorrect = 0;
        for(int i = 1; i <= n; i++){
            int j;
            cin >> j;
            if(i != j) incorrect++;
        }

        cout << "Case #" << c+1 << ": " << incorrect << ".000000" << endl;
    }
}
