
#include <cstdlib>
#include <stdio.h>
#include <string.h>
using namespace std;

int rep[256];
void init(){
    char c[][128] = {   "ejp mysljylc kd kxveddknmc re jsicpdrysi",
                        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                        "de kr kd eoya kw aej tysr re ujdr lkgc jv" };
    char m[][128] = {   "our language is impossible to understand",
                        "there are twenty six factorial possibilities",
                        "so it is okay if you want to just give up"};
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < strlen(c[i]); j++){
            rep[c[i][j]] = m[i][j];
        }
    }
    rep['q'] = 'z';
    rep['z'] = 'q';
    rep[' '] = ' ';
}
int main(){
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    init();
    int t, i, kase = 0;
    char s[128];
//    for(i = 97; i < 97 + 26; i++){
//        printf("%c = %c\n", i, rep[i]);
//    }
    gets(s);
    sscanf(s, "%d", &t);
    while(t--){
        gets(s);
        for(i = 0; i < strlen(s); i++)
            s[i] = rep[s[i]];
        printf("Case #%d: %s\n", ++kase, s);
    }
    return 0;
}
