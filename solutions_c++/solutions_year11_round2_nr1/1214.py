#include <iostream>
#include <cstdio>

using namespace std;

int N;

const int maxN = 101;
char play[maxN][maxN];
float wps[maxN];
int gp[maxN];

float owps[maxN];
float oowps[maxN];
float res[maxN];

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        cin >> N;
        for(int i = 0; i < N; i++){
            wps[i]=0.0;
            gp[i] = 0;
            for(int j = 0; j < N; j++){
                char c;
                cin >> c;
                play[i][j] = c;
                if(c == '1'){
                    wps[i]++;
                }
                if(c != '.'){
                    gp[i]++;
                }
//                cout << "C " << c << endl;
            }
            wps[i] /= gp[i];
        }
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
//                cout << play[i][j] <<" ";
            }
//            cout << endl;
        }
        for(int i = 0; i < N; i++){
//            cout << i << " " << wps[i] << endl;
        }
        for(int i = 0; i < N; i++){
            owps[i] = 0.0;
            int n = 0;
            for(int j = 0; j < N; j++){
                if(play[i][j] != '.'){ // opponent
                    float thr = 0.0;
                    int gp = 0;
                    for(int k = 0; k < N; k++){
                            if(k != i){
                                if(play[j][k] == '1'){
                                    thr++;
                                }
                                if(play[j][k] != '.'){
                                    gp++;
                                }
                            }
                    }
                    thr /= gp;
                    owps[i] += thr;
                    n++;
                }
            }
            owps[i] /= n;
        }
        for(int i = 0; i < N; i++){
//            cout << i << " " << owps[i] << endl;
        }
        for(int i = 0; i < N; i++){
            oowps[i] = 0.0;
            int n = 0;
            for(int j = 0; j < N; j++){
                if(play[i][j] != '.'){ // opponent
                    oowps[i] += owps[j];
                    n++;
                }
            }
            oowps[i] /= n;
        }
        for(int i = 0; i < N; i++){
//            cout << i << " " << oowps[i] << endl;
        }
        for(int i = 0; i < N; i++){
            res[i] = 0.25 * wps[i] + 0.50 * owps[i] + 0.25 * oowps[i];
        }
        cout << "Case #" << t << ":" << endl;
        for(int i = 0; i <N; i++){
            printf("%.10f\n", res[i]);
        }
    }
}
