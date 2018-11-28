#include <cstdio>
#include <cstring>
#include<readline/readline.h>
#include<readline/history.h>
#include<iostream>

using namespace std;

#define LEN 19

char str[] = "welcome to code jam";
const char *s;
int tab[501][20];
int n;

int run() {
    for(int i=0;i<strlen(s);i++) {
        for(int j=0;j<LEN;j++) {
            if(i!=0) {
                tab[i][j] = tab[i-1][j];
            } else {
                tab[i][j] = 0;
            }
            //printf("%c  - %c\n", s[i], str[j]);
            if(s[i] == str[j]) {
                if(j==0) {
                    tab[i][j] += 1;
                    //printf("add 1\n");
                } else {
                    tab[i][j] += tab[i][j-1];
                    //printf("add +%d\n", tab[i][j-1]);
                }
            }
            //printf("state: %d %d\n", j, tab[i][j]);
            tab[i][j] = tab[i][j] % 10000;
        }
    }
    return tab[strlen(s)-1][LEN-1];
}

void load() {
    std::string line;
    std::getline(cin, line);
    n = atoi(line.data());
    for(int i=1;i<=n;i++) {
        std::getline(cin, line);
        s = line.data();
        //printf("%s\n", s );
        printf("Case #%d: %04d\n", i, run());
    }
}

int main() {
    load();
    return 0;
}
