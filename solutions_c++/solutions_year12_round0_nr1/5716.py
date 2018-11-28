#include <cstdio>
using namespace std;

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    char a[3][100] = {
         "ejp mysljylc kd kxveddknmc re jsicpdrysi", 
         "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", 
         "de kr kd eoya kw aej tysr re ujdr lkgc jv"
    };
    
    char b[3][100] = {
         "our language is impossible to understand", 
         "there are twenty six factorial possibilities",
         "so it is okay if you want to just give up"
    };

    
    char map[26] = {0};
    map['z'-'a'] = 'q';
    map['q'-'a'] = 'z';
    int seen[26] = {0};
    seen['q'-'a'] = 1;
    for(int i = 0; i < 3; i++) {
            for(int j = 0; a[i][j]; j++) {
                 if(a[i][j]!=' ') {
                               
                               map[a[i][j]-'a'] = b[i][j];
                               
                               
                               seen[b[i][j]-'a'] = 1;
                 }
            }
    }
    
    bool ok = true;
    for(int i = 0; i < 26; i++) {
            if(!map[i]) {
                        printf("%c\n", i+'a');
                        ok = false;
            }
    }
    //printf("%s\n", ok?"Solved it!":"Not Solved\n");
    
    int t;
    scanf("%d\n", &t);
    char dummy[100];
    for(int test = 1; test <= t; test++) {
            char s[100];
            gets(s);
            printf("Case #%d: ", test);
            for(int k = 0; s[k]; k++) {
                    putchar(s[k]==' '?' ':map[s[k]-'a']);
            }
            putchar('\n');
    }
}
               
                   
