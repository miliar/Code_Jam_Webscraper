#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

#define cin fin

int main()
{
    ifstream fin("test");

    int T, N, S, p; // num of test cases
    cin >> T;
    for(int testCase=0; testCase<T; ++testCase){ // test cases
        int y = 0;
        cin >> N >> S >> p;
        for(int i = 0; i < N; ++i){
            int t;
            cin >> t;
            if((t+2) / 3 >= p){
                ++y;
            } else
                if(S>0 && t && (t+4)/3 >= p ){
                    --S;
                    ++y;
                }
        }
        cout << "Case #" << testCase+1 << ": " << y << endl;
    }

    return 0;
}

