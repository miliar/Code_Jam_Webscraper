#include <cstdio>

using namespace std;

int d[1100],L,t,N,C;
bool booster[1100];

int probaj(){
    int sol = 0;
    for(int i = 0; i < N; ++i){
        if( booster[i] == true ){
            
            if( sol >= t ){
                // izgradio se vec
                sol += d[i%C];
            }else{
                // izgradit ce se u putovanju
                int razlika = t - sol;
                int temp = razlika / 2; // koliko ce prijeci u tom sporom vremenu
                if( temp < d[i%C] ){
                    // ovoliko ce prijeci u sporom vremenu
                    sol += razlika;
                    // a ovoliko brzo
                    sol += (d[i%C] - temp);
                }else{
                    // nece se stici izgraditi, putuje sporo
                    sol += 2 * d[i%C];
                }
            }
        }else{
            // nema boostera
            sol += 2 * d[i%C];
        }
    }
    return sol;
}


int main(){
    int testovi;
    scanf("%d",&testovi);
    for(int test = 0; test < testovi; ++test){
        fprintf(stderr, "%d\n",test+1);
        scanf("%d %d %d %d",&L,&t,&N,&C);
        for(int i = 0;i < C; ++i){
            scanf("%d",&d[i]);
        }

        int sol = 2000000000;

        if( L == 1 ){
            for(int i = 0;i < N; ++i){
                booster[i] = true;
                int k = probaj();
                if( k < sol ) sol = k;
                booster[i] = false;
            }
            // stavi svugdje booster i probaj
        }else if(L == 2){
            for(int i = 0; i < N-1; ++i){
                booster[i] = true;
                for(int j = i+1; j < N; ++j){
                    booster[j] = true;
                    int k = probaj();
                    if( k < sol ) sol = k;
                    booster[j] = false;
                }
                booster[i] = false;
            }
            // stavi svugdje booster i probaj
        }else{
            sol = probaj();
            // samo probaj
        }
        printf("Case #%d: %d\n",test+1,sol);
    }
    return 0;
}
