#include<stdio.h>
#include<iostream>
#include<map>
#include<string.h>
#include<string>
#include<algorithm>
using namespace std;

char ss[26], s[1010];

int main()
{
    freopen("A-small-attempt8.in", "r", stdin);
    freopen("a-out.out", "w", stdout);
    int _, tt = 1;
    scanf("%d", &_);
    ss[0] = 'y', ss[1] = 'h', ss[2] = 'e', ss[3] = 's';
    ss[4] = 'o', ss[5] = 'c', ss[6] = 'v', ss[7] = 'x';
    ss[8] = 'd', ss[9] = 'u', ss[10] = 'i', ss[11] = 'g';
    ss[12] = 'l', ss[13] = 'b', ss[14] = 'k', ss[15] = 'r';
    ss[16] = 'z', ss[17] = 't', ss[18] = 'n', ss[19] = 'w';
    ss[20] = 'j', ss[21] = 'p', ss[22] = 'f', ss[23] = 'm';
    ss[24] = 'a', ss[25] = 'q';
    gets(s);
    while(_--){
        gets(s);
        int n = strlen(s);
        for(int i = 0; i < n; i++){
            int k = s[i] - 'a';
            if(s[i] != ' ') s[i] = ss[k];
        }
        printf("Case #%d: %s\n", tt++, s);
    }

    return 0;
}
