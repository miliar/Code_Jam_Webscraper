#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

bool check(vector<int> &frecs, int num){
    for(int i = 0; i < frecs.size(); ++i){
        if(frecs[i] < num and num%frecs[i] != 0)
            return false;
        if(frecs[i] > num and frecs[i]%num != 0)
            return false;
    }
    return true;
}

int main(){
    int T, N, L, H;
    int c = 1;
    cin >> T;
    while(T--){
        cin >> N >> L >> H;
        vector<int> frecs(N);
        int tmp;
        for(int i = 0; i < N; ++i){
            cin >> tmp;
            frecs[i] = tmp;
        }
        bool found = false;
        int num = -1;
        for(int i = L; i <= H and !found; ++i){
            if(check(frecs,i)){
                found = true;
                num = i;
            }
        }
        printf("Case #%d: ", c++);
        if(found){
            cout << num << endl;
        }
        else{
            puts("NO");
        }
        
    }
    return 0;
}
