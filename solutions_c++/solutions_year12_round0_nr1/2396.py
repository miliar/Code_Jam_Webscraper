#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<map>
using namespace std;
map <char, char> dict;
string s, v;
char p[1000];

int main () {
    s = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    v = "our language is impossible to understand";
    for (int c = 0; c < s.size(); c++) {
        dict[s[c]] = v[c];
    }
    s = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    v = "there are twenty six factorial possibilities";
    for (int c = 0; c < s.size(); c++) {
        dict[s[c]] = v[c];
    }
    s = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    v = "so it is okay if you want to just give up";
    for (int c = 0; c < s.size(); c++) {
        dict[s[c]] = v[c];
    }
    dict['q'] = 'z';
    dict['z'] = 'q';
    int t;
    scanf("%d", &t);
    for (int lo = 1; lo <= t; lo++) {
        scanf(" ");
        gets(p);
        int x= strlen(p);
        printf("Case #%d: ", lo);
        for (int c = 0; c < x; c++) {
            printf("%c", dict[p[c]]);
        }
        printf("\n");
    }
    return 0;
}
        
