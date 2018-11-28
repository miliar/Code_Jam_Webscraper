#include <iostream>
#include <math.h>
using namespace std;

int main(){
    int T, N, num, time;
    char color;
    int c = 1;
    cin >> T;
    int blue, orange, acumblue, acumorange;
    while(T--){
        cin >> N;
        blue = orange = 1;
        acumblue = acumorange = 0;
        time = 0;
        for(int i = 0; i < N; ++i){
            cin >> color;
            cin >> num;
            int tmp = 0;
            if(color == 'O'){
                tmp = abs(orange - num) - acumblue;
                time += (tmp > 0)?tmp + 1 : 1;
                orange = num;
                acumorange += (tmp > 0)?tmp + 1 : 1;
                acumblue = 0;
            }
            else{
                tmp = abs(blue - num) - acumorange;
                time += (tmp > 0)?tmp + 1 : 1;
                blue = num;
                acumorange = 0;
                acumblue += (tmp > 0)?tmp + 1 : 1;
            }
        }
        cout << "Case #" << c++ << ": " << time << endl;
    }
}
