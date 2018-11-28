#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

const int MAXP  =   11;

int T[MAXP][1<<MAXP];
long long f[MAXP+1][1<<MAXP][MAXP+1];
int M[1<<MAXP];
int P;

void init(){
    scanf("%d", &P);
    for(int i=0; i<(1<<P); ++i)
        scanf("%d", &M[i]);
    for(int i=P-1; i>=0; --i){
        for(int j=0; j<(1<<(i)); ++j)
            scanf("%d", &T[P - i][j]);
    }
    /*
    for(int i=0; i<(1<<P); ++i)
        printf("%d ", M[i]);
    printf("\n");
    
    for(int i=1; i<=P; ++i){
        for(int j=0; j<(1<<(P-i)); ++j)
            printf("%d ", T[i][j]);
        printf("\n");
    }
    */
}

long long solve(){
    memset(f, -1, sizeof(f));
    for(int i=0; i<1<<P; ++i){
        for(int j=P-M[i]; j<=P; ++j)
            f[0][i][j] = 0;
    }
    for(int i=1; i<=P; ++i){
        for(int j=0; j<(1<<(P-i)); ++j){
            for(int k=0; k<=P-i; ++k){
                f[i][j][k] = -1; 
                //printf("f[%d][%d][%d] = %d\n", i,j,k,f[i][j][k]);
                if(f[i-1][j+j][k] >= 0 && f[i-1][j+j+1][k] >=0 && (f[i][j][k] < 0 || f[i-1][j+j][k] + f[i-1][j+j+1][k] < f[i][j][k]))
                     f[i][j][k] = f[i-1][j+j][k] + f[i-1][j+j+1][k];
                if(f[i-1][j+j][k+1] >= 0 && f[i-1][j+j+1][k+1] >=0 &&
                   (f[i][j][k] < 0 || f[i-1][j+j][k+1] + f[i-1][j+j+1][k+1] + T[i][j] < f[i][j][k]))
                    f[i][j][k] = f[i-1][j+j][k+1] + f[i-1][j+j+1][k+1] + T[i][j];
                if(k && f[i][j][k-1] >= 0 && (f[i][j][k] < 0 || f[i][j][k-1] < f[i][j][k]))
                    f[i][j][k] = f[i][j][k-1];
                //printf("f[%d][%d][%d] = %d\n", i,j,k,f[i][j][k]);
            }
        }
    }
    return f[P][0][0];
}

int main(){
    int t;
    scanf("%d", &t);
    for(int i=1; i<=t; ++i){
        init();
        cout<<"Case #"<<i<<": "<<solve()<<endl;
    }
}
