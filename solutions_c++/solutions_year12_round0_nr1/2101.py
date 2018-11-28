
#include<iostream>
#include<stdio.h>
#include<string.h>
#include<string>
using namespace std;
typedef long long LL;
string G[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv"};
string E[] = {"our language is impossible to understand","there are twenty six factorial possibilities","so it is okay if you want to just give up"};
int t,txt,gToEng[200];
char text[200];
int main(){
    freopen("1.txt","r",stdin);
    freopen("out.txt","w",stdout);
    for(int i = 0; i < 200; ++i)gToEng[i] = i;
    for(int i = 0; i < 3; ++i)for(int j = 0; j < G[i].size(); ++j)gToEng[G[i][j]] = E[i][j];
    gToEng['z'] = 'q'; gToEng['q'] = 'z';
    scanf("%d",&t);
    gets(text);
    while(t--){
        gets(text);
        printf("Case #%d: ",++txt);
        for(int i = 0; text[i]; ++i)printf("%c",gToEng[text[i]]);
        printf("\n");
    }
    return 0;
}
