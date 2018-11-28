#include <iostream>
#include <vector>

using namespace std;

int main(){
    int T;
    cin >> T;
    for(int tc = 0; tc < T; tc++){
         int N;
         cin >> N;
         
         int sol = 0;
         int acum = 0;
         char racum = '*';
         int pos[2];
         pos[0] = pos[1] = 1;
         for(int i=0;i<N;i++){
                 char R;
                 int P;
                 cin >> R >> P;
                 if(racum == '*') racum = (R=='O')?'B':'O';
                 if(R == racum){
                      acum = max(0, abs(P - pos[(R=='O')?0:1]) - acum) + 1;
                      sol += acum;
                      pos[(R=='O')?0:1] = P;
                      racum = (R=='O')?'B':'O';
                 }
                 else {
                      int T = abs(P - pos[(R=='O')?0:1]) + 1;
                      acum += T;
                      sol += T;
                      pos[(R=='O')?0:1] = P;
                 }
         }
         cout << "Case #" << tc+1 << ": " << sol << endl;
    }
}
