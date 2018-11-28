#include <stdio.h>

#include <iostream>
#include <string>
using namespace std;

int main()
{
    freopen("A-small-attempt3.in", "r", stdin);
    freopen("A-out.txt", "w", stdout);
    char decode[256];
    string s = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    string r = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
    int i;
    for(i = 0; i < s.size(); i++)
        decode[s[i]] = r[i];
    decode['y'] = 'a';
    decode['e'] = 'o';
    decode['q'] = 'z';
    decode['z'] = 'q';
    int x, t;
    string in;
    scanf("%d ", &t);
    for(x = 1; x <= t; x++) {
        getline(cin, in);
        printf("Case #%d: ", x);
        for(i = 0; i < in.size(); i++)
            printf("%c", decode[in[i]]);
        printf("\n");
    }
    return 0;
}
