#include<stdio.h>
#define MINI(a,b) ((a)<(b)?(a):(b))
#define MAXI(a,b) ((a)>(b)?(a):(b))
char map[26];
char str[103];
bool vis1[26], vis2[26];
char *in[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
char *out[3] = {"our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"};
int main()
{
    freopen("data.txt","r",stdin);
    freopen("Aout.txt","w",stdout);
    int i,j;
    map['z' - 'a'] = 'q' - 'a';
    map['q' - 'a'] = 'z' - 'a';
    vis1['z' - 'a'] = true;
    vis2['q' - 'a'] = true;
    vis2['z' - 'a'] = true;
    vis1['q' - 'a'] = true;
    for (i=0; i<3; ++i)
    {
        for (j=0; in[i][j]; ++j)
        {
            if (in[i][j] == ' ') continue;
            map[in[i][j]-'a'] = out[i][j]-'a';
            vis1[out[i][j]-'a'] = true;
            vis2[in[i][j] - 'a'] = true;
        }
    }
    /*for (i=0; i<26; ++i) printf("%c : %c :: %d %d\n", i+97, map[i]+97, vis1[i],vis2[i]);*/
    int t,T;
    scanf("%d",&T);
    getchar();
    for (t=1; t<=T; ++t)
    {
        gets(str);
        printf("Case #%d: ",t);
        for (i=0; str[i]; ++i)
        {
            if (str[i]==' ') printf(" ");
            else printf("%c",map[str[i]-'a']+'a');
        }
        puts("");
    }
    return 0;
}
