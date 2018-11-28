#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

#define TAM 1123123

long long int temps[TAM];
long long int a[TAM];
long long int t2[TAM];

int main(){
    long long int L,t,N,C;
    FILE *fin = fopen("B-large.in","r");
    FILE *fout = fopen("B.out","w");
    int nt;
    fscanf(fin,"%d",&nt);
    for(int tt = 1 ; tt <= nt ; tt++){
        fscanf(fin,"%lld %lld %lld %lld",&L,&t,&N,&C);
        for(int i = 0 ; i < C ; i++){
            fscanf(fin,"%lld",&a[i]);
        }
        for(int k = 0; k < N;k++){
            temps[k] = 2*a[k%C];
        }

        long long int ans = 0;
        int k = N;
        for(int i = 0 ; i < N ; i ++){
            if(ans + temps[i] > t){
                temps[i] = temps[i] - (t - ans);
                ans  += t - ans;
                k = i;
                break;

            }
            else ans+= temps[i];
        }
        for(int i = k ;i < N ; i++){
            t2[i-k] = temps[i];
        }
        sort(t2,t2+N-k);

        for(int i = N - k - 1,j = 0; i >= 0 ; i--,j++){

            if(j < L) ans += t2[i] * 0.5;
            else ans += t2[i];
        }

        fprintf(fout,"Case #%d: %lld\n",tt,ans);
    }

    return 0;

}
