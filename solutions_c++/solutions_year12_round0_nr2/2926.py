#include <iostream>

using namespace std;


int arredondamento(double num) {
    int numInt = num;
    if( (num - numInt) >= 0.5){
        numInt++;
        return numInt;
    }else{
        return numInt;
    }
}

int main(){
    long long T,N,S,p, cont,media;
    cin >> T;
    for(int i = 1; i <= T; i++){
        cin >> N;
        cin >> S;
        cin >> p;
        int t[100], maxNotasPossi[2][100];
        cont = 0;
        for(int j = 0; j < N; j++){
            cin >> t[j];
            //Maiores notas possíveis
            media = arredondamento((double)t[j]/3);
            if((t[j] <= 1)||(t[j] >= 29)){
                if(t[j] <= 1){
                    maxNotasPossi[0][j] = t[j];
                    maxNotasPossi[1][j] = t[j];
                }else{
                    maxNotasPossi[0][j] = media;
                    maxNotasPossi[1][j] = media;
                }
            }else{
                if(t[j] % 3 == 1){
                    maxNotasPossi[0][j] = media+1;
                    maxNotasPossi[1][j] = media+1;
                }else{
                    maxNotasPossi[0][j] = media;
                    maxNotasPossi[1][j] = media+1;
                }
            }
            if(maxNotasPossi[0][j] != maxNotasPossi[1][j]){
                if(maxNotasPossi[0][j] >= p){
                    cont++;
                }else{
                    if(maxNotasPossi[1][j] >= p && S > 0){
                        cont++;
                        S--;
                    }
                }
            }else{
               if(maxNotasPossi[0][j] >= p){
                    cont++;
                }
            }
        }
        cout << "Case #" << i << ": " << cont << endl;
    }
}
