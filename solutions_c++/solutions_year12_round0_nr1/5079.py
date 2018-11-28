#include<stdio.h>
#include<vector>
#include<string>
#include<math.h>
#include<algorithm>
using namespace std;

#define sz size()
#define pb push_back
#define len length()
#define clr clear()

#define eps 0.0000001
#define PI  3.14159265359

int main() {

    FILE *ff=fopen("A-small-attempt0.in", "r"), *gg=fopen("A-small-attempt0.out", "w");

    int i,j,q,tt,ttt,n;
    char s[555],ps[555];
    string t1[5]={"our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up", "aoz"};
    string t2[5]={"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv", "yeq"};

    for(i='a'; i<='z'; i++) s[i]='?';

    for(i=0; i<4; i++) {
        q=t1[i].len;
        for(j=0; j<q; j++) s[t2[i][j]]=t1[i][j];
    }

    s['z'] = 'q';
    //for(i='a'; i<='z'; i++) printf("%c ", s[i]);


    fscanf(ff,"%d\n", &ttt);
    for(tt=1;tt<=ttt;tt++) {

        fgets(ps,1000,ff);
        n=strlen(ps);
        fprintf(gg,"Case #%d: ", tt);
        for(i=0; i<n; i++) {
            if (ps[i]>='a' && ps[i]<='z') fprintf(gg,"%c", s[ps[i]]); else fprintf(gg,"%c", ps[i]);
        }
    }

    fclose(ff); fclose(gg);

    return 0;
}
