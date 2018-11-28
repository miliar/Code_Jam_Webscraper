#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){
    int TC;
    cin >> TC;
    vector<int> chickens;
    vector<int> speeds;
    vector<int> place;
    vector<int> ok;
    for(int ii = 1; ii <= TC; ++ii){
        int N, K, B, T;
        cin >> N >> K >> B >> T;
        chickens = vector<int>(N);
        speeds = vector<int>(N);
        place = vector<int>(N);
        ok = vector<int>(N);

        for(int i = 0; i < N; ++i){
            cin >> chickens[i];
        }
        for(int i = 0; i < N; ++i){
            cin >> speeds[i];
        }
        int swaps = 0;
        int count = 0;
        for(int i = N-1; i >= 0; --i){
            place[i] = chickens[i] + T*speeds[i];
            if(place[i] >= B){
                count++;
                if(i < N-1) ok[i] = ok[i+1]+1;
                else ok[i] = 1;
                for(int j = N-1; j > i; --j){
                    if(place[j] < B) swaps++;
                }
            }
            else{
                if(i < N-1) ok[i] = ok[i+1];
                else ok[i] = 0;
            }
            if(count == K) break;
        }
        if(count == K){
            cout << "Case #" << ii << ": " << swaps << endl;
        }
        else{
            cout << "Case #" << ii << ": IMPOSSIBLE" << endl;
        }

    }
    return 0;
}
