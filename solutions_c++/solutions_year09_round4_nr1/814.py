#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <iomanip>
#include <algorithm>
#include <cmath>

using namespace std;

int go() {
    int N;
    cin >> N;
    vector<vector<int> > v(N, vector<int> (N));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            char c;
            cin >> c;
            v[i][j] = (c == '1');    
        }    
    }
    int iCnt = 0;
    int iDoing = 0;
    for (int iDoing = 0; iDoing < N; iDoing++) {
       int iMoveUp = -1;
       for (int i = iDoing; i < N && iMoveUp == -1; i++) {
           int iOnes = 0;
           for (int j = iDoing + 1; j < N; j++) {
               if (v[i][j]) {
                  iOnes = 1;
                  break;             
               }
           }
           if (iOnes == 0) {
               iMoveUp = i;
           }
       }
       if (iMoveUp != -1) {
           for (int i = iMoveUp; i > iDoing; i--) {
               swap(v[i], v[i-1]);
               iCnt++;
           }
       }
   }
    return iCnt; 
}

int main() {
    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cout << "Case #" << i + 1 << ": " << go() << std::endl;       
    }
}
