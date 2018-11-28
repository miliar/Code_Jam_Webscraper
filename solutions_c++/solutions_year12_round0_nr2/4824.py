#include<iostream>

using namespace std;

int main(){
    int T, N, S, max, r = 0, tsc, sc = 0;
    cin >> T;
    for (int i = 1; i <= T ; i++){
        r = 0;
        cin >> N >> S >> max;
        
        for(int j = 0 ; j < N ; j++){
            sc = 0;
            cin >> tsc;
            switch(tsc){
                case 0:
                    sc = 0; break;
                case 1: case 2: case 3:
                    sc = 1;  break;
                case 4: case 5: case 6:
                    sc = 2;  break;
                case 7: case 8: case 9:
                    sc = 3;  break;
                case 10: case 11: case 12:
                    sc = 4;  break;
                case 13: case 14: case 15:
                    sc = 5;  break;
                case 16: case 17: case 18:
                    sc = 6;  break;
                case 19: case 20: case 21:
                    sc = 7;  break;
                case 22: case 23: case 24:
                    sc = 8;  break;
                case 25: case 26: case 27:
                    sc = 9;  break;
                case 28: case 29: case 30:
                    sc = 10;  break;
            }
            if (sc >= max){
                r++;
            }else if(S > 0 && tsc != 0 && (tsc%3)!=1 && (sc+1) >= max){
                --S;
                r++;
            }
        }
        cout<<"Case #"<<i<<": "<<r<<"\n";
    }
    return 0;
}
