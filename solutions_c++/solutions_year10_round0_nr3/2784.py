
#include<iostream>
#include<vector>
#include<queue>


using namespace std;

int main(){


    int T, R, k, N, g;

    cin >> T;

    for(int i = 0; i < T; ++i){
        
        cin >> R >> k >> N;
        
        int sum = 0;
        queue<int> groups;
        for(int j = 0; j < N; ++j){
            cin >> g;
            groups.push(g);
        }
    
        int cap, num;
        for(int rounds = 0; rounds < R; ++rounds){
            cap = 0; num = 0;
            g = groups.front();
//            cout << "g = " << g << endl;
            while(cap + g <= k && num < groups.size()){
                cap += g; sum += g;
                groups.pop();
                groups.push(g);
                ++num;
                g = groups.front();
            }
//            cout << "Runde " << rounds << ": " << sum << endl;
        }

        cout << "Case #" << i+1 << ": " << sum << endl;




    }




    return 0;
}



