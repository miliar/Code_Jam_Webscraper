#include <stdio.h>
#include <string.h>
#include <memory.h>

const int M = 10000;

char s[510];
char t[] = "welcome to code jam";

int d[510][20];

int main() {
    int N;
    scanf("%d\n",&N);
    for(int ca=1;ca<=N;ca++) {
        gets(s);
        memset(d,0,sizeof(d));
        d[0][0] = (s[0]==t[0]?1:0);
        for(int i=1;s[i];i++) {
            d[i][0] = d[i-1][0] + (s[i]==t[0]?1:0);
        }
        int i,j;
        for(i=1;s[i];i++) {
            for(j=1;t[j];j++) {
                if(s[i]==t[j]) {
                    d[i][j] = (d[i-1][j] + d[i-1][j-1]) % M;
                }
                else {
                    d[i][j] = d[i-1][j];
                }
            }
        } 
        //printf("%d %d %d\n",i,j,d[i-1][0]);
        printf("Case #%d: %04d\n",ca, d[i-1][j-1]);
    }
    return 0;
}

