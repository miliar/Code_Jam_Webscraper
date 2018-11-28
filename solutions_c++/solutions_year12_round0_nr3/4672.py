#include<cstdio>
#include<cstring>
#include<iostream>
#include<ctype.h>
using namespace std;

int main() {
    int T;
    char strT[10];
    FILE *in, *out;
    in = freopen("input_c.in", "r+", stdin);
    out = freopen("output_c.out", "w+", stdout);
    fgets(strT, 10, stdin);
    T = atoi(strT);
    
    for (int i=1; i<=T; i++) {
        
        long int A, B, count = 0;
        char strM[50], strN[50];
        scanf("%li%li", &A, &B);
        for (long int m = A; m <= B; m++) {
                sprintf(strM, "%li%li", m, m);
              //  printf("%s\n",strM);
                for(long int n = m+1; n <= B; n++) {
                              
                         sprintf(strN, "%li", n);
                    //     printf("in: %s\n", strN);
                         char *result = strstr(strM, strN);
                         if (result!= NULL) {
                            count++;
                         }
                         
                } 
        }
        printf("Case #%d: %li\n", i, count);
    }
}
