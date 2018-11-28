#include <cstdio>
#include <cstring>
#include<readline/readline.h>
#include<readline/history.h>
#include<iostream>

using namespace std;


char tab[5000][16];
int l,d,n;
char word[1000];
short map[16][30];

int run() {
    for(int i=0;i<l;i++) {
        for(int j=0;j<30;j++) {
            map[i][j] = 0;
        }
    }

    int k=0;
    int pos=0;
    while(word[k]) {
        if(word[k] == '(') {
            k++;
            while(word[k]!=')') {
                map[pos][ word[k]-'a' ] = 1;
                k++;
            }
        } else {
            map[pos][ word[k]-'a' ] = 1;
        }
        k++;
        pos++;
    }
    /*
    for(int i=0;i<d;i++) {
        for(int j=0;j<28;j++) {
            printf("%d ", map[i][j]);
        }
        printf("\n");
    }*/
    int result = 0;
    for(int i=0;i<d;i++) {
        bool is=true;
        for(int j=0;j<l;j++) {
            if( !map[j][tab[i][j]-'a'] ) {
                is = false;
                //printf("nie %d %d %d\n", tab[i][j], i, j);
                break;
            }
        }
        if(is) {
            result++;
        }
    }
    return result;
}

void load() {
    scanf("%d %d %d\n", &l, &d, &n);
    for(int i=0;i<d;i++) {
        scanf("%s", tab[i]);
    }

    for(int i=1;i<=n;i++) {
        scanf("%s", word);
        printf("Case #%d: %d\n", i, run());
    }
}

int main() {
    load();
    return 0;
}
