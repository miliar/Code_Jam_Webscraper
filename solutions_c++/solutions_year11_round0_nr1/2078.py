#include <iostream>
using namespace std;
#define MAX 1000
int test, size, but[2][MAX], BTime = 0, OTime = 0, BPos = 1, OPos = 1;

int computeB(int j) {
    BTime += abs(but[0][j] - BPos) + 1;
    if(BTime <= OTime) {
        BTime = OTime+1;
    }
    BPos = but[0][j];
}

int computeO(int j) {
    OTime += abs(but[1][j] - OPos) + 1;
    if(OTime <= BTime) {
        OTime = BTime+1;
    }
    OPos = but[1][j];
}

int main() {
    cin >> test;
    
    for(int i = 1; i <= test; ++i) {
        cin >> size;
        BTime = 0;
        OTime = 0;
        BPos = 1;
        OPos = 1;
        for(int j = 1; j <= size; ++j) {
            char c;
            cin >> c;
            if(c == 'B') {
                cin >> but[0][j];
                //cout << c << " " << but[0][j] << endl;
                computeB(j);
                //cout << "B " << BTime << " " << BPos << endl;
            }
            else {
                cin >> but[1][j];
                //cout << c << " " << but[1][j] << endl;
                computeO(j);
                //cout << "O " << OTime << " " << OPos << endl;
            }
        }
        
        cout << "Case #" << i << ": " << max(OTime, BTime) << endl;
    }
}
