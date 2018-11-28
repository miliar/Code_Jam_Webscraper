#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int T, dig, diez[] = {1,10,100,1000,10000,100000,1000000,10000000}, j, tam;
    long int A, B, C, resp, nuevos[10];
    scanf("%d\n",&T);
    for (int t=1 ; t<=T ; t++) {
        scanf("%ld %ld\n", &A, &B);
        resp = 0;
        while (A<B) {
            dig = floor(log10(abs(A)))+1;
            tam = 0;
            for (int i=1 ; i<=dig ; i++) {
                C = (A % diez[i])*diez[dig-i] + (A / diez[i]);
                for (j=0 ; j<tam && nuevos[j]!=C ; j++);
                if (C>A && C<=B && j==tam) {
                    nuevos[tam] = C;
                    resp++;
                    tam++;
                }
            }
            A++;
        }
        printf("Case #%d: %ld\n", t, resp);
    }
    return 0;
}