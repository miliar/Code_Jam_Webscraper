#include <iostream>

using namespace std;

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        int N;
        cin >> N;
        int res = 0;
        int minx = 1000001;
        int sumx = 0;
        int xorx = 0;
        for(int i = 0; i < N ; i++){
            int c;
            cin >> c;
            if(c < minx){
                minx = c;
            }
            sumx += c;
            xorx ^= c;
        }
        cout << "Case #" << t << ": ";
        if(xorx == 0){
            cout << (sumx - minx);
        }else{
            cout << "NO";
        }
        cout << endl;
    }
}
