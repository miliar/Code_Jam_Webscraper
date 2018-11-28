#include<iostream>
using namespace std;

//18 % 3 = 0
//    => / 3 + 1 [ surprising ]
//    => / 3
//    6 6 6
//    5 6 7      [ surprising ]
//
//19 % 3 = 1
//    => / 3 + 1
//    6 6 7
//    5 7 7      [ surprising ]
//    
//20 % 3 = 2
//    => / 3 + 2 [ surprising ]
//    => / 3 + 1
//    6 7 7
//    6 6 8      [ surprising ]

int main() {
    int n;
    cin >> n;
    for (int k=1;k<=n;k++) {
        int T, S, P, resp = 0;
        cin >> T >> S >> P;
        for (int l=0;l<T;l++) {
            int num, score;
            cin >> num;
            if (num % 3 == 1)
               score = (num / 3) + 1;
            else
            if (num % 3 == 2) {
               score = (num / 3) + 1;
               if (S && score == P -1)
                  score++, S--;        
            }
            else {
               score = (num / 3); 
               if (S && score == P - 1 && num > 2)
                  score++, S--;
            }
            //cout << num << " " << score << endl;
            resp += (score >= P);
        }
        cout << "Case #" << k << ": " << resp << endl;
    }
    return 0;
}
