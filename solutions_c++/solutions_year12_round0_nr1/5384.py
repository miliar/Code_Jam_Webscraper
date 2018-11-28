#include <stdio.h>
#include <string.h>

char mp[30];
char s[40][110], t[40][110];

int main()
{
    int T, i, j;
    mp[0] = 'y';
    mp[1] = 'h';
    mp[2] = 'e';
    mp[3] = 's';
    mp[4] = 'o';
    mp[5] = 'c';
    mp[6] = 'v';
    mp[7] = 'x';
    mp[8] = 'd';
    mp[9] = 'u';
    mp[10] = 'i';
    mp[11] = 'g';
    mp[12] = 'l';
    mp[13] = 'b';
    mp[14] = 'k';
    mp[15] = 'r';
    mp[16] = 'z';
    mp[17] = 't';
    mp[18] = 'n';
    mp[19] = 'w';
    mp[20] = 'j';
    mp[21] = 'p';
    mp[22] = 'f';
    mp[23] = 'm';
    mp[24] = 'a';
    mp[25] = 'q';
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out.txt", "w", stdout);
    scanf("%d", &T);
    gets(s[0]);
    for(i = 0; i < T; ++i) {
        gets(s[i]);
        int len = strlen(s[i]);
        for(j = 0; j < len; ++j) {
            if(s[i][j] == ' ')
                t[i][j] = ' ';
            else
                t[i][j] = mp[s[i][j] - 'a'];
        }
        t[i][j] = 0;
        printf("Case #%d: %s\n", i + 1, t[i]);
    }
    /*for(i = 0; i < T; ++i)
        gets(t[i]);
    for(i = 0; i < 26; ++i)
        mp[i] = ' ';
    for(i = 0; i < T; ++i) {
        int len = strlen(s[i]);
        for(j = 0; j < len; ++j) {
            if(s[i][j] == ' ') continue;
            if(mp[s[i][j] - 'a'] == ' ')
                mp[s[i][j] - 'a'] = t[i][j];
            else {
                if(mp[s[i][j] - 'a'] != t[i][j])
                    printf("error\n");
            }
        }
    }
    for(i = 0; i < 26; ++i)
        printf("mp[%d] = '%c';\n", i, mp[i]);*/
    return 0;
}
