#include<cstdio>

using namespace std;

char m[256];

const char s[3][100] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
                    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                    "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
const char t[3][100] = {"our language is impossible to understand",
                    "there are twenty six factorial possibilities",
                    "so it is okay if you want to just give up"};

char ss[110];
int main() {
    for(int i = 0; i < 256; i ++)
        m[i] = i;
    m['y'] = 'a';
    m['e'] = 'o';
    m['q'] = 'z';
    for(int i = 0; i < 3; i ++) {
        int j = 0;
        while(s[i][j]) {
            m[s[i][j]] = t[i][j];
            j++;
        }
    }
    for(int i = 'a'; i <= 'z'; i ++) {
        bool ok = false;
        for(int j = 'a'; j <= 'z'; j ++)
            if(m[j]==i) ok = true;
        if(!ok) m['z'] = i;
    }
    int t;
    scanf("%d\n", &t);
    for(int i = 1; i <= t; i ++) {
        gets(ss);
        printf("Case #%d: ",i);
        int j = 0;
        while(ss[j]) {
            printf("%c", m[ss[j]]);
            j++;
        }
        printf("\n");
    }
}
