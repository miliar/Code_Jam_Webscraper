#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T; //test case
    int N; //number of googler
    int S; //number of surprise
    int P; //best result of at least p
    int score[105];
    cin >> T;
    for (int i = 1; i <= T; i++){
        cin >> N >> S >> P;
        int result = 0;
        for (int j = 1; j <= N; j++){
            cin >> score[j];
            //exception
            if(P > score[j]){
                continue;
            }

            //not surprise
            if ((score[j]+2) / 3 >= P){
                result++;
                continue;
            }else{
                //surprise
                if (S>0 && (score[j]+4) / 3 >= P){
                    result++;
                    S--;
                    continue;
                }
            }
        }
        cout << "Case #" << i << ": " << result << endl;
    }


    return 0;
}
