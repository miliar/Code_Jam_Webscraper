#include <stdio.h>
#include <string.h>

char c[256];

void init(){
    for (int i=0; i<256; i++)
        c[i] = i;
    char s0[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    char ss0[] = "our language is impossible to understand";
    char s1[] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    char ss1[] = "there are twenty six factorial possibilities";
    char s2[] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    char ss2[] = "so it is okay if you want to just give up";

    c['a'] = 'y';
    c['o'] = 'e';
    c['z'] = 'q';
    c['q'] = 'z';

    for (int i=0; i<(int)strlen(s0); i++){
        c[s0[i]] = ss0[i];
    }

    for (int i=0; i<(int)strlen(s1); i++){
        c[s1[i]] = ss1[i];
    }

    for (int i=0; i<(int)strlen(s2); i++){
        c[s2[i]] = ss2[i];
    }
/*
    bool b[256];
    memset(b, false, sizeof(b));
    for (char ch='a'; ch<='z'; ch++){
        b[c[ch]] = true;
        if (c[ch]==ch){
            printf("%c\n",ch);
        }
    }
    for (char ch='a'; ch<='z'; ch++){
        if (!b[ch]){
            printf("%c\n",ch);
        }
    }
*/
}

int main(){
    init();
    int t;
    char s[200];
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small-attempt2.out","w",stdout);
    scanf("%d\n",&t);
    for (int k=1; k<=t; k++){
        gets(s);
        for (int i=0; i<(int)strlen(s); i++){
            s[i] = c[s[i]];
        }
        printf("Case #%d: %s\n",k,s);
    }
    return 0;
}
