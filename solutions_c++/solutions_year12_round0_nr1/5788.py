#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <map>
#include <math.h>

using namespace std;

char s[50], w[1000];

int main(){
    s[0] = 'y'; s[1] = 'h'; s[2] = 'e';
    s[3] = 's'; s[4] = 'o'; s[5] = 'c';
    s[6] = 'v'; s[7] = 'x'; s[8] = 'd';
    s[9] = 'u'; s[10] = 'i';s[11] = 'g';
    s[12] = 'l';s[13] = 'b';s[14] = 'k';
    s[15] = 'r';s[16] = 'z';s[17] = 't';
    s[18] = 'n';s[19] = 'w';s[20] = 'j';
    s[21] = 'p';s[22] = 'f';s[23] = 'm';
    s[24] = 'a';s[25] = 'q';

    freopen("A-small-attempt0.IN", "r", stdin );
    freopen("sol.txt", "w", stdout);

    int n;
    scanf("%d", &n ); getchar();
    for(int i = 0; i < n; ++i){
        gets(w);
        printf("Case #%d: ", i+1);
        int l = strlen(w);
        for(int j = 0; j < l; ++j){
            if( isspace(w[j]) )putchar(' ');
            else putchar(s[w[j]-'a']);
        }
        putchar('\n');
    }

    return 0;
}



