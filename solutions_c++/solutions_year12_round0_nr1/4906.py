#include<cstdio>
#include<cstring>
#include<iostream>
#include<string>
#include<cassert>

using namespace std;

char mp[26];

int main()
{
    char a[][105] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
                     "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                     "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
    char b[][105] = {"our language is impossible to understand",
                        "there are twenty six factorial possibilities",
                        "so it is okay if you want to just give up"};
    int cc = 0;

    memset(mp,0,sizeof(mp));
    for(int i = 0;i < 3; ++i)
    {
        for(int j  =0; j < strlen(a[i]); ++j) if(a[i][j] != ' ')
        {
            if(mp[(int)a[i][j] - 97] != 0) assert(mp[(int)a[i][j] - 97] == b[i][j]);
            else {mp[(int)a[i][j] - 97] = b[i][j]; cc++;}
        }
    }

    mp[25] = 'q';
    mp[(int)('q') - 97] = 'z';

    //cerr << cc <<endl;
    //for(int i = 0; i < 26; ++i) fprintf(stderr, "%c -- %c\n", (char)(i+97), mp[i]);
    int T;
    scanf("%d\n",&T);
    char out[105];

    for(int ii = 1; ii <= T;++ii)
    {
        string str;
        getline(cin,str);
        memset(out, 0, sizeof(out));
        for (int i = 0; i < str.length(); ++i)
        {
            if (str[i] == ' ') out[i] = ' ';
            else out[i] = mp[(int)(str[i]) - 97];
        }
        assert(strlen(out) == str.length());
        printf("Case #%d: %s\n",ii,out);
    }
    return 0;
}
