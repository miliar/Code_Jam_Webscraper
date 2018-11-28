
#include<iostream>
#include<string>
#include<cmath>

using namespace std;

int main(){


    int T, K, N;

    cin >> T;

    string y = "";

    for(int i = 0; i < T; ++i){
        cin >> N >> K;

        if((K+1) %( (1 << N)) == 0){
            y = "ON";
        }
        else y = "OFF";

        cout << "Case #" << i+1 << ": " << y << endl;


    }


    return 0;
}


