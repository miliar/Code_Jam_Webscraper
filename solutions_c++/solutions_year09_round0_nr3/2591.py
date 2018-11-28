#include <cstdio>
#include <cstring>
using namespace std;

FILE *in = fopen("input.txt","rt");
FILE *out = fopen("output.txt","wt");

char goal[] = "welcome to code jam";
int dy[ 501 ][ 21 ];
char str[ 501 ];
int ans;

void input() {
    fgets(str, 500, in);
    memset( dy, 0, sizeof(dy) ) ;
}

void process() {
    int i, j, k;
    for( i=0; i<strlen(str); i++ ) if( str[i] == 'w' ) dy[i][0] = 1;
    for( i=1; i<strlen(goal); i++ ) {
        for( j=i; j<strlen(str); j++ ) {
            if( str[j] == goal[i] ) for(k=0; k<j; k++) dy[j][i] = (dy[j][i] + dy[k][i-1]) % 10000;
        }
    }
    ans = 0;
    for( i=0; i<strlen(str); i++ ) 
        ans = (ans + dy[i][strlen(goal)-1]) % 10000;
}

void output() { 
    fprintf(out,"%04d\n", ans);
}

int main()
{
    int t, tcnt;
    fscanf(in,"%d\n",&t);
    for( tcnt=1; tcnt<=t; tcnt++ ) {
        input();
        process();
        fprintf(out,"Case #%d: ", tcnt);
        output();
    }
    return 0;
}