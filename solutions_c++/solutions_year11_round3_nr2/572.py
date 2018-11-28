#include<stdio.h>



int L, t, N, C;
int a[1010];
int P[1010][5];

int minimo(int a, int b){
    if(a>b) return b;
    else return a;
}

int funcao(int x, int passou){
    int m = t - passou;
    if(m<0) m=0; 
    int resp;
    if(2*x>=m)
        resp = m + (x-m/2);
    else
        resp = x*2;
   return resp;
}

int main(){
    int T;
    int g, i, k;
    scanf("%d ", &T);
    for(g=1; g<=T; g++){
        scanf("%d %d %d %d ", &L, &t, &N, &C);
        for(i=0; i<C; i++){
            scanf("%d ", &a[i]);
        }
        P[0][0]=a[0]*2;
        P[0][1]=funcao(a[0], 0);
        P[0][2]=P[0][1];

        for(i=1; i<N; i++){
            P[i][0]=P[i-1][0] + a[(i%C)]*2;
            P[i][1] = minimo(P[i-1][1] + a[(i%C)]*2, P[i-1][0]+funcao(a[(i%C)], P[i-1][0]));
            P[i][2] = minimo(P[i-1][2] + a[(i%C)]*2, P[i-1][1]+funcao(a[(i%C)], P[i-1][1]));
        }
        printf("Case #%d: ", g);
        printf("%d\n", P[N-1][L]);
        /*for(i=0; i<N; i++){
            for(k=0; k<3; k++)
                printf("%d ", P[i][k]);
            printf("\n");
        }*/
    }
    return 0;
}
