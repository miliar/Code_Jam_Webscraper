#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <queue>
using namespace std;

char hash[26];

void ff(){
    char aa[3][150] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv"};
    char bb[3][150] = {"our language is impossible to understand",
        "there are twenty six factorial possibilities","so it is okay if you want to just give up"};
    int i, j;
    for(i = 0; i < 3; ++i){
        for(j = 0; aa[i][j];++j){
            if(aa[i][j] == ' ') continue;
            hash[aa[i][j] - 'a'] = bb[i][j];
        }
    }
}

int main()
{
    ff();
    hash[16] = 'a' + 25;
    hash[25] = 'a' + 16;
    int T;
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("1.txt", "w", stdout);
    scanf("%d", &T);
    getchar();
    int cas = 1;
    while(T--){
        char a[150];
        gets(a);
        int i;
        for(i = 0; a[i]; ++i){
            if(a[i] == ' ')
                continue;
            a[i] = hash[a[i] - 'a'];
        }
        printf("Case #%d: ", cas++);
        puts(a);
    }
    return 0;
}