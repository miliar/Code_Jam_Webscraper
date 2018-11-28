#include <cstdio>
#include <cstring>
char str1[150], str2[150];
//char mp[26];

char mp[26] = {'y', 'h', 'e', 's', 'o', 'c' ,
'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k',
 'r', 'z' ,'t', 'n', 'w', 'j', 'p', 'f' ,'m', 'a', 'q'} ;

int cnt[26];

int main() {
    freopen("A-small-attempt4.in", "r", stdin);
    freopen("A-small-attempt4.out", "w", stdout);
    int ct, i, len, T;
    scanf("%d",&T);
    gets(str1);
    //memset(mp, '0', sizeof(mp));
     memset(cnt, 0, sizeof(cnt));
    for (ct = 1; ct <= T; ct++) {
        gets(str1);
        //gets(str2);
        
        //printf("%s\n",str1);
       //  printf("%s\n",str2);
        len = strlen(str1);
        strcpy(str2, str1);
       // memset(cnt, 0, sizeof(cnt));
        for (i = 0; i < len; i++) {
            if ( !(str1[i] >= 'a' && str1[i] <= 'z') ) continue;
           // if (mp[ str1[i] - 'a' ] == 0) {
             //   mp[ str1[i] - 'a' ] = str2[i];       
            //}
            str2[i] = mp[ str1[i] - 'a'];
           // printf("%d\n",str1[i] - 'a');
           //cnt[ str1[i] - 'a']++;
        }
        printf("Case #%d: %s\n",ct, str2);
    }
    /*
    for (i = 0; i < 26; i++) {
        //if (cnt[i] == 0) {
           printf("%c %d %c\n",i + 'a', cnt[i], mp[i]);       
        //}
    }
    while (1);
    */
    return 0;
}